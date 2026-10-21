def rng_opcodes(self, opcode, opcode_hi_byte, opcode_lo_byte):

    # CXNN
    # RND Vx, NNN
    # Set Vx = random_byte AND NN
    if (opcode & 0xF000) == 0xC000:
        # TODO: Implement
        self.log_opcode(opcode, "RND Vx, NNN", f"", implemented=False)
        return 1
