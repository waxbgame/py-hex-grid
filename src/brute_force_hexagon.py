import simplegui
from math import cos, sin, radians

def draw(canvas):
    REGULAR_HEXAGON_ANGLE = 60
    size = 100
    pos = (300,300)
    FLAT_TOPPED = 0
    POINTY_TOPPED = 30

    arc_pos = POINTY_TOPPED
    num_points = 6
    regular_angles = 360 / num_points
    points = []
    for arc_degree in range(360/regular_angles):
        points.append(
            (cos(radians(arc_pos + arc_degree*regular_angles)),
             sin(radians(arc_pos + arc_degree*regular_angles))
            )
        )
    points = map(lambda point: (point[0]*size+pos[0],point[1]*size+pos[1]), points)
    canvas.draw_polygon(
        points,
        1,
        'Red',
        'Blue'
    )
frame = simplegui.create_frame("Home", 500, 500)
frame.set_draw_handler(draw)
frame.start()
