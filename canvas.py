from PIL import Image, ImageDraw

## Canvas Config
c_length = 700
c_height = 600
c_mode = 'RGB'
c_color = (250,250,250)
c_outline = (0,0,0)

img = Image.new(c_mode, (c_length, c_height), color = c_color)
img_t = Image.new(c_mode, (c_length, c_height), color = c_color)

draw = ImageDraw.Draw(img)
