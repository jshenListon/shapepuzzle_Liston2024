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
from circle import * 

st.set_page_config(page_title="How to play Shape Puzzle", page_icon=":notebook:")


with st.sidebar:
    color = st.color_picker('color picker', '#00f900', key='l_c')
    st.write(ImageColor.getrgb(color))

st.header("Chapter 2: Arcs and Circles")
st.write("##")
st.divider()

with st.expander("Tutorial No.1: Circles in different way of drawing"):

    st.markdown("#### Let's start with circle functions.")
    st.markdown(
    """
        1. Easy like previously, define or claim the key variables, then call the function to draw a circle.
        Be aware that once the size or circle are larger than our size of canvas, that part would not be shown on the canvas.

            ```python
            ## Claim the center and radiu
            center = (100, -100)
            radiu = 400
            ## Call the function
            circle_c_r(center, radiu, fill = (201, 30, 30), color = (201, 30, 30))
            ```
            Now, by simply design the center of circles and the radius, you can generate some cool design, for example

            ```python
            ## Claim the center and radiu
            center = (100, -100)
            radiu = 400
            ## Call the function
            circle_c_r(center, radiu, fill = (201, 30, 30), color = (201, 30, 30))

            c1 = (150, -80)
            r1 = 150
            circle_c_r(c1, r1, fill = 'white', color = 'white')
            ```

        2. Our 2nd circle function, circle_draw():
            Sometimes, we might not be able to "see" the center but rather starting at a point on the canvas, 
            with some idea of the 'size' in mind, and draw a circle to meet the starting point. 

            This way of drawing a circle might be more natural for some design

            - In the code window below, define a point to start and the 'size', i.e. diameter of circle:

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