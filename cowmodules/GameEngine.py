# Importing libraries
import sdl2
import sdl2.ext
import ctypes
import  math

sdl2.SDL_Init(sdl2.SDL_INIT_VIDEO)
class World(sdl2.ext.Window):
    def __init__(self, world_name, dimensions, icon=None):
        # Filters
        assert type(world_name) == str, "World name parameter must be a string!"
        assert type(dimensions) == list, "Dimensions parameter must be a list!"
        assert len(dimensions) == 2, "Dimensions must only have 2 int values."
        if icon != None:
            assert type(icon) == str, "Icon parameter must be a path"

            # Add icon
            self.icon = sdl2.ext.load_image(icon)
            sdl2.SDL_SetWindowIcon(self, self.icon)

        for i in dimensions:
            assert type(i) == int, "Dimensions must be ints!"

        # Creating the window
        self.name = world_name
        self.width = dimensions[0]
        self.height = dimensions[1]
        super().__init__(self.name, size=(dimensions[0], dimensions[1]))

        # Declare some vars
        self.renderer = sdl2.ext.Renderer(self, logical_size=(0, 0))

        # Create a sprite factory that allows us to create visible 2D elements
        # easily.
        self.factory = sdl2.ext.SpriteFactory(
            sdl2.ext.TEXTURE, renderer=self.renderer)

        # Creates a simple rendering system for the Window. The
        # SpriteRenderSystem can draw Sprite objects on the window.
        self.spriterenderer = self.factory.create_sprite_render_system(
            self.window)

        self.show()

    def event(self):
        event = sdl2.SDL_Event()
        
        if sdl2.SDL_PollEvent(ctypes.byref(event)) != 0:
            if event.type == sdl2.SDL_QUIT:
                return "Quit"

        return 0

    def __start_loop(self):
        is_running = True
        event = sdl2.SDL_Event()
        while is_running:
            while sdl2.SDL_PollEvent(ctypes.byref(event)) != 0:
                if event.type == sdl2.SDL_QUIT:
                    is_running = False
                    break

        sdl2.SDL_Quit()

    def hide(self):
        self.hide()

    def close(self):
        self.close()

    def process(self):
        self.process()

    def set_background(self, r, g, b):
        '''
        Loop through height and width value. Divided by 10 because of weird math.
        '''
        index = 0

        for y in range(int(self.height / (self.height / 10))):
            for x in range(int(self.width / (self.width / 10))):
                self.renderer.draw_point([x,y], sdl2.ext.Color(r, g, b))
                self.renderer.present()

class Events:
    def __init__(self, type):
        self.type = type

    def type(self):
        return type(self.type)

# Custom events
class EventTypes:
    class QuitEvent:
        def __init__(self):
            pass
    
    class NormalEvent:
        def __init__(self):
            pass

# Objects
class Square:
    def __init__(self, size, position, color):
        # Filters
        assert len(position) == 2, "Position value must have 2 int values"
        assert type(size) == int, "Size value must be int"

        # Assign values
        self.size = size
        self.position = position
        self.color = color
    
    def draw(self, world):
        # Get world renderer
        renderer = world.renderer

        # Draw shape
        renderer.fill((self.position[0], self.position[1], self.size, self.size), color=sdl2.ext.Color(255, 255, 255))

        # Show changes
        renderer.present()

class Circle:
    def __init__(self, position, radius):
        self.radius = radius
        self.position = position

    def draw(self, renderer): 
        pass

def run(world):
    assert type(world) == World, "Parameter is not a world"

    processor = sdl2.ext.TestEventProcessor()
    processor.run(world)

def quit():
    sdl2.SDL_Quit()