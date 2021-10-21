# Import libraries
import sdl2
from cowmodules.GameEngine import engine, Vector2

class Square:
    def __init__(self, size, position, color, gravity=False, gravitySpeed=1, mass=5):
        '''
        Create a square with the given values.
        '''
        
        # Filters
        assert type(position) == Vector2, "Position value must be a Vector2"
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
        renderer.fill([self.position.x, self.position.y, self.size, self.size], sdl2.ext.Color(self.color[0], self.color[1], self.color[2]))

class Rectangle:
    def __init__(self, size, position, color, gravity=False, gravitySpeed=1, mass=5):
        ''''
        Create a rectangle object with the given values.
        '''
        
        # Filters
        assert type(position) == Vector2, "Position value must be a Vector2"
        assert type(size) == list, "Size value must be a list containing the x and y values"

        # Assign values
        self.size = size
        self.position = position
        self.color = color
        self.gravity = gravity
        self.gravitySpeed = gravitySpeed
        self.mass = mass
        self.vel_x = 0
        self.vel_y = 0

    def draw(self, window):
        '''
        Draws the object on the screen.
        
        Note: You have to run renderer.present() for the effects to be visible
        '''
        
        renderer = window.renderer

        # Draw shape
        renderer.fill([self.position.x, self.position.y, self.size[0], self.size[1]], sdl2.ext.Color(self.color[0], self.color[1], self.color[2]))
        
        
class Group:
    
    def __init__(self, position):
        '''
        Group together objects and move them with the offset from the position
        '''
        
        # Filter
        assert position == Vector2, "Position value type is not a Vector2"
        
        self.objects = []
        self.position = position
        
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
    
    def get_offset(self, object):
        # Check if object.position is valid
        assert type(object.position) == Vector2, "object.position type is not a Vector2"
        
        return self.position.subtract(object.position)
    
    
class Sprite:
    
    def __init__(self, window, path, position):
        # Filter out passed variables
        assert type(window) == engine.Window, "Window value is not a window."
        assert type(position) == Vector2, "Position value is not a Vector2"
        
        # Create sprite
        self.sprite = window.factory.from_image(path)
        
        # Position sprite
        self.sprite.position = (position.x, position.y)
        
    def draw(self, window):
        window.spriterenderer.render(self.sprite)
        

class Circle:
    def __init__(self, position, radius):
        self.radius = radius
        self.position = position

    def draw(self, window): 
        pass