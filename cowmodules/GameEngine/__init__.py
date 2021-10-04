import sdl2
import ctypes

# Events
Poll_Event = sdl2.SDL_PollEvent
Quit_Event = sdl2.SDL_QUIT

# Types
Direction_UP = 0
Direction_DOWN = 1
Direction_LEFT = 2
Direction_RIGHT = 3
Axis_X = 4
Axis_Y = 5
CAL_SUBTRACT = 6
CAL_ADD = 7

def byref(param):
    return ctypes.byref(param)