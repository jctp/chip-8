from opcodes.alu import alu_opcodes
from opcodes.display import display_opcodes
from opcodes.flow import flow_opcodes
from opcodes.input import input_opcodes
from opcodes.memory_operations import mops_opcodes
from opcodes.register_loads_moves import register_opcodes
from opcodes.rng import rng_opcodes
from opcodes.skips import skips_opcodes
from opcodes.timers import timer_opcodes


def dispatcher_cycle(self, opcode, opcode_hi_byte, opcode_lo_byte):
    # Brute force it for now

    cycles = 0

    cycles = alu_opcodes(self, opcode, opcode_hi_byte, opcode_lo_byte)
    cycles = display_opcodes(self, opcode, opcode_hi_byte, opcode_lo_byte)
    cycles = flow_opcodes(self, opcode, opcode_hi_byte, opcode_lo_byte)
    cycles = input_opcodes(self, opcode, opcode_hi_byte, opcode_lo_byte)
    cycles = mops_opcodes(self, opcode, opcode_hi_byte, opcode_lo_byte)
    cycles = register_opcodes(self, opcode, opcode_hi_byte, opcode_lo_byte)
    cycles = rng_opcodes(self, opcode, opcode_hi_byte, opcode_lo_byte)
    cycles = skips_opcodes(self, opcode, opcode_hi_byte, opcode_lo_byte)
    cycles = timer_opcodes(self, opcode, opcode_hi_byte, opcode_lo_byte)

    if cycles == 0:
        raise Exception(f"Opcode not implemented or stubbed: {opcode:04X}")

    return
