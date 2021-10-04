from cowmodules import GameEngine
from cowmodules.GameEngine import engine, objects, services
from cowmodules.GameEngine import key
import threading
import time

world = engine.Window("Damn", [900, 600])

is_running = True

world.set_background(255, 255, 255)

square = objects.Square(100, [100, 100], [255, 0, 0], True, mass=10)
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
world.draw("1")

# Functions
def key_down():
    if key.is_down("A"):
        square.position[0] -= 5
    if key.is_down("D"):
        square.position[0] += 5
    if key.is_down("W") and physicEngine.check_for_collision(square, platform):
        threading.Thread(physicEngine.apply_velocity(square, "y", 30, "subtract"))

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
    while GameEngine.Poll_Event(GameEngine.byref(event)) != 0:
        if event.type == GameEngine.Quit_Event:
            is_running = False
            break

    # Detect collisions
    if physicEngine.check_for_collision(square, platform):
        square.gravity = False
    else:
       square.gravity = True
    
    # Input
    threading.Thread(target=key_down()).start()

    world.refresh()
    world.wait(10)