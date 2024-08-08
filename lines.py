from PIL import Image, ImageDraw
import numpy as np
import math
import shapely
from shapely.geometry import LineString
from canvas import *


def _re_coord(point):
    return (point[0]+c_length/2, c_height/2-point[1])

def _back_coord(point):
    return (point[0]-c_length/2, c_height/2-point[1])

def line_end(start, angle, length):
    x, y = start
    endy = y + length * math.sin(math.radians(-angle)) 
    endx = x + length * math.cos(math.radians(-angle))
    return (endx, endy)

def lines_intersection(l1, l2):
    line1 = LineString([l1['start'], l1['end']])
    line2 = LineString([l2['start'], l2['end']])
    int_pt = line1.intersection(line2)
    return (int_pt.x, int_pt.y)

def p2d (start, end):
    angle = np.rad2deg(np.arctan2(end[1] - start[1], end[0] - start[0]))
    dist = np.linalg.norm(np.array(start) - np.array(end))
    x_range = (start[0], end[0])
    mid_point = ((start[0]+end[0])/2, (start[1]+end[1])/2)
    data = {
        'angle':angle,
        'dist':dist,
        'x_range':x_range,
        'mid_point':mid_point
    }
    return data

def line2P(start,end,color=(0,0,0),width=1):
    draw.line([_re_coord(start), _re_coord(end)], fill=color, width=width, joint=None)
    data = {'start':start,
          'end':end}
    return data

def lineDraw(start, angle, length, color=(0,0,0), width=1):
    end = line_end(_re_coord(start), angle, length)
    draw.line([_re_coord(start), end], fill=color, width=width, joint=None)
    data = {'start':start,
          'end':_back_coord(end)}
    return data

def lineFunc(x_range, alpha=1, const = 0, color=(0,0,0), width=1): 
    start_x = x_range[0]-c_length/2
    end_x =x_range[-1]-c_length/2 #the last one of range
    start_y = c_height - (alpha*start_x + const)
    end_y = c_height - (alpha*end_x + const)
    draw.line([(start_x,start_y), (end_x, end_y)], fill=color, width=width, joint=None)
    data = {'start':(start_x,start_y),
          'end':(end_x,end_y)}
    return data