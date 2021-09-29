import cowmodules
from cowmodules import GameEngine
from cowmodules.GameEngine import engine, objects, services
from cowmodules.GameEngine import key
import threading
import time
import sdl2
import ctypes

world = engine.Window("Damn", [900, 600])

is_running = True

world.set_background(255, 255, 255)

square = objects.Square(100, [100, 100], [255, 0, 0], True)
platform = objects.Rectangle([900, 5], [0, 500], [0, 0, 0])

# Variables
keydebounce = 0.1
key_down = False

# Create a physic engine
physicEngine = services.PhysicService(window=world, gravity=True) # Effects are applied every frame
physicEngine.add_object(square)
square.gravitySpeed = 5

# Create a scene
world.create_scene("1")
world.add_to_scene(square, "1")
world.add_to_scene(platform, "1")

# Functions
def key_pressed(key_down, pressed_keys):
    if check_for(pressed_keys, "A") and not key_down:
        square.position[0] -= 5
        time.sleep(0.01)
        key_down = True
    elif not check_for(pressed_keys, "A") and key_down:
        key_down = False
    if check_for(pressed_keys, "D") and not key_down:
        square.position[0] += 5
        time.sleep(0.01)
        key_down = True
    elif not check_for(pressed_keys, "D") and key_down:
        key_down = False
    if check_for(pressed_keys, "W") and not key_down and physicEngine.check_for_collision(square, platform):
        square.position[1] -= 50
        time.sleep(0.01)
        key_down = True
    elif not check_for(pressed_keys, "W") and key_down:
        key_down = False

def check_for(list, key):
    for match in list:
        if match == key:
            return True
    
    return False

# Main event loop
index = 0
event = world.event()
while is_running:
    # Run physic engine
    physicEngine.run()

    # Print loop times for debugging
    index += 1
    # print("Looped " + str(index) + " times")

    # Closing the window
    while GameEngine.Poll_Event(ctypes.byref(event)) != 0:
        if event.type == GameEngine.Quit_Event:
            is_running = False
            break

    # Detect collisions
    if physicEngine.check_for_collision(square, platform):
        square.gravity = False
    else:
       square.gravity = True
    
    # Key functionality
    threading.Thread(target=key_pressed(key_down, key.get_pressed_keys())).start()

    world.refresh()
    world.wait(10)