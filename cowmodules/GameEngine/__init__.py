import sdl2
import sdl2.ext
import os
import ctypes

# Events
Poll_Event = sdl2.SDL_PollEvent
Quit_Event = sdl2.SDL_QUIT

# Simple types
Direction_UP = 0
Direction_DOWN = 1
Direction_LEFT = 2
Direction_RIGHT = 3
Axis_X = 4
Axis_Y = 5
CAL_SUBTRACT = 6
CAL_ADD = 7

# Types
class Vector2:
    
    def __init__(self, x, y):
        # Make sure x and y values are ints
        assert type(x) == int, "X value is not an int!"
        assert type(y) == int, "Y value is not an int!"
        
        self.x = x
        self.y = y
        
    def add(self, Vector2):
        x = Vector2.x
        y = Vector2.y
        
        self.x += x
        self.y += y
        
    def subtract(self, Vector2):
        x = Vector2.x
        y = Vector2.y
        
        self.x -= x
        self.y -= y

def byref(param):
    return ctypes.byref(param)