import pygame


class Chip8Display:
    WINDOW_WIDTH = 64
    WINDOW_HEIGHT = 32
    WINDOW_SCALE = 15

    def __init__(self):
        pygame.init()
        self.pixels = bytearray(64 * 32)

        self.screen = pygame.display.set_mode(
            (
                self.WINDOW_WIDTH * self.WINDOW_SCALE,
                self.WINDOW_HEIGHT * self.WINDOW_SCALE,
            )
        )

    def redraw(self):
        self.screen.fill((0, 0, 0))

        for y in range(self.WINDOW_HEIGHT):
            for x in range(self.WINDOW_WIDTH):
                if self.pixels[y * self.WINDOW_WIDTH + x]:
                    pygame.draw.rect(
                        self.screen,
                        (255, 255, 255),
                        (
                            x * self.WINDOW_SCALE,
                            y * self.WINDOW_SCALE,
                            self.WINDOW_SCALE,
                            self.WINDOW_SCALE,
                        ),
                    )
        pygame.display.flip()

    def xor(self, x, y):
        index = (y % 32) * 64 + (x % 64)
        old_pixel = self.pixels[index]
        self.pixels[index] ^= 1

        collision = old_pixel == 1 and self.pixels == 0

        return collision

    def read(self, x, y):
        return self.pixels[y * 64 + x]

    def clear(self):
        self.pixels = bytearray(64 * 32)
