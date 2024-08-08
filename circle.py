from PIL import Image, ImageDraw
import math
import numpy as np
from canvas import *


def _re_coord(point,x=c_length/2,y=c_height/2):
    return (point[0]+x, y-point[1])

def _back_coord(point):
    return (point[0]-c_length/2, c_height/2-point[1])

def circle_c_r(center, radiu, fill = None, color = (0,0,0), width = 1):
    ce = _re_coord(center) 
    p1 = (ce[0]- radiu/math.sqrt(2), ce[1] - radiu/math.sqrt(2))
    p2 = (ce[0]+ radiu/math.sqrt(2), ce[1] + radiu/math.sqrt(2))
    draw.pieslice([p1,p2], start=0, end=360, fill=fill, outline=color, width=width)
    data = {'center':center,
          'radiu':radiu,
          'arc':math.pi*2*radiu}
    return data

def circle_draw(point, diameter, angle=0, fill = None, color = (0,0,0), width = 1):
    po = _re_coord(point); radiu = diameter/2 
    x_e = radiu * math.cos(-angle); y_e = radiu*math.sin(-angle)
    ce = (po[0]-x_e, po[1]-y_e)
    p1 = (ce[0]- radiu/math.sqrt(2), ce[1] - radiu/math.sqrt(2))
    p2 = (ce[0]+ radiu/math.sqrt(2), ce[1] + radiu/math.sqrt(2))
    draw.pieslice([p1,p2], start=0, end=360, fill=fill, outline=color, width=width)
    data = {'center':_back_coord(ce),
          'radiu':radiu,
          'arc':math.pi*2*radiu}
    return data

