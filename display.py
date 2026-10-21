import pygame

class Chip8Display:
    WINDOW_WIDTH = 64
    WINDOW_HEIGHT = 32
    WINDOW_SCALE = 15

    def __init__(self):
        pygame.init()
        pygame.display.set_caption("CHIPster")
        self.pixels = bytearray(64 * 32)

        self.screen = pygame.display.set_mode(
            (
                self.WINDOW_WIDTH * self.WINDOW_SCALE,
                self.WINDOW_HEIGHT * self.WINDOW_SCALE,
            )
        )

    def redraw(self):
        self.screen.fill("#827717")

        scanlines = pygame.Surface(
            (
                self.WINDOW_WIDTH * self.WINDOW_SCALE,
                self.WINDOW_HEIGHT * self.WINDOW_SCALE
            ),
            pygame.SRCALPHA
        )

        pixels = pygame.Surface(
            (
                self.WINDOW_WIDTH * self.WINDOW_SCALE,
                self.WINDOW_HEIGHT * self.WINDOW_SCALE
            ),
            pygame.SRCALPHA
        )

        # Scanlines
        for y in range(0, self.WINDOW_HEIGHT * self.WINDOW_SCALE):
            if y % self.WINDOW_SCALE == 0:
                pygame.draw.line(
                    scanlines,
                    ("#AFB42B44"),
                    (0, y),
                    (self.WINDOW_WIDTH * self.WINDOW_SCALE, y)
                )

        # Pixels
        for y in range(self.WINDOW_HEIGHT):
            for x in range(self.WINDOW_WIDTH):
                if self.pixels[y * self.WINDOW_WIDTH + x]:
                    pygame.draw.rect(
                        pixels,
                        ("#CDDC39"),
                        (
                            x * self.WINDOW_SCALE,
                            y * self.WINDOW_SCALE,
                            self.WINDOW_SCALE,
                            self.WINDOW_SCALE,
                        ),
                    )

        self.screen.blit(scanlines, (0, 0))
        self.screen.blit(pixels, (0, 0))

        # CRT Glow - downscale, then upscale again
        glow = self.screen.copy()
        glow = pygame.transform.smoothscale(
            glow,
            (
                glow.get_width() // 10,
                glow.get_height() // 10
            )
        )
        glow = pygame.transform.smoothscale(
            glow,
            self.screen.get_size()
        )
        glow.set_alpha(100)

        self.screen.blit(glow, (0, 0))
        pygame.display.flip()

    def xor(self, x, y):
        index = (y % 32) * 64 + (x % 64)
        old_pixel = self.pixels[index]
        self.pixels[index] ^= 1

        collision = old_pixel == 1 and self.pixels[index] == 0

        return collision

    def read(self, x, y):
        return self.pixels[y * 64 + x]

    def clear(self):
        self.pixels = bytearray(64 * 32)
