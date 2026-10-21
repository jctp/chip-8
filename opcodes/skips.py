def skips_opcodes(self, opcode, opcode_hi_byte, opcode_lo_byte):


    # 3XNN
    # SE Vx, NN
    # Skip next instruction if Vx == NN
    if (opcode & 0xF000) == 0x3000:
        # TODO: Implement
        self.log_opcode(
            opcode,
            "SE Vx, NN",
            f"",
            implemented = False
        )
        return 1

    # 4XNN
    # SNE Vx, NN
    # Skip next instruction if Vx != NN
    elif (opcode & 0xF000) == 0x4000:
        # TODO: Implement
        self.log_opcode(
            opcode,
            "SNE Vx, NN",
            f"",
            implemented = False
        )
        return 1

    # 5XY0
    # SE Vx, Vy
    # Skip next instruction if Vx == Vy
    elif (opcode & 0xF000) == 0x5000:
        # TODO: Implement
        self.log_opcode(
            opcode,
            "SE Vx, Vy",
            f"",
            implemented = False
        )
        return 1

    # 9XY0
    # SNE Vx, Vy
    # Skip next instruction if Vx != Vy
    elif (opcode & 0xF000) == 0x9000:
        # TODO: Implement
        self.log_opcode(
            opcode,
            "SNE Vx, Vy",
            f"",
            implemented = False
        )
        return 1

    # EX9E
    # SKP Vx
    # Skip next instruction if key with value of Vx pressed
    elif (opcode & 0xF0FF) == 0xE09E:
        # TODO: Implement
        self.log_opcode(
            opcode,
            "SKP Vx",
            f"",
            implemented = False
        )
        return 1

    # EXA1
    # SKNP Vx
    # Skip next instruction if key with value of Vx pressed
    elif (opcode & 0xF0FF) == 0xE0A1:
        # TODO: Implement
        self.log_opcode(
            opcode,
            "SKNP Vx",
            f"",
            implemented = False
        )
        return 1
