import sys
from io import StringIO
import streamlit as st
import numpy as np
from PIL import Image, ImageDraw, ImageColor
from canvas import *
from streamlit_ace import st_ace
import extra_streamlit_components as stx
from sewar.full_ref import uqi
from lines import *
from triangle import *

st.set_page_config(page_title="How to play Shape Puzzle", page_icon=":notebook:")


with st.sidebar:
    color = st.color_picker('color picker', '#00f900', key='l_c')
    st.write(ImageColor.getrgb(color))

st.header("Chapter 1: Lines and Triangles")
st.write("##")
st.divider()

with st.expander("Tutorial No.1: Line segments"):

    st.markdown("#### Let's start with playing with line-segments")
    st.markdown(
    """
        1. We will firstly draw a simple line-segment. The easiest way to do so is using our line function:
            ```python
            line2P(start, point)
            ```
            - In the code window below, define two points on the canvas by:

            ```python
            a = (-100, 0) ## the x-axis is -100 and y-axis is 0
            b = (100, 0)  ## the x-axis is 100 and y-axis is 0
            line2P(a, b)  ## then call our line2P function to draw the line
            ```

            You should see a horizontal line-segment in the canvas. 
            Feel free to change the color or the width of drawing by refering the "Functions" page from side bar.

        2. Our 2nd Line function, LineDraw():
            Sometimes, it might be easier to just start from a single point, but thinking about the direction and the length of drawing a 
            line segment. This is more intuitive for the real drawing scenario.

            - In the code window below, define a point and the length and angle you want to draw :

            ```python
            a = (-100, 0) ## the x-axis is -100 and y-axis is 0
            angle = 45  ## 45 degree anti-clock wise
            length = 200 ## length of the drawing
            lineDraw(a, angle, length, width=50)  ## then call our lineDraw function to draw the line
            ## We can also specify the width of drawing by passing parameter explicitly.
            ```

            You should see a slant line-segment in the canvas.
        
        3. Release the power of for-loop:
            The most powerful part of drawing through code is the capability of producing iterative graphs. 
            The more detailed instruction about Python for-loops, please check [here](https://www.w3schools.com/python/python_for_loops.asp)

            - In the code window below, define a startinig point and using for-loop and lineDraw:

            ```python
            c = (-50,-100) ## The starting point to draw
            lst = [c]  ## Create a list for later reference
            for i in range (100): ## Iterate 100 rounds
                l = lineDraw(lst[-1], i*125, 300, (212, 16, 16), width=2) ## Try to figure out what are we doing here?
                lst.append(l['end']) ## add the end-point of the line drawn to the list for the next iteration
            ```
        4. Now, see if you can produce a shape stated in "target shape":

            ```python
            s = (0,0) ## The starting point
            n = 8 ## 
            lst = [s]

            #### Start your for-loop here ####

            #### End of your for-loop ####
            ```
            Having fun!!
    """
    )

    st.divider()
    st.markdown("###### Write your code here")
    ## Code input
    code1 = st_ace(language="python", theme="tomorrow_night_bright", keybinding="vscode", font_size=14, tab_size=4, show_gutter=True, min_lines=10, key="ace",)
    o1, o2 = st.columns(2)
    if code1:
        ImageDraw.Draw(img).rectangle([(0, 0), (c_length,c_height)], fill = c_color, outline = c_outline, width=2)
        redirected_output = sys.stdout = StringIO()
        try:
            exec(code1)
            result = str(redirected_output.getvalue())
            st.code(result)
        except Exception as e:
            st.code(str(e))
    with o1:
        st.markdown("##### Target Shape:"); target = Image.open('image/T1_t.jpg')
        t2 = target.resize((c_length,c_height))
        ImageDraw.Draw(img_t).rectangle([(0, 0), (c_length,c_height)], fill = c_color, outline = c_outline, width=2)
        img_t.paste(t2); st.image(img_t); st.session_state['imt'] = np.array(img_t)
    with o2:
        st.markdown("##### Output Shape"); st.image(img, caption=''); st.session_state['imo'] = np.array(img)
    
    sim = round(uqi(st.session_state['imt'],st.session_state['imo']),4)
    st.write(f"The similarity score between target and output: {sim}")


with st.expander("Tutorial No.2: Triangles and Transformations 1"):

    st.markdown("Now, we will start to draw more cool shapes")
    st.markdown(
    """
        1. The simplest way to draw a triangle is to define three points on the canvas:

            - In the code window below, define two points on the canvas by:

            ```python
            a = (-100, 0) ## the x-axis is -100 and y-axis is 0
            b = (100, 0)  ## the x-axis is 100 and y-axis is 0
            c = (0, 200) ## the x-axis is 0 and y-axis is 200
            triangle_base(a,b,c, fill = (0, 249, 0), color=(0,0,0))  ## then call our basic triangle function to draw the shape

            ```

            You should see a isosceles triangle in the canvas. 
            In the triangle_base() function, we have two parameters for coloring:
            -- the "fill" is for the color filled in the triangle
            -- the "color" is color of the edge of the triangle
            

        2. Our 2nd Triangle function, triangle_LP():

            Again, it might be easier to just start from a line, but thinking about another point to draw a 
            triangle. This is convient for some scenario when iteration applies.

            - In the code window below, try the follow drawing:

            ```python
            for i in range (10): # We create an iteration of 10
            
                # Each iteration, draw a line with one different end point per iter
                l = line2P((100,0+i*10),(-300,100), (0, 249, 0))
                # then for each different line drawn, touch it to a fixed point (150,150) to form a triangle
                triangle_LP(l, (150,150), (0, 249, 0))
            ```

            You should see a repeated triangle shape in the canvas.
        
        3. Transform of shapes 1: Rescale:

            Shape transformations are very helpful functions in drawing shapes. 

            The first transformation we are trying is Rescale, 

            - In the code window below, define a startinig triangle from triangle_base() and then scale it:

            ```python
            a = (-100, 0) ## the x-axis is -100 and y-axis is 0
            b = (100, 0)  ## the x-axis is 100 and y-axis is 0
            c = (0, 200) ## the x-axis is 0 and y-axis is 200
            ### Our initial triangle, give it a name, t
            t = triangle_base(a,b,c, fill = (0, 249, 0), color=(0, 249, 0))

            ### we rescale it with half size
            ### 1. We use the default color here, which was filled with canvas color and edge with black
            ### 2. We choose redraw=False, this means keep the original triangle t
            ##### 2.5 If we are passing redraw=True, the t will disappear. 
            t2 = rescale_c(t, alpha=0.5, redraw=False)
            ```

            You might already see a chance of creating a for-loop for some great design? 

            The rescale function we used above is rescaling based on centre of triangle, we can also use another 
            rescale function rescale_p() to specify the point we want to base on for rescaling.

            - In the code window below, following the code from above, paste the next snippet

            ```python
            a = (-100, 0) ## the x-axis is -100 and y-axis is 0
            b = (100, 0)  ## the x-axis is 100 and y-axis is 0
            c = (0, -200) ## the x-axis is 0 and y-axis is 200
            ### Our initial triangle, give it a name, t
            t3 = triangle_base(a,b,c, fill = (201, 64, 26), color=(201, 64, 26))

            ### we rescale it with half size, but at different point 
            t4 = rescale_p(t3, 'p2', alpha=0.5, redraw=False)
            ```

        4. Transform of shapes 2: Translation:

            The second transformation we are introducing is translation,

            - In the code window below, define a startinig triangle from triangle_base() and then Translate it
            to different location:

            ```python
            a = (-200, 0) ## the x-axis is -100 and y-axis is 0
            b = (10, 0)  ## the x-axis is 100 and y-axis is 0
            c = (0, -100) ## the x-axis is 0 and y-axis is 200
            ### Our initial triangle, give it a name, t
            t5 = triangle_base(a,b,c, fill = (201, 64, 26), color=(201, 64, 26))

            ## We use vector here to specify the direction and magnitute of translation. 
            ## The translate_o() function is traslating triangles by a vector defined from the 
            ## origin. i.e. the center of the canvas.
            t6 = translate_o(t3, vector = (100,150), redraw=False)
            ```

            Now we should try the effect of translate by a vector defined from a point of the triangle

            - In the code window below, define a startinig triangle from triangle_base() and then Translate it
            to different location, using translate_p() function:

            ```python
            a = (-20, 0) ## the x-axis is -100 and y-axis is 0
            b = (10, 0)  ## the x-axis is 100 and y-axis is 0
            c = (0, -100) ## the x-axis is 0 and y-axis is 200
            ### Our initial triangle, give it a name, t
            t7 = triangle_base(a,b,c, fill = (201, 64, 26), color=(201, 64, 26))

            translate_p(t7, vector = (-10,10), point = 'p2', redraw=False)
            ```
            The code above specify "P2" as origin of translation rather than center of canvas

        5. Using data for more complicated design:

            Read the code below and check out the output from a more specific design

            ```python
            b_line = line2P((-200,-160),(200,-160),color='black') # set the baseline
            tpoint = (0,200) # set the top point of the triangle

            # Create the first triangle
            t1 = triangle_LP(b_line,tpoint,color='black',fill='black')
            # Translate the triangle_LP
            down_vector = (0,-50)
            t2 = translate_o(t1, down_vector,fill=None, redraw=False) 

            # Redraw the edge of the second triangle

            l1 = line2P(t2['p1'], t2['p2'], color='white', width=10)
            l2 = line2P(t2['p1'], t2['p3'], color='white', width=10)
            l3 = line2P(t2['p2'], t2['p3'], color='white', width=10)

            ## Find two intersections on the baseline

            p1 = lines_intersection(l2, b_line)
            p2 = lines_intersection(l3, b_line)

            ## Redraw the line-segment with information

            l4 = line2P(p1, t2['p1'], color = 'black', width=10)
            l5 = line2P(p2, t2['p2'], color = 'black', width=10)
            l3 = line2P(t2['p1'], t2['p2'], color = 'black', width=10)
            ```

            Feel free to play around the code above to try different design.

        6. Try to design/create a shape like the target shape :)
            
    """
    )

    st.divider()
    st.markdown("###### Write your code here")
    ## Code input
    code2 = st_ace(language="python", theme="tomorrow_night_bright", keybinding="vscode", font_size=14, tab_size=4, show_gutter=True, min_lines=10, key="ace2",)
    o1, o2 = st.columns(2)
    if code2:
        ImageDraw.Draw(img).rectangle([(0, 0), (c_length,c_height)], fill = c_color, outline = c_outline, width=2)
        redirected_output = sys.stdout = StringIO()
        try:
            exec(code2)
            result = str(redirected_output.getvalue())
            st.code(result)
        except Exception as e:
            st.code(str(e))
    with o1:
        st.markdown("##### Target Shape:"); target = Image.open('image/T2_t.jpg')
        t2 = target.resize((c_length,c_height))
        ImageDraw.Draw(img_t).rectangle([(0, 0), (c_length,c_height)], fill = c_color, outline = c_outline, width=2)
        img_t.paste(t2); st.image(img_t); st.session_state['imt'] = np.array(img_t)
    with o2:
        st.markdown("##### Output Shape"); st.image(img, caption=''); st.session_state['imo'] = np.array(img)
    
    sim = round(uqi(st.session_state['imt'],st.session_state['imo']),4)
    st.write(f"The similarity score between target and output: {sim}")



with st.expander("Tutorial No.3: Transformation 2, Rotation and Reflection"):

    st.markdown("We will continues on more transformations that helps us to create shape designs")
    st.markdown(
    """
        1. Rotation by a point on the canvas:

            - Copy and past the code below to the code window:

            ```python
            P1=(100,100); P2=(200,50); P3=(-10,-50)

            t = triangle_base(P1, P2, P3, 'red')
            t1 = rotation(t,redraw=False, fill='blue') ## Rotation by the origin (0,0), default
            # rotate 90 degree based on a point from the triangle
            t2 = rotation(t, t['p1'], redraw = False, fill = 'yellow')
            # rotate 120 degree based on a point on the canvas
            t3 = rotation(t, (-50, 100), angle=120, redraw=False, fill='orange')

            ```

            You should see differernt rotations with different color 
            Carefully read the code and comments, figuring out:
            -- What is the parameter that control the point of rotation
            -- what is the parameter that control the degree of rotation
            

        2. Reflection by a line on the canvas:

            - Copy and past the code below to the code window:

            ```python
            P1=(100,100); P2=(200,50); P3=(-10,-50)

            t = triangle_base(P1, P2, P3, 'red')

            ## Define different lines
            l1 = line2P(t['p2'],t['p3'], 'green') 
            l2 = line2P((0,0),(0,200), 'yellow')
            l3 = line2P((100,0),(200,0), 'orange')

            ## Reflect by different lines:
            t3 = reflection(t, l1, redraw=False, fill='green')
            t4 = reflection(t, l2, redraw=False, fill='yellow')
            t5 = reflection(t, l3, redraw=False, fill='orange')
            ```

            You should see differernt reflection with different color 
            Carefully read the code and comments, figuring out:
            
            -- What is the parameter that control the line of reflection

        
        3. Translations with for loops

            Let's review the power of our favourate for-loops!

            - Copy and past the code below to the code window:

            ```python
            ## You can define the colors you are using at the beginning
            ## To choose the color, using color picker to get the hex code or RGB values
            B_color = 'white'
            P_color = (11, 129, 11)

            ## Define an initial triangle
            start = triangle_base((20,50),(20,80),(35,22.3),color=B_color)
            start = rescale_c(start,3,color=B_color)
            # try to reflect 1st time
            a = reflection(start,line2P(start['p1'],start['p2'],P_color),
                redraw=False,color=P_color)

            ## Looping around

            for i in range(12):
                a = reflection(a,line2P(a['p2'],a['p3']),redraw=False,color=P_color)
                a = reflection(a,line2P(a['p1'],a['p3']),redraw=False,color=P_color)
            ## After reflection you might want to fine-tune to add on another rotation
            reflection(a,line2P(a['p2'],a['p3'],P_color),redraw=False,color=P_color)

            ```

            You might also try some different colors for the flower --- 
            
        4.  Now, see if you can produce a shape stated in "target shape":




    """
    )
    st.divider()
    st.markdown("###### Write your code here")
    ## Code input
    code3 = st_ace(language="python", theme="tomorrow_night_bright", keybinding="vscode", font_size=14, tab_size=4, show_gutter=True, min_lines=10, key="ace3",)
    o1, o2 = st.columns(2)
    if code3:
        ImageDraw.Draw(img).rectangle([(0, 0), (c_length,c_height)], fill = c_color, outline = c_outline, width=2)
        redirected_output = sys.stdout = StringIO()
        try:
            exec(code3)
            result = str(redirected_output.getvalue())
            st.code(result)
        except Exception as e:
            st.code(str(e))
    with o1:
        st.markdown("##### Target Shape:"); target = Image.open('image/T3_t.jpg')
        t3 = target.resize((c_length,c_height))
        ImageDraw.Draw(img_t).rectangle([(0, 0), (c_length,c_height)], fill = c_color, outline = c_outline, width=2)
        img_t.paste(t3); st.image(img_t); st.session_state['imt'] = np.array(img_t)
    with o2:
        st.markdown("##### Output Shape"); st.image(img, caption=''); st.session_state['imo'] = np.array(img)
    
    sim = round(uqi(st.session_state['imt'],st.session_state['imo']),4)
    st.write(f"The similarity score between target and output: {sim}")