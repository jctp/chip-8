from logger import logger

from chip8 import Chip8Cpu
from memory import Chip8Memory
from rom import Chip8Rom
from display import Chip8Display

system_rom = Chip8Rom(
    file_path="roms/3-corax+.ch8",
    debug_logger=logger
)
system_display = Chip8Display()
system_memory = Chip8Memory()
system_cpu = Chip8Cpu(
    memory=system_memory, display=system_display, io=None, rom=system_rom, cpu_hz=None, debug_logger=logger
)

while True:
    system_cpu.cycle()