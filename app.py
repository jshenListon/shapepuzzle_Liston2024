# app.py

import sys
import time
from io import StringIO
import streamlit as st
from PIL import Image, ImageDraw, ImageColor
from canvas import *
from streamlit_ace import st_ace
import extra_streamlit_components as stx
from streamlit_image_select import image_select
import numpy as np
# from sqlite3 import Connection
import datetime
from lines import *
from triangle import *


def get_manager():
    return stx.CookieManager()

### Manage Cookies and ajs_state ####

#time.sleep(3)
#cookie_manager = get_manager()
#ajs_id = cookie_manager.get_all()["ajs_anonymous_id"]
date_reg = datetime.date.today().strftime("%d/%m/%Y")
st.session_state['timestamp'] = datetime.datetime.now().strftime("%d/%m/%Y %H:%M:%S")

#st.session_state['conn'] = get_connection("data_drawer.db")
#user_checked = check_value_id_user(st.session_state.conn, ajs_id).values[0][0] > 0
#if not user_checked:
#    user_id = str(st.text_input("Welcome! please enter your username here:)"))
#    values = (ajs_id, user_id, date_reg)
#    insert_value_ajs_states (st.session_state.conn, values)

## Sidebar for color picker
with st.sidebar:
    color = st.color_picker('color picker', '#00f900', key='l_c')
    st.write(ImageColor.getrgb(color))

st.header("Shape Puzzles")
st.write("##")
st.divider()

st.markdown("###### Write your code here")
## Code input
code = st_ace(
    language="python",
    theme="tomorrow_night_bright",
    keybinding="vscode",
    font_size=14,
    tab_size=4,
    show_gutter=True,
    min_lines=10,
    key="ace",
)
st.divider()

target = image_select(
    label="Select a target image",
    images=[
        'image/TrianglePolygon.png',
        'image/TriangleHole.png',
        "image/TriangleCrash.png",
        'image/archillect.png',
        'image/TriangleFox.png'
    ],
    captions=["Iterative Polygon", "Infinite traps", "One Cut", "Archillect", "Red Fox"],
    use_container_width = False
)

o1, o2 = st.columns(2)
if code:
    ImageDraw.Draw(img).rectangle([(0, 0), (c_length,c_height)], fill = c_color, outline = c_outline, width=2)
    redirected_output = sys.stdout = StringIO()
    try:
        exec(code)
        result = str(redirected_output.getvalue())
        st.code(result)
    except Exception as e:
        st.code(str(e))

st.write("##")
st.divider()
with o1:
    st.markdown("##### Target Shape:")
    target = Image.open(target)
    t2 = target.resize((c_length,c_height))
    ImageDraw.Draw(img_t).rectangle([(0, 0), 
                                    (c_length,c_height)],
                                    fill = c_color, 
                                    outline = c_outline, 
                                    width=2)
    img_t.paste(t2)
    st.image(img_t)
    st.session_state['imt'] = np.array(img_t)
with o2:
    st.markdown("##### Output Shape")    
    st.image(img, caption='')
    st.session_state['imo'] = np.array(img)


