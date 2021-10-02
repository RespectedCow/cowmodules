import sdl2
import ctypes

# Events
Poll_Event = sdl2.SDL_PollEvent
Quit_Event = sdl2.SDL_QUIT

def byref(param):
    return ctypes.byref(param)