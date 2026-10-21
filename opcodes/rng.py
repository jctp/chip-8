import random


def rng_opcodes(self, opcode, opcode_hi_byte, opcode_lo_byte):

    # CXNN
    # RND Vx, NNN
    # Set Vx = random_byte AND NN
    if (opcode & 0xF000) == 0xC000:
        vx_number = (opcode & 0x0F00) >> 8
        nn = opcode & 0x00FF
        output = random.randint(0, 255) & nn
        self.v[vx_number].set(output)
        self.log_opcode(opcode, "RND Vx, NNN", f"", implemented=True)  # TODO: Logging
        return 1
