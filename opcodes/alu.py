def alu_opcodes(self, opcode, opcode_hi_byte, opcode_lo_byte):

    # 7XNN
    # ADD Vx, byte
    if (opcode & 0xF000) == 0x7000:
        self.log_opcode(
            opcode,
            "ADD Vx, byte",
            f"",
            implemented = False
        )

    # 8XY0
    # LD Vx, Vy
    elif (opcode & 0xF00F) == 0x8000:
        self.log_opcode(
            opcode,
            "LD Vx, Vy",
            f"",
            implemented = False
        )

    # 8XY1
    # OR
    elif (opcode & 0xF00F) == 0x8001:
        self.log_opcode(
            opcode,
            "OR",
            f"",
            implemented = False
        )

    # 8XY2
    # AND
    elif (opcode & 0xF00F) == 0x8002:
        self.log_opcode(
            opcode,
            "AND",
            f"",
            implemented = False
        )

    # 8XY3
    # XOR
    if (opcode & 0xF00F) == 0x8003:
        self.log_opcode(
            opcode,
            "XOR",
            f"",
            implemented = False
        )

    # 8XY4
    # ADD
    if (opcode & 0xF00F) == 0x8004:
        self.log_opcode(
            opcode,
            "ADD",
            f"",
            implemented = False
        )

    # 8XY5
    # SUB
    if (opcode & 0xF00F) == 0x8005:
        self.log_opcode(
            opcode,
            "SUB",
            f"",
            implemented = False
        )

    # 8XY6
    # SHR
    elif (opcode & 0xF00F) == 0x8006:
        self.log_opcode(
            opcode,
            "SHR",
            f"",
            implemented = False
        )

    # 8XY7
    # SUBN Vx, Vy
    elif (opcode & 0xF00F) == 0x8007:
        self.log_opcode(
            opcode,
            "SHR",
            f"",
            implemented = False
        )

    # 8XYE
    # SHL
    elif (opcode & 0xF00F) == 0x800E:
        self.log_opcode(
            opcode,
            "SHL",
            f"",
            implemented = False
        )

    # FX1E
    # ADD I, Vx
    elif (opcode & 0xF0FF) == 0xF01E:
        self.log_opcode(
            opcode,
            "ADD I, Vx",
            f"",
            implemented = False
        )