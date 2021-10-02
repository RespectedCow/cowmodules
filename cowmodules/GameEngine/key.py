# Imports
import sdl2
import ctypes
import threading

# Main
def get_pressed_keys():
        key_state = sdl2.SDL_GetKeyboardState(None)

        KEY_ARRAY = [
            ["A", sdl2.SDL_SCANCODE_A],
            ["B", sdl2.SDL_SCANCODE_B],
            ["C", sdl2.SDL_SCANCODE_C],
            ["D", sdl2.SDL_SCANCODE_D],
            ["E", sdl2.SDL_SCANCODE_E],
            ["F", sdl2.SDL_SCANCODE_F],
            ["G", sdl2.SDL_SCANCODE_G],
            ["H", sdl2.SDL_SCANCODE_H],
            ["I", sdl2.SDL_SCANCODE_I],
            ["J", sdl2.SDL_SCANCODE_J],
            ["K", sdl2.SDL_SCANCODE_K],
            ["L", sdl2.SDL_SCANCODE_L],
            ["M", sdl2.SDL_SCANCODE_M],
            ["N", sdl2.SDL_SCANCODE_N],
            ["O", sdl2.SDL_SCANCODE_O],
            ["P", sdl2.SDL_SCANCODE_P],
            ["Q", sdl2.SDL_SCANCODE_Q],
            ["R", sdl2.SDL_SCANCODE_R],
            ["S", sdl2.SDL_SCANCODE_S],
            ["T", sdl2.SDL_SCANCODE_T],
            ["U", sdl2.SDL_SCANCODE_U],
            ["V", sdl2.SDL_SCANCODE_V],
            ["W", sdl2.SDL_SCANCODE_W],
            ["X", sdl2.SDL_SCANCODE_X],
            ["Y", sdl2.SDL_SCANCODE_Y],
            ["Z", sdl2.SDL_SCANCODE_Z],
            ["0", sdl2.SDL_SCANCODE_0],
            ["1", sdl2.SDL_SCANCODE_1],
            ["2", sdl2.SDL_SCANCODE_2],
            ["3", sdl2.SDL_SCANCODE_3],
            ["4", sdl2.SDL_SCANCODE_4],
            ["5", sdl2.SDL_SCANCODE_5],
            ["6", sdl2.SDL_SCANCODE_6],
            ["7", sdl2.SDL_SCANCODE_7],
            ["8", sdl2.SDL_SCANCODE_8],
            ["9", sdl2.SDL_SCANCODE_9]
        ]

        return_array = []

        for arr in KEY_ARRAY:
            if key_state[arr[1]]:
                return_array.append(arr[0])

        return return_array

values = [
    ["A", False],
    ["B", False],
    ["C", False],
    ["D", False],
    ["E", False],
    ["F", False],
    ["G", False],
    ["H", False],
    ["I", False],
    ["J", False],
    ["K", False],
    ["L", False],
    ["M", False],
    ["N", False],
    ["O", False],
    ["P", False],
    ["Q", False],
    ["R", False],
    ["S", False],
    ["T", False],
    ["U", False],
    ["V", False],
    ["W", False],
    ["X", False],
    ["Y", False],
    ["Z", False],
    ["0", False],
    ["1", False],
    ["2", False],
    ["3", False],
    ["4", False],
    ["5", False],
    ["6", False],
    ["7", False],
    ["8", False],
    ["9", False]
]

def is_pressed(key):
    if check_for(get_pressed_keys(), key):
        return True

    return False

def __reset__(key):
    if is_pressed(key) and not check_for(values, [key, False]):
        value = find_in_list(values, [key, True])
        value[1] = False

def is_down(key):
    whattoreturn = False

    if is_pressed(key) and check_for(values, [key, False]):
        value = find_in_list(values, [key, False])
        value[1] = True
        whattoreturn = True
    
    __reset__(key)

    return whattoreturn

def check_for(list, key):
    for match in list:
        if match == key:
            return True
    
    return False

def find_in_list(list, object):
    for value in list:
        if value == object:
            return value

    return None