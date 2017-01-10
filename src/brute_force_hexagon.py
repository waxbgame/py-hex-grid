import simplegui
from math import cos, sin, radians

def draw(canvas):
    size = 100
    pos = (300,300)
    canvas.draw_polygon(
        [(cos(radians(30))*size+pos[0],sin(radians(30))*size+pos[1]),
         (cos(radians(90))*size+pos[0],sin(radians(90))*size+pos[1]),
         (cos(radians(150))*size+pos[0],sin(radians(150))*size+pos[1]),
         (cos(radians(210))*size+pos[0],sin(radians(210))*size+pos[1]),
         (cos(radians(270))*size+pos[0],sin(radians(270))*size+pos[1]),
         (cos(radians(330))*size+pos[0],sin(radians(330))*size+pos[1])],
         1,
         'Red',
         'Blue'
        )
#(cos(330)*size+pos[0],sin(330)*size+pos[1])], 
frame = simplegui.create_frame("Home", 500, 500)
frame.set_draw_handler(draw)
frame.start()
