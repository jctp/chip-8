from opcodes._dispatcher import dispatcher_cycle
import time

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

    def __init__(self, memory, display, io, rom, cpu_hz, debug_logger):
        self.memory = memory
        self.display = display
        self.io = io
        self.rom = rom
        self.cpu_hz = cpu_hz
        self.logger = debug_logger

        self.stack = []
        self.logger.debug("Set up empty stack.")

        # Set up general purpose registers
        self.v = [self.EightBitRegister() for _ in range(16)]

        self.delay_register = self.EightBitRegister()
        self.sound_register = self.EightBitRegister()
        
        self.delay_timer = self.Timer(self.delay_register)
        self.sound_timer = self.Timer(self.sound_register)
        
        self.program_counter = self.SixteenBitRegister()
        self.program_counter.set(0x200)

        self.stack_pointer = self.EightBitRegister()
        self.index_register = self.SixteenBitRegister()

        # Load ROM into memory at 0x200
        for i, byte in enumerate(self.rom.contents):
            self.memory.contents[i + 0x200] = byte

    def log_opcode(
        self,
        opcode,
        mnemomic,
        extra=None,
        implemented=False
    ):

        #if implemented == False:
            #raise Exception(f"Opcode not implemented: {opcode:04X}, mnemonic: {mnemonic}")

        if extra != None:
            self.logger.debug(f"{opcode}: {mnemomic}: {extra}")
        else:
            self.logger.debug(f"{opcode}: {mnemomic}")

    def cycle(self):
        current_pc = self.program_counter.contents
        opcode = (
            (self.memory.contents[current_pc] << 8) | (self.memory.contents[current_pc + 1])
        )
        opcode_hi_byte = self.memory.contents[current_pc]
        opcode_lo_byte = self.memory.contents[current_pc + 1]

        self.logger.debug(f"Opcode:{opcode:04X} {opcode_hi_byte:02X} {opcode_lo_byte:02X}")

        cycles_to_wait = dispatcher_cycle(self, opcode, opcode_hi_byte, opcode_lo_byte)

        # Safety
        if cycles_to_wait == None:
            cycles_to_wait = 1

        self.display.redraw()

        time.sleep(0.20 * cycles_to_wait)
        self.program_counter.inc(2)

