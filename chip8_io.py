# Keymap
# Emu       Keyboard

# 1 2 3 C   1 2 3 4
# 4 5 6 D   Q W E R
# 7 8 9 E   A S D F
# A 0 B F   Z X C V

import pygame


class Chip8IO:
    def __init__(self):
        self.keys = [False] * 16

        self.key_map = {
            pygame.K_1: 0x1,
            pygame.K_2: 0x2,
            pygame.K_3: 0x3,
            pygame.K_4: 0xC,
            pygame.K_q: 0x4,
            pygame.K_w: 0x5,
            pygame.K_e: 0x6,
            pygame.K_r: 0xD,
            pygame.K_a: 0x7,
            pygame.K_s: 0x8,
            pygame.K_d: 0x9,
            pygame.K_f: 0xE,
            pygame.K_z: 0xA,
            pygame.K_x: 0x0,
            pygame.K_c: 0xB,
            pygame.K_v: 0xF,
        }

    def set_key(self, pygame_key, state):
        if pygame_key in self.key_map:
            chip8_key = self.key_map[pygame_key]
            self.keys[chip8_key] = state
