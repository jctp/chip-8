import pygame

class Chip8Display:
    WINDOW_WIDTH = 64
    WINDOW_HEIGHT = 32
    WINDOW_SCALE = 15

    def __init__(self, background_colour, foreground_colour):
        pygame.init()
        pygame.display.set_caption("CHIPster")
        self.pixel_map = bytearray(64 * 32)

        self.background_colour = background_colour
        self.foreground_colour = foreground_colour

        self.screen = pygame.display.set_mode(
            (
                self.WINDOW_WIDTH * self.WINDOW_SCALE,
                self.WINDOW_HEIGHT * self.WINDOW_SCALE,
            )
        )

        self.pixels = pygame.Surface(
            (
                self.WINDOW_WIDTH * self.WINDOW_SCALE,
                self.WINDOW_HEIGHT * self.WINDOW_SCALE
            ),
            pygame.SRCALPHA
        )

    def redraw(self):
        self.screen.fill(self.background_colour)
        self.pixels.fill((0, 0, 0, 0))

        # Pixels
        for y in range(self.WINDOW_HEIGHT):
            for x in range(self.WINDOW_WIDTH):
                if self.pixel_map[y * self.WINDOW_WIDTH + x]:
                    pygame.draw.rect(
                        self.pixels,
                        (self.foreground_colour),
                        (
                            x * self.WINDOW_SCALE,
                            y * self.WINDOW_SCALE,
                            self.WINDOW_SCALE,
                            self.WINDOW_SCALE,
                        ),
                    )

        self.screen.blit(self.pixels, (0, 0))

        pygame.display.flip()

    def xor(self, x, y):
        index = (y % 32) * 64 + (x % 64)
        old_pixel = self.pixel_map[index]
        self.pixel_map[index] ^= 1

        collision = old_pixel == 1 and self.pixel_map[index] == 0

        return collision

    def read(self, x, y):
        return self.pixel_map[y * 64 + x]

    def clear(self):
        self.pixel_map = bytearray(64 * 32)
