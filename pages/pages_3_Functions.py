import streamlit as st

with st.expander("Line Functions"):

    st.markdown("##### Line Functions")
    st.divider()
    st.markdown(
    """
        **:red[line2P(start, end, color=(0,0,0), width=1)]**
        - *Draws an line segment between the start and end points.*

        **PEREMETERS**

        - **start**: The start point of the line segment. [Data format, tuple], e.g. (100, 200)
        - **end**: The end point of the line segment. [Data format, tuple], e.g. (200, 100)
        - **color**: The color of the line segment. [Data format, tuple], e.g.(255,255,255). The RGB form of color can be extracted from 
        the color picker in the slide bar of section of the app. Default value, black, (0,0,0)
        - **width**: The width of the drawing of the line segment. [Data format, int]
    """)

    st.divider()
    st.markdown(
    """
        **:red[lineDraw(start, angle, length, color=(0,0,0), width=1)]**
        - *Draws an line segment from a starting point with predetermined angle and length.*

        **PEREMETERS**

        - **start**: The start point of the line segment. [Data format, tuple], e.g. (100, 200)
        - **angle**: The angle of direction of the line drawing towards. [Data format, int or float]. For example, starting from 
        (0,0) the origin of the canvas and draw a horizental line to the right, the angle would be 0 degree, so angle = 0;
        to draw a vertical line goes up, the angle would be 90 degree, thus angle = 90.
        - **length**: The length of the line drawing. [Data format, int or float]. Warning: the canvas is set up with dimention (700,600), 
        so if the lenght of line starting from (0,0) to the right horizentally with length 400, the canvas can only show 350 of the drawing.
        - **color**: The color of the line segment. [Data format, tuple], e.g.(255,255,255). The RGB form of color can be extracted from 
        the color picker in the slide bar of section of the app. Default value, black, (0,0,0)
        - **width**: The width of the drawing of the line segment. [Data format, int]
    """)

    st.divider()
    st.markdown(
    """
        **:red[lineFunc(x_range, alpha=1, const = 0, color=(0,0,0), width=1)]**
        - *Draws an line segment on a canvas based on its linear equation.*

        **PEREMETERS**

        - **x_range**: The range of domain (x-axis) of the linear function. [Data format, tuple], e.g. (100, 200)
        - **alpha**: The gradient (slope) of the linear function. [Data format, int or float]. 
        - **const**: The y-intecept of the linear funciton. [Data format, int or float]. 
        - **color**: The color of the line segment. [Data format, tuple], e.g.(255,255,255). The RGB form of color can be extracted from 
        the color picker in the slide bar of section of the app. Default value, black, (0,0,0)
        - **width**: The width of the drawing of the line segment. [Data format, int]
    """)

    st.divider()
    st.markdown(
    """
        **:red[p2d(start, end)]**
        - *Given two points, return linear data of them.*

        **PEREMETERS**

        - **start**: The start point of the line segment. [Data format, tuple], e.g. (100, 200)
        - **end**: The end point of the line segment. [Data format, tuple], e.g. (200, 100)

        **RETURNS**

        - **angle**: The angle of the line w.r.t. the positive x-axis;
        - **dist**: The distance between two points, i.e. the length of the line segment;
        - **x_range**: The range of the x-axis of two points;
        - **mid_point**: The midpoint of the line segment between two end points.
    """)

    st.divider()
    st.markdown(
    """
        **:red[lines_intersection(l1, l2)]**
        - *Given two non-parallel lines, return the point of intesection.*

        **PEREMETERS**

        - **l1**: The first line segment. [Data format, line objects], For example, if we created a line by other line function, such as 
        l1 = line2P(), the function line2P() will create a python dictionary with data {'start': the start point, 'end': the end point};
        This object can be passed to the lines_intersection() function.
        - **l2**: same as above

        **RETURNS**

        - the point of intersection, (x_axis, y_axis).
    """)


with st.expander("Triangle Functions"):

    st.markdown("##### Triangle Functions")
    st.markdown(
    """
        **:red[triangle_base(p1, p2, p3, fill = None, color=(0,0,0), width=1)]**
        - *Draws a triangle based on three points given.*

        **PEREMETERS**

        - **p1 / p2 / p3**: Three points as compolsory parameters of drawing. [Data format, tuple], e.g. (100, 200)
        - **fill**: The color of the shape of triangle (interior area). [Data format, tuple], e.g.(255,255,255). The RGB form of color can be extracted from 
        the color picker in the slide bar of section of the app. Default value, None, not filling any color.
        - **color**: The color of the edge of the triangle. [Data format, tuple], e.g.(255,255,255). The RGB form of color can be extracted from 
        the color picker in the slide bar of section of the app. Default value, black, (0,0,0)
        - **width**: The width of the drawing of the line segment. [Data format, int]
    """)

    st.divider()
    st.markdown(
    """
        **:red[triangle_LP(line, p, fill=None, color = (0,0,0))]**
        - *Draws a triangle based on a line-segment and a point out of the line.*

        **PEREMETERS**

        - **line**: The line segment. [Data format, line objects], For example, if we created a line by other line function, such as 
        l1 = line2P(), the function line2P() will create a python dictionary with data {'start': the start point, 'end': the end point};
        - **p**: The point out of the line-segment for the triangle. [Data format, tuple], e.g. (100, 200)
        - **fill**: The color of the shape of triangle (interior area). [Data format, tuple], e.g.(255,255,255). The RGB form of color can be extracted from 
        the color picker in the slide bar of section of the app. Default value, None, not filling any color.
        - **color**: The color of the edge of the triangle. [Data format, tuple], e.g.(255,255,255). The RGB form of color can be extracted from 
        the color picker in the slide bar of section of the app. Default value, black, (0,0,0)
        - **width**: The width of the drawing of the line segment. [Data format, int]
    """)

    st.divider()
    st.markdown(
    """
        **:red[t_center(triangle)]**
        - *Given a triangle object, returns the centers of the triangle object.*

        **PEREMETERS**

        - **triangle**: The triangle object drawing from the above two functions. [Data format, dictionary];

        **RETURNS**

        - A dictionary of centers of the target triangle.

         -- 'centroid': the [centroid](https://byjus.com/maths/centroid/) of the triangle. 
    """)

    st.divider()
    st.markdown(
    """
        **:red[rescale_c(shape, alpha = 1, redraw=True, color='black', fill='white', width=1)]**
        - *Given a triangle, rescale the triangle based on the center of the triangle.*

        **PEREMETERS**

        - **shape**: The triangle object drawing from the above two functions. [Data format, dictionary];
        - **alpha**: The scaling factor. Default = 1, i.e. same size as the original shape. When alpha > 1, it means enlarge the triangle; 
        when 0 < alpha < 1, it means shrink the triangle.
        - **redraw**: The boolean parameter to determine whether to eliminate the original triangle. Default = True, i.e. only keep the newly drawn triangle;
        - **fill**: The color of the shape of triangle (interior area). [Data format, tuple], e.g.(255,255,255). The RGB form of color can be extracted from 
        the color picker in the slide bar of section of the app. Default value, None, not filling any color.
        - **color**: The color of the edge of the triangle. [Data format, tuple], e.g.(255,255,255). The RGB form of color can be extracted from 
        the color picker in the slide bar of section of the app. Default value, black, (0,0,0)
        - **width**: The width of the drawing of the line segment. [Data format, int]
    """)

    st.divider()
    st.markdown(
    """
        **:red[rescale_p(shape, point='p1',alpha = 1, redraw=True, color='black', fill='white', width=1)]**
        - *Given a triangle, rescale the triangle based on a vertex on the triangle.*

        **PEREMETERS**

        - **shape**: The triangle object drawing from the above two functions. [Data format, dictionary];
        - **point**: The name of the vertex of the triangle object. ('p1', 'p2', or 'p3'). [Data format, string];
        - **alpha**: The scaling factor. Default = 1, i.e. same size as the original shape. When alpha > 1, it means enlarge the triangle; 
        when 0 < alpha < 1, it means shrink the triangle.
        - **redraw**: The boolean parameter to determine whether to eliminate the original triangle. Default = True, i.e. only keep the newly drawn triangle;
        - **fill**: The color of the shape of triangle (interior area). [Data format, tuple], e.g.(255,255,255). The RGB form of color can be extracted from 
        the color picker in the slide bar of section of the app. Default value, None, not filling any color.
        - **color**: The color of the edge of the triangle. [Data format, tuple], e.g.(255,255,255). The RGB form of color can be extracted from 
        the color picker in the slide bar of section of the app. Default value, black, (0,0,0)
        - **width**: The width of the drawing of the line segment. [Data format, int]
    """)

    st.divider()
    st.markdown(
    """
        **:red[translate_o(shape, vector=(0,0), redraw=True, color='black', fill=None, width=1)]**
        - *Given a triangle, translate the triangle based on a vector from the oringin.*

        **PEREMETERS**

        - **shape**: The triangle object drawing from the above two functions. [Data format, dictionary];
        - **vector**: The vector of translation. Default value = (0,0), i.e. no translation;
        - **redraw**: The boolean parameter to determine whether to eliminate the original triangle. 
        Default = True, i.e. only keep the newly drawn triangle;
        - **fill**: The color of the shape of triangle (interior area). [Data format, tuple], e.g.(255,255,255). The RGB form of color can be extracted from 
        the color picker in the slide bar of section of the app. Default value, None, not filling any color.
        - **color**: The color of the edge of the triangle. [Data format, tuple], e.g.(255,255,255). The RGB form of color can be extracted from 
        the color picker in the slide bar of section of the app. Default value, black, (0,0,0)
        - **width**: The width of the drawing of the line segment. [Data format, int]
    """)

    st.divider()
    st.markdown(
    """
        **:red[translate_p(shape, vector=(100,0), point='p1', redraw=True, color='black', fill=None, width=1)]**
        - *Given a triangle, translate the triangle based on a vector from a vertex of a triangle.*

        **PEREMETERS**

        - **shape**: The triangle object drawing from the above two functions. [Data format, dictionary];
        - **vector**: The vector of translation. Default value = (100,0);
        - **point**: The name of the vertex of the triangle object. ('p1', 'p2', or 'p3'). [Data format, string]; 
        - **redraw**: The boolean parameter to determine whether to eliminate the original triangle. 
        Default = True, i.e. only keep the newly drawn triangle;
        - **fill**: The color of the shape of triangle (interior area). [Data format, tuple], e.g.(255,255,255). The RGB form of color can be extracted from 
        the color picker in the slide bar of section of the app. Default value, None, not filling any color.
        - **color**: The color of the edge of the triangle. [Data format, tuple], e.g.(255,255,255). The RGB form of color can be extracted from 
        the color picker in the slide bar of section of the app. Default value, black, (0,0,0)
        - **width**: The width of the drawing of the line segment. [Data format, int]
    """)

    st.divider()
    st.markdown(
    """
        **:red[rotation(shape, point=(0,0), angle=90, redraw=True, color='black', fill='white', width=1)]**
        - *Given a triangle, rotate the triangle based on a point on Canvas.*

        **PEREMETERS**

        - **shape**: The triangle object drawing from the above two functions. [Data format, dictionary];
        - **point**: The name of the vertex of the triangle object. ('p1', 'p2', or 'p3'). [Data format, string];
        - **angle**: The angle of rotation, clockwise, default value = 90, i.e. 90 degrees; 
        - **redraw**: The boolean parameter to determine whether to eliminate the original triangle. 
        Default = True, i.e. only keep the newly drawn triangle;
        - **fill**: The color of the shape of triangle (interior area). [Data format, tuple], e.g.(255,255,255). The RGB form of color can be extracted from 
        the color picker in the slide bar of section of the app. Default value, None, not filling any color.
        - **color**: The color of the edge of the triangle. [Data format, tuple], e.g.(255,255,255). The RGB form of color can be extracted from 
        the color picker in the slide bar of section of the app. Default value, black, (0,0,0)
        - **width**: The width of the drawing of the line segment. [Data format, int]
    """)

    st.divider()
    st.markdown(
    """
        **:red[reflection(shape, line, redraw=True, color='black', fill='white', width=1)]**
        - *Given a triangle, reflect the triangle based on a line already existed on Canvas.*

        **PEREMETERS**

        - **shape**: The triangle object drawing from the above two functions. [Data format, dictionary];
        - **line**: The variable name of the line defined. [Data format, dictionary];
        - **redraw**: The boolean parameter to determine whether to eliminate the original triangle. 
        Default = True, i.e. only keep the newly drawn triangle;
        - **fill**: The color of the shape of triangle (interior area). [Data format, tuple], e.g.(255,255,255). The RGB form of color can be extracted from 
        the color picker in the slide bar of section of the app. Default value, None, not filling any color.
        - **color**: The color of the edge of the triangle. [Data format, tuple], e.g.(255,255,255). The RGB form of color can be extracted from 
        the color picker in the slide bar of section of the app. Default value, black, (0,0,0)
        - **width**: The width of the drawing of the line segment. [Data format, int]
    """)

    