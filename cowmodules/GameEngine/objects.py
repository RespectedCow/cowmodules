# Import libraries
import sdl2

class Square:
    def __init__(self, size, position, color, gravity=False, gravitySpeed=1, mass=5):
        # Filters
        assert len(position) == 2, "Position value must have 2 int values"
        assert type(size) == int, "Size value must be int"

        # Assign values
        self.size = size
        self.position = position
        self.color = color
        self.gravity = gravity
        self.gravitySpeed = gravitySpeed
        self.mass = mass
        self.vel_y = 0
        self.vel_x = 0

    def draw(self, window):
        renderer = window.renderer

        # Draw shape
        renderer.fill([self.position[0], self.position[1], self.size, self.size], sdl2.ext.Color(self.color[0], self.color[1], self.color[2]))

class Rectangle:
    def __init__(self, size, position, color, gravity=False, gravitySpeed=1):
        # Filters
        assert len(position) == 2, "Position value must have 2 int values"
        assert type(size) == list, "Size value must be a list containing the x and y values"

        # Assign values
        self.size = size
        self.position = position
        self.color = color
        self.gravity = gravity
        self.gravitySpeed = gravitySpeed

    def draw(self, window):
        renderer = window.renderer

        # Draw shape
        renderer.fill([self.position[0], self.position[1], self.size[0], self.size[1]], sdl2.ext.Color(self.color[0], self.color[1], self.color[2]))
        
        
class Group:
    
    def __init__(self):
        self.objects = []
        
    def add_object(self, object):
        self.objects.append(object)
        
    def remove_object(self, object):
        for object2 in self.objects:
            if object == object2:
                self.objects.remove(object2)
                return 0
            
        return 1
    
    def get_objects(self):
        return self.objects
        

class Circle:
    def __init__(self, position, radius):
        self.radius = radius
        self.position = position

    def draw(self, window): 
        pass