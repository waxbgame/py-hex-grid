import simplegui
from math import cos, sin, radians

class RegularShapeMaker:
    
    class RegularShape:
        
        def __init__(self, builder):
            self.point_count = builder.point_count
            self.pixel_radius = builder.pixel_radius
            self.pos = builder.pos
            self.arc_pos_initial = builder.arc_pos_initial
        
    def with_num_points(self, point_count):
        self.point_count = point_count
        return self
    
    def with_pixel_radius(self, pixel_radius):
        self.pixel_radius = pixel_radius
        return self
    
    def with_initial_position_xy(self, pos):
        self.pos = pos
        return self
    
    def with_initial_arc_pos_degrees(self, degrees):
        self.arc_pos_initial = degrees
        return self
    
    def build(self):
        return self.RegularShape(self)

hexagon = RegularShapeMaker() \
    .with_num_points(6) \
    .with_pixel_radius(100) \
    .with_initial_position_xy((200,200)) \
    .with_initial_arc_pos_degrees(0) \
    .build()

def coords_for_shape(shape):
    pos = shape.pos
    size = shape.pixel_radius
    arc_pos = shape.arc_pos_initial
    num_points = shape.point_count
    regular_angles = 360 / num_points
    points = []
    for arc_degree in range(360/regular_angles):
        points.append(
            (cos(radians(arc_pos + arc_degree*regular_angles)),
             sin(radians(arc_pos + arc_degree*regular_angles))
            )
        )
    points = map(lambda point: (point[0]*size+pos[0],point[1]*size+pos[1]), points)
    return points

points = coords_for_shape(hexagon)

def draw(canvas):
        canvas.draw_polygon(
        points,
        5,
        'Orange',
        'Blue'
    )

frame = simplegui.create_frame("Home", 500, 500)
frame.set_draw_handler(draw)
frame.start()
