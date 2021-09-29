# Importing libraries
import sdl2
import sdl2.ext
from cowmodules import commons
from cowmodules.GameEngine.objects import Square, Circle
import threading

class PhysicService:
    
    def __init__(self, window,gravity=False):
        self.gravity = gravity
        self.objects = []
        self.window = window

    def add_object(self, object):
        self.objects.append(object)

    def _apply_gravity(self, object):
        if self.gravity and object.gravity and object.position[1] < self.window.height:
            gravSpeed = object.gravitySpeed or 1
            object.position[1] += 1

    def run(self):
        # Valid objects
        VALID = [
            Square
        ]

        for object in self.objects:
            if commons.check_in_array_type(self.objects, Square):
                threading.Thread(target=self._apply_gravity(object))