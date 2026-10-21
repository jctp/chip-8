from logger import logger

from chip8 import Chip8Cpu
from memory import Chip8Memory
from rom import Chip8Rom
from display import Chip8Display
from chip8_io import Chip8IO

system_rom = Chip8Rom(file_path="roms/superpong.ch8", debug_logger=logger)
system_display = Chip8Display()
system_memory = Chip8Memory()
system_io = Chip8IO()

system_cpu = Chip8Cpu(
    memory=system_memory,
    display=system_display,
    io=system_io,
    rom=system_rom,
    cpu_hz=6000,
    debug_logger=logger,
)

while True:
    system_cpu.cycle()
