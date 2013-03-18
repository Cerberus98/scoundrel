import pygame


colors = pygame.color.THECOLORS
context = None


class Context(object):
    def __init__(self, screen, clock, tile_size, view, view_size, world_ratio):
        self.screen = screen
        self.clock = clock
        self.view = view
        self.view_size = view_size
        self.tile_size = tile_size
        self.world_ratio = world_ratio

        # Where to start drawing from, for scrolling tiles correctly
        self.camera = (-40, -20)
        self.screen_offset = (0, 0)
        window_size = screen.get_size()
        self.window_scaling = (window_size[0] / 800, window_size[1] / 600)

    def screen_coords(self, position):
        return ((position[0] - self.camera[0]) * self.world_ratio,
                (position[1] - self.camera[1]) * self.world_ratio)

    def __enter__(self):
        return self

    def __exit__(self, type, value, traceback):
        pygame.display.flip()
        self.clock.tick(60)
        pygame.display.set_caption(
            "Scoundrel FPS: %d View: %s Camera: %s Offset %s" %
                (self.clock.get_fps(), self.view, self.camera,
                 self.screen_offset))