def input_opcodes(self, opcode, opcode_hi_byte, opcode_lo_byte):

    # FX0A
    # LD Vx, K
    # Wait for key press, store key in Vx
    if (opcode & 0xF0FF) == 0xF00A:
        # TODO: Implement
        self.log_opcode(
            opcode,
            "LD Vx, K",
            f"",
            implemented = False
        )
        return 1