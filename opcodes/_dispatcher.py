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
    alu_opcodes(self, opcode, opcode_hi_byte, opcode_lo_byte)
    display_opcodes(self, opcode, opcode_hi_byte, opcode_lo_byte)
    flow_opcodes(self, opcode, opcode_hi_byte, opcode_lo_byte)
    input_opcodes(self, opcode, opcode_hi_byte, opcode_lo_byte)
    mops_opcodes(self, opcode, opcode_hi_byte, opcode_lo_byte)
    register_opcodes(self, opcode, opcode_hi_byte, opcode_lo_byte)
    rng_opcodes(self, opcode, opcode_hi_byte, opcode_lo_byte)
    skips_opcodes(self, opcode, opcode_hi_byte, opcode_lo_byte)
    timer_opcodes(self, opcode, opcode_hi_byte, opcode_lo_byte)
    return
