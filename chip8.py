from opcodes._dispatcher import dispatcher_cycle
import time
import pygame


class Chip8Cpu:
    class EightBitRegister:
        def __init__(self):
            self.contents = 0

        def set(self, value):
            self.contents = (value) & 0xFF

        def get(self):
            return self.contents

        def inc(self, increment=1):
            self.contents = (self.contents + increment) & 0xFF

        def dec(self, decrement=1):
            self.contents = (self.contents - decrement) & 0xFF

    class SixteenBitRegister:
        def __init__(self):
            self.contents = 0

        def set(self, value):
            self.contents = (value) & 0xFFFF

        def get(self):
            return self.contents

        def inc(self, increment=1):
            self.contents = (self.contents + increment) & 0xFFFF

        def dec(self, decrement=1):
            self.contents = (self.contents - decrement) & 0xFFFF

    class Timer:
        def __init__(self, timer_register):
            self.timer_register = timer_register

    def __init__(self, memory, display, io, rom, cpu_hz, debug_logger, logging_enabled = False):
        self.memory = memory
        self.display = display
        self.io = io
        self.rom = rom
        self.cpu_hz = cpu_hz
        self.logger = debug_logger
        self.logging_enabled = logging_enabled

        self.stack = []  # len() will get the top of the stack

        # Set up general purpose registers
        self.v = [self.EightBitRegister() for _ in range(16)]

        self.delay_register = self.EightBitRegister()
        self.sound_register = self.EightBitRegister()

        self.delay_timer = self.Timer(self.delay_register)
        self.sound_timer = self.Timer(self.sound_register)

        self.program_counter = self.SixteenBitRegister()
        self.program_counter.set(0x200)

        self.index_register = self.SixteenBitRegister()

        # Load ROM into memory at 0x200
        for i, byte in enumerate(self.rom.contents):
            self.memory.contents[i + 0x200] = byte

        # Decade counter for ticks
        self.ticks = 10

        # Sound support
        pygame.mixer.init()
        self.beep = pygame.mixer.Sound("tone.wav")
        self.beeping = False

        self.beep.play()

    def log_opcode(self, opcode, mnemonic, extra=None, implemented=False):

        if implemented == False:
            raise Exception(
                f"Opcode not implemented: {opcode:04X}, mnemonic: {mnemonic}"
            )

        if extra != None:
            self.logger.debug(
                f" {self.program_counter.contents:04X} : {opcode:04X} : {mnemonic} : {extra}"
            )
        else:
            self.logger.debug(
                f" {self.program_counter.contents:04X} : {opcode:04X} : {mnemonic}"
            )

    def timer_tick(self):
        if self.delay_register.get() > 0:
            self.delay_register.dec()

        if self.sound_register.get() > 0:
            if not self.beeping:
                self.beep.play(-1)
                self.beeping = True

            self.sound_register.dec()

        elif self.beeping:
            self.beep.stop()
            self.beeping = False

    def cycle(self):
        # Input handler
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                self.io.set_key(event.key, True)
            if event.type == pygame.KEYUP:
                self.io.set_key(event.key, False)

        current_pc = self.program_counter.contents
        opcode = (self.memory.contents[current_pc] << 8) | (
            self.memory.contents[current_pc + 1]
        )
        opcode_hi_byte = self.memory.contents[current_pc]
        opcode_lo_byte = self.memory.contents[current_pc + 1]

        cycles_to_wait = dispatcher_cycle(self, opcode, opcode_hi_byte, opcode_lo_byte)

        # Safety
        if cycles_to_wait == None:
            cycles_to_wait = 1

        self.display.redraw()

        wait_time = 1 / self.cpu_hz
        counter_delay = wait_time * 10

        self.ticks -= 1

        if self.ticks == 0:
            self.timer_tick()
            self.ticks = 10

        time.sleep(wait_time * cycles_to_wait)
        self.program_counter.inc(2)
