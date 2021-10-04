# Importing libraries
from typing import List
import cowmodules
from cowmodules import GameEngine
from cowmodules.GameEngine.key import find_in_list
import sdl2
import sdl2.ext
from cowmodules import common
from cowmodules.GameEngine.objects import Square, Circle
import threading
import time
import math

class PhysicService:
    
    def __init__(self, window,gravity=False, delay=0.001):
        self.gravity = gravity
        self.objects = []
        self.window = window
        self.delay = delay

    def add_object(self, object):
        self.objects.append(object)

    def check_for_collision(self, object1, object2): # Collision detection
        x_aligned = False
        y_aligned = False

        for x1 in range(object1.position[0] + 1, object1.position[0] + get_dimension(object1.size, "x") + 1):
            for x2 in range(object2.position[0] + 1, object2.position[0] + get_dimension(object2.size, "x") + 1):
                if x1 == x2:
                    x_aligned = True
                    break

        for y1 in range(object1.position[1] + 1, object1.position[1] + get_dimension(object1.size, "y") + 1):
            for y2 in range(object2.position[1] + 1, object2.position[1] + get_dimension(object2.size, "y") + 1):
                if y1 == y2:
                    y_aligned = True
                    break

        if x_aligned == True and y_aligned == True:
            return True
        else:
            return False

    def _apply_gravity(self, object):
        if self.gravity and object.gravity and object.position[1] < self.window.height:
            gravSpeed = object.gravitySpeed or 1
            object.position[1] += gravSpeed
            time.sleep(self.delay)

    def apply_velocity(self, object, axis=GameEngine.Axis_X, calculation=GameEngine.CAL_ADD, decay=1):
        '''
        Applies a velocity effect to an object with vel_x and vel_y values
        '''
        if object.vel_x > 0:
            f_x = object.vel_x

            # Apply effects
            if calculation == GameEngine.CAL_ADD:
                object.position[0] += f_x
            elif calculation == GameEngine.CAL_SUBTRACT:
                object.position[0] -= f_x

            # Decrease velocity
            object.vel_x -= object.mass

        if object.vel_y > 0:
            f_y = object.vel_y

            # Apply effects
            if calculation == GameEngine.CAL_ADD:
                object.position[1] += f_y
            elif calculation == GameEngine.CAL_SUBTRACT:
                object.position[1] -= f_y

            # Decrease velocity
            object.vel_y -= object.mass

    def run(self):
        # Valid objects
        VALID = [
            Square,
            Circle
        ]

        for object in self.objects:
            if common.check_in_array_type(self.objects, Square):
                threading.Thread(target=self._apply_gravity(object))


def get_dimension(objectSize, xy):
    if type(objectSize) == list:
        if xy == "x":
            return objectSize[0]
        elif xy == "y":
            return objectSize[1]

    elif type(objectSize) == int:
        return objectSize