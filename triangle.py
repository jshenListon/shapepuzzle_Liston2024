from PIL import Image, ImageDraw
import math
import numpy as np
from canvas import *


def _re_coord(point,x=c_length/2,y=c_height/2):
    return (point[0]+x, y-point[1])

def _back_coord(point):
    return (point[0]-c_length/2, c_height/2-point[1])

def triangle_base(p1, p2, p3, fill = None, color=(0,0,0),width=1):
    draw.polygon([_re_coord(p1),_re_coord(p2),_re_coord(p3)], fill=fill, outline=color)
    #draw.line([p1, p2], fill=color, width=width, joint=None)
    #draw.line([p2, p3], fill=color, width=width, joint=None)
    #draw.line([p3, p1], fill=color, width=width, joint=None)
    #draw.point([p1,p2,p3], fill=color)
    data = {'p1':p1,
          'p2':p2,
          'p3':p3}
    return data

def triangle_LP(line, p, fill=None, color = (0,0,0)):
    p1 = _re_coord(line['start'])
    p2 = _re_coord(line['end'])
    p3 = _re_coord(p)
    draw.polygon([p1,p2,p3], fill=fill, outline=color)
    data = {'p1':_back_coord(p1),
          'p2':_back_coord(p2),
          'p3':_back_coord(p3)}
    return data

def t_center(triangle):
    reshapes = dict(map(lambda x: (x[0], _re_coord(x[1])), triangle.items()))
    p1,p2,p3=reshapes.values()
    p1 = np.asarray(p1);p2 = np.asarray(p2);p3 = np.asarray(p3)

    centroid_x = (p1[0] + p2[0] + p3[0]) / 3
    centroid_y = (p1[1] + p2[1] + p3[1]) / 3

    data = {'centroid':_back_coord((centroid_x,centroid_y))}
    return data

def rescale_c(shape, alpha = 1, redraw=True, color='black', fill='white',width=1):
    reshapes = dict(map(lambda x: (x[0], _re_coord(x[1])), shape.items()))

    p1,p2,p3=reshapes.values()
    p1 = np.asarray(p1);p2 = np.asarray(p2);p3 = np.asarray(p3)
    d1 = np.linalg.norm(p2-p3); d2 = np.linalg.norm(p1-p3); d3 = np.linalg.norm(p1-p2)
    dv = np.array([d1,d2,d3])
    pxv = np.array([p1[0],p2[0],p3[0]]); pyv = np.array([p1[1],p2[1],p3[1]])
    c_x = np.dot(dv,pxv)/np.sum(dv); c_y = np.dot(dv,pyv)/np.sum(dv)
    p1n = (p1-np.array([c_x,c_y]))*alpha + np.array([c_x,c_y])
    p2n = (p2-np.array([c_x,c_y]))*alpha + np.array([c_x,c_y])
    p3n = (p3-np.array([c_x,c_y]))*alpha + np.array([c_x,c_y])
    if redraw:
        triangle_base(_back_coord(p1),_back_coord(p2),_back_coord(p3), fill = c_color, color=c_color)
        triangle_base(_back_coord(p1n),_back_coord(p2n),_back_coord(p3n), fill = fill, color=color)
    else:
        triangle_base(_back_coord(p1n),_back_coord(p2n),_back_coord(p3n), fill = fill, color=color)
    data = {'p1':_back_coord(tuple(p1n)),
          'p2':_back_coord(tuple(p2n)),
          'p3':_back_coord(tuple(p3n))}
    return data


def rescale_p(shape, point='p1',alpha = 1, redraw=True, color='black', fill='white',width=1):
    reshapes = dict(map(lambda x: (x[0], _re_coord(x[1])), shape.items()))
    p1,p2,p3=reshapes.values()
    p1 = np.asarray(p1);p2 = np.asarray(p2); p3 = np.asarray(p3)
    p = _re_coord(shape[point])
    p1n = (p1-p)*alpha + p
    p2n = (p2-p)*alpha + p
    p3n = (p3-p)*alpha + p
    if redraw:
      triangle_base(_back_coord(p1),_back_coord(p2),_back_coord(p3), fill = c_color, color=c_color)
      triangle_base(_back_coord(p1n),_back_coord(p2n),_back_coord(p3n), fill = fill, color=color)
    else:
      triangle_base(_back_coord(p1n),_back_coord(p2n),_back_coord(p3n), fill = fill, color=color)
    data = {'p1':_back_coord(tuple(p1n)),
            'p2':_back_coord(tuple(p2n)),
            'p3':_back_coord(tuple(p3n))}
    return data

def translate_o(shape, vector=(0,0), redraw=True, color='black', fill='white',width=1):
    reshapes = dict(map(lambda x: (x[0], _re_coord(x[1])), shape.items()))
    p1,p2,p3=reshapes.values()
    p1 = np.asarray(p1);p2 = np.asarray(p2);p3 = np.asarray(p3)
    p1n = (p1[0] + vector[0], p1[1]-vector[1])
    p2n = (p2[0] + vector[0], p2[1]-vector[1])
    p3n = (p3[0] + vector[0], p3[1]-vector[1])
    if redraw:
       triangle_base(_back_coord(p1),_back_coord(p2),_back_coord(p3), fill = c_color, color=c_color)
       triangle_base(_back_coord(p1n),_back_coord(p2n),_back_coord(p3n), fill = fill, color=color)
    else:
       triangle_base(_back_coord(p1n),_back_coord(p2n),_back_coord(p3n), fill = fill, color=color)
    data = {'p1':_back_coord(tuple(p1n)),
          'p2':_back_coord(tuple(p2n)),
          'p3':_back_coord(tuple(p3n))}
    return data

def translate_p(shape, vector=(100,0), point='p1', redraw=True, color='black', fill='white',width=1):
    reshapes = dict(map(lambda x: (x[0], _re_coord(x[1])), shape.items()))
    p1,p2,p3=reshapes.values()
    p1 = np.asarray(p1);p2 = np.asarray(p2);p3 = np.asarray(p3)
    vec = np.asarray(vector)-np.asarray(shape[point])
    p1n = (p1[0] + vec[0], p1[1]-vec[1])
    p2n = (p2[0] + vec[0], p2[1]-vec[1])
    p3n = (p3[0] + vec[0], p3[1]-vec[1])
    if redraw:
       triangle_base(_back_coord(p1),_back_coord(p2),_back_coord(p3), fill = c_color, color=c_color)
       triangle_base(_back_coord(p1n),_back_coord(p2n),_back_coord(p3n), fill = fill, color=color)
    else:
       triangle_base(_back_coord(p1n),_back_coord(p2n),_back_coord(p3n), fill = fill, color=color)
    data = {'p1':_back_coord(tuple(p1n)),
          'p2':_back_coord(tuple(p2n)),
          'p3':_back_coord(tuple(p3n))}
    return data

def rotation(shape, point=(0,0),angle=90,redraw=True, color='black', fill='white',width=1):
    c, s = np.cos(np.radians(angle)), np.sin(np.radians(angle))
    R = np.array(((c, -s), (s, c)))

    reshapes = dict(map(lambda x: (x[0], _re_coord(x[1])), shape.items()))
    p1,p2,p3=reshapes.values()
    p1 = np.asarray(p1);p2 = np.asarray(p2);p3 = np.asarray(p3)
    p = np.asarray(_re_coord(point))

    p1n = np.matmul(R,p1 - p) + p
    p2n = np.matmul(R,p2 - p) + p
    p3n = np.matmul(R,p3 - p) + p

    if redraw:
       triangle_base(_back_coord(p1),_back_coord(p2),_back_coord(p3), fill = c_color, color=c_color)
       triangle_base(_back_coord(p1n),_back_coord(p2n),_back_coord(p3n), fill = fill, color=color)
    else:
       triangle_base(_back_coord(p1n),_back_coord(p2n),_back_coord(p3n), fill = fill, color=color)
    data = {'p1':_back_coord(tuple(p1n)),
          'p2':_back_coord(tuple(p2n)),
          'p3':_back_coord(tuple(p3n))}
    return data

def reflection(shape, line, redraw=True, color='black', fill='white',width=1):
    
    reshapes_l = dict(map(lambda x: (x[0], _re_coord(x[1])), line.items()))
    l1,l2 = reshapes_l.values()
    l1 = np.asarray(l1); l2=np.asarray(l2)
    dx=l2[0]-l1[0]; dy = l2[1]-l1[1]

    if dx != 0:
      slope = dy/dx
      angle = np.arctan(slope)
      c, s = np.cos(angle), np.sin(angle)
      R = np.array(((c, s), (-s, c)))
      nR = np.array(((c, -s), (s, c)))
    else:
      R = np.array(((1, 0), (0, -1)))
      nR = np.array(((-1, 0), (0, 1)))
  
    ref = np.array(((1, 0), (0, -1)))

    reshapes = dict(map(lambda x: (x[0], _re_coord(x[1])), shape.items()))
    p1,p2,p3=reshapes.values()
    p1 = np.asarray(p1);p2 = np.asarray(p2);p3 = np.asarray(p3)

    p1n = np.matmul(nR,np.matmul(ref, np.matmul(R,p1 - l1))) + l1
    p2n = np.matmul(nR,np.matmul(ref, np.matmul(R,p2 - l1))) + l1
    p3n = np.matmul(nR,np.matmul(ref, np.matmul(R,p3 - l1))) + l1

    if redraw:
       triangle_base(_back_coord(p1),_back_coord(p2),_back_coord(p3), fill = c_color, color=c_color)
       triangle_base(_back_coord(p1n),_back_coord(p2n),_back_coord(p3n), fill = fill, color=color)
    else:
       triangle_base(_back_coord(p1n),_back_coord(p2n),_back_coord(p3n), fill = fill, color=color)
    data = {'p1':_back_coord(tuple(p1n)),
          'p2':_back_coord(tuple(p2n)),
          'p3':_back_coord(tuple(p3n))}
    return data