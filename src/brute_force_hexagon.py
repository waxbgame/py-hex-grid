import simplegui
from math import cos, sin, radians

def draw(canvas):
    size = 100
    pos = (300,300)
    FLAT_TOPPED = 0
    POINTY_TOPPED = 30
    
    arc_pos = POINTY_TOPPED
    canvas.draw_polygon(
        [(cos(radians(arc_pos))*size+pos[0],sin(radians(arc_pos))*size+pos[1]),
         (cos(radians(arc_pos + 60))*size+pos[0],sin(radians(arc_pos + 60))*size+pos[1]),
         (cos(radians(arc_pos + 2*60))*size+pos[0],sin(radians(arc_pos + 2*60))*size+pos[1]),
         (cos(radians(arc_pos + 3*60))*size+pos[0],sin(radians(arc_pos + 3*60))*size+pos[1]),
         (cos(radians(arc_pos + 4*60))*size+pos[0],sin(radians(arc_pos + 4*60))*size+pos[1]),
         (cos(radians(arc_pos + 5*60))*size+pos[0],sin(radians(arc_pos + 5*60))*size+pos[1])],
         1,
         'Red',
         'Blue'
        )
#(cos(330)*size+pos[0],sin(330)*size+pos[1])], 
frame = simplegui.create_frame("Home", 500, 500)
frame.set_draw_handler(draw)
frame.start()
