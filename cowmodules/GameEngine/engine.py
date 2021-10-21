# Importing libraries
import sdl2
import sdl2.ext
import ctypes
from cowmodules.cowtime import Clock
from cowmodules import common
from cowmodules.GameEngine import Vector2
    
class Window(sdl2.ext.Window):
    def __init__(self, world_name, dimensions, icon=None, background=[0,0,0]):
        '''
        Creates a window with the given values.
        '''
        
        # Filters
        assert type(world_name) == str, "World name parameter must be a string!"
        assert type(dimensions) == Vector2, "Dimensions value must be a Vector2"
        if icon != None:
            assert type(icon) == str, "Icon parameter must be a path"

            # Add icon
            self.icon = sdl2.ext.load_image(icon)
            sdl2.SDL_SetWindowIcon(self, self.icon)

        # Creating the window
        self.name = world_name
        self.width = dimensions.x
        self.height = dimensions.y
        self.background = sdl2.ext.Color(background[0], background[1], background[2])
        super().__init__(self.name, size=(dimensions.x, dimensions.y))

        # Declare some vars
        self.renderer = sdl2.ext.Renderer(self, logical_size=(0, 0))
        self.scenes = [] # Both self.scene and self.scene_indictor have to be updated at the same rate
        self.scene_indictor = []
        self.activated_scenes = []

        # Create pythonic clock
        self.clock = Clock()

        # Create a sprite factory that allows us to create visible 2D elements
        # easily.
        self.factory = sdl2.ext.SpriteFactory(
            sdl2.ext.TEXTURE, renderer=self.renderer)

        # Creates a simple rendering system for the Window. The
        # SpriteRenderSystem can draw Sprite objects on the window.
        self.spriterenderer = self.factory.create_sprite_render_system(
            self.window)

        self.show()

    def refresh(self):
        '''
        Clears the window and redraws everything.
        '''
        
        # Clear window
        self.renderer.clear(sdl2.ext.Color(self.background[0], self.background[1], self.background[2]))

        # Get the list of everything to redraw
        for scene in self.activated_scenes:
            for object in scene:
                object.draw(self)

        self.renderer.present()

    def get_ticks(self):
        return sdl2.SDL_GetTicks()

    def wait(self, time):
        sdl2.SDL_Delay(time)

    def add_to_scene(self, object, scene_name):
        # Check if scene exist
        scene = self.get_scene(scene_name)

        # Insert object into scene
        scene.append(object)

    def draw(self, scene_name):
        '''
        Draws a scene(Appends it to self.activated_scenes)
        
        Only takes effect after refreshing.
        '''
        
        # Find scene and check if exist
        scene = self.get_scene(scene_name)

        assert scene != None, "Scene does not exist!"

        # Add scene to activated_scenes
        self.activated_scenes.append(scene)

    def get_mouse_pos(self):
        """Get the mouse state.

        This is only required during initialization. Later on the mouse
        position will be passed through events.
        """

        x = ctypes.c_int(0)
        y = ctypes.c_int(0)

        sdl2.mouse.SDL_GetMouseState(ctypes.byref(x), ctypes.byref(y))

        self._mouse_x = x.value
        self._mouse_y = y.value
        return self._mouse_x, self._mouse_y

    def get_scene(self, scene_name):
        index = 0
        for name in self.scene_indictor:
            if name == scene_name:
                return self.scenes[index]
            index += 1

        return None

    def create_scene(self, scene_name):
        '''
        Creates a scene
        '''
        
        # Check if scene exist
        scene = self.get_scene(scene_name)

        assert scene == None, "Scene exist!"

        # Insert scene
        self.scenes.append([])
        self.scene_indictor.append(scene_name)

    def remove_scene(self, scene_name):
        '''
        Removes scene from both self.scenes and self.activated_scenes
        '''
        
        # Get the scene
        scene = self.get_scene(scene_name)

        assert scene != None, ""

        # Remove scene if all goes well
        self.scenes.remove(scene)
        self.activated_scenes.remove(scene)

    def event(self):
        event = sdl2.SDL_Event()
        return event

    def hide(self):
        self.hide()

    def close(self):
        self.close()

    def set_background(self, r, g, b): 
        '''
        Loop through height and width value. Divided by 10 because of weird math.

        Process takes about a second
        '''
        index = 0
        self.background = sdl2.ext.Color(r, g, b)
        self.renderer.clear(sdl2.ext.Color(self.background[0], self.background[1], self.background[2]))
        self.renderer.present()
        

class Camera:
    
    def __init__(self, world, scene_name):
        self.scene = world.get_scene(scene_name)
        self.exclude_list = []
    
    def move_y(self, y):
        for object in self.scene:
            object.position.y += y

    def move_x(self, x):
        for object in self.scene:
            if common.check_in_array(self.exclude_list, object) == False:
                object.position.x += x

    def exclude(self, object):
        self.exclude_list.append(object)

# functions
def run(world):
    '''
    Runs a window without an event loop.
    '''
    
    assert type(world) == Window, "Parameter is not a world"

    processor = sdl2.ext.TestEventProcessor()
    processor.run(world)

def quit():
    sdl2.SDL_Quit()