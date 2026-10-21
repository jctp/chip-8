def timer_opcodes(self, opcode, opcode_hi_byte, opcode_lo_byte):

    # FX07
    # LD Vx, DT
    # Set Vx = Delay Timer
    if (opcode & 0xF0FF) == 0xF007:
        # TODO: Implement
        self.log_opcode(
            opcode,
            "LD Vx, DT"
            f"",
            implemented = False
        )
        return 1

    # FX15
    # LD DT, Vx
    # Set Delay Timer = Vx
    if (opcode & 0xF0FF) == 0xF015:
        # TODO: Implement
        self.log_opcode(
            opcode,
            "LD DT, Vx"
            f"",
            implemented = False
        )
        return 1

    # FX18
    # LD ST, Vx
    # Set Sount Timer = Vx
    if (opcode & 0xF0FF) == 0xF018:
        # TODO: Implement
        self.log_opcode(
            opcode,
            "LD ST, Vx"
            f"",
            implemented = False
        )
        return 1