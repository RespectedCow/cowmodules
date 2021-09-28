import time
from cowmodules import GameEngine
from cowmodules import key
import threading

world = GameEngine.Window("Damn", [900, 600])

is_running = True

world.set_background(0, 0, 0)

square = GameEngine.Square(100, [100, 100], [255, 255, 255], True)

# Variables
keydebounce = 0.1
key_down = False

# Create a physic engine
physicEngine = GameEngine.PhysicEngine(window=world, gravity=True, delay=0.01)
physicEngine.add_object(square)

# Create a scene
world.create_scene("1")
world.add_to_scene(square, "1")

# Functions
def key_pressed(key_down, pressed_keys):
    if check_for(pressed_keys, "A") and not key_down:
        square.position[0] -= 1

        key_down = True
    elif not check_for(pressed_keys, "A") and key_down:
        key_down = False
    if check_for(pressed_keys, "D") and not key_down:
        square.position[0] += 1

        key_down = True
    elif not check_for(pressed_keys, "D") and key_down:
        key_down = False

def check_for(list, key):
    for match in list:
        if match == key:
            return True
    
    return False


# Main event loop
index = 0
while is_running:
    # Run physic engine
    physicEngine.run()

    # Print loop times for debugging
    index += 1
    # print("Looped " + str(index) + " times")

    # Get valuespy
    event = world.event()

    if event == "Quit":
        is_running = False
        break
    
    # Key functionality
    threading.Thread(target=key_pressed(key_down, key.get_pressed_keys())).start()

    world.refresh()
    world.wait(2)