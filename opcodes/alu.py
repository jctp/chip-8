def alu_opcodes(self, opcode, opcode_hi_byte, opcode_lo_byte):

    # 7XNN
    # ADD Vx, byte
    # Adds the value NN to value of register Vx, then stores result in Vx
    if (opcode & 0xF000) == 0x7000:
        register_number = (opcode & 0x0F00) >> 8
        incoming_byte = opcode_lo_byte
        self.v[register_number].set(self.v[register_number].contents + incoming_byte)
        self.log_opcode(
            opcode,
            "ADD Vx, byte",
            f"Added {incoming_byte:02X} to V{register_number}",
            implemented=True,
        )

    # 8XY1
    # OR Vx, Vy
    # Bitwise OR on values of Vx and Vy, stores result in Vx
    elif (opcode & 0xF00F) == 0x8001:
        vx_register = (opcode & 0x0F00) >> 8
        vy_register = (opcode & 0x00F0) >> 4

        vx_contents = self.v[vx_register].contents
        vy_contents = self.v[vy_register].contents

        self.v[vx_register].set(vx_contents | vy_contents)

        if self.logging_enabled:
            self.log_opcode(
                opcode,
                "OR Vx, Vy",
                f"(V{vx_register}) {vx_contents:02X} OR (V{vy_register}) {vy_contents:02X}",
                implemented=True,
            )

    # 8XY2
    # AND Vx, Vy
    # Bitwise AND on values of Vx and Vy, stores result in Vx
    elif (opcode & 0xF00F) == 0x8002:
        vx_register = (opcode & 0x0F00) >> 8
        vy_register = (opcode & 0x00F0) >> 4

        vx_contents = self.v[vx_register].contents
        vy_contents = self.v[vy_register].contents

        self.v[vx_register].set(vx_contents & vy_contents)

        if self.logging_enabled:
            self.log_opcode(
                opcode,
                "AND Vx, Vy",
                f"(V{vx_register}) {vx_contents:02X} AND (V{vy_register}) {vy_contents:02X}",
                implemented=True,
            )

    # 8XY3
    # XOR Vx, Vy
    elif (opcode & 0xF00F) == 0x8003:
        vx_register = (opcode & 0x0F00) >> 8
        vy_register = (opcode & 0x00F0) >> 4

        vx_contents = self.v[vx_register].contents
        vy_contents = self.v[vy_register].contents

        self.v[vx_register].set(vx_contents ^ vy_contents)

        if self.logging_enabled:
            self.log_opcode(
                opcode,
                "XOR Vx, Vy",
                f"(V{vx_register}) {vx_contents:02X} XOR (V{vy_register}) {vy_contents:02X}",
                implemented=True,
            )

    # 8XY4
    # ADD Vx, Vy
    elif (opcode & 0xF00F) == 0x8004:
        vx_register = (opcode & 0x0F00) >> 8
        vy_register = (opcode & 0x00F0) >> 4

        vx_contents = self.v[vx_register].contents
        vy_contents = self.v[vy_register].contents

        result = (vx_contents + vy_contents) & 0xFF

        self.v[vx_register].set(result)

        if result > 0xFF:
            self.v[0xF].set(1)
        else:
            self.v[0xF].set(0)

        if self.logging_enabled:
            self.log_opcode(
                opcode,
                "ADD Vx, Vy",
                f"(V{vx_register}) {vx_contents:02X} + (V{vy_register}) {vy_contents:02X}",
                implemented=True,
            )

    # 8XY5
    # SUB Vx, Vy
    elif (opcode & 0xF00F) == 0x8005:
        vx_register = (opcode & 0x0F00) >> 8
        vy_register = (opcode & 0x00F0) >> 4

        vx_contents = self.v[vx_register].contents
        vy_contents = self.v[vy_register].contents

        if vx_contents > vy_contents:
            self.v[0xF].set(1)
        else:
            self.v[0xF].set(0)

        result = (vx_contents - vy_contents) & 0xFF

        self.v[vx_register].set(result)

        if self.logging_enabled:
            self.log_opcode(
                opcode,
                "SUB Vx, Vy",
                f"(V{vx_register}) {vx_contents:02X} - (V{vy_register}) {vy_contents:02X}",
                implemented=True,
            )

    # 8XY7
    # SUBN Vx, Vy
    elif (opcode & 0xF00F) == 0x8007:
        vx_register = (opcode & 0x0F00) >> 8
        vy_register = (opcode & 0x00F0) >> 4

        vx_contents = self.v[vx_register].contents
        vy_contents = self.v[vy_register].contents

        vx_lsb = vx_contents & 0x01

        if vy_contents >= vx_contents:
            self.v[0xF].set(1)
        else:
            self.v[0xF].set(0)

        result = vy_contents - vx_contents

        self.v[vx_register].set(result)

        if self.logging_enabled:
            self.log_opcode(
                opcode,
                "SUBN Vx, Vy",
                f"",  # TODO: Logging
                implemented=True,
            )

    # 8XYE
    # SHL Vx {, Vy}
    elif (opcode & 0xF00F) == 0x800E:
        vx_register = (opcode & 0x0F00) >> 8
        vy_register = (opcode & 0x00F0) >> 4

        vx_contents = self.v[vx_register].contents
        vy_contents = self.v[vy_register].contents

        vx_msb = (vx_contents & 0x80) >> 7

        if vx_msb == 1:
            self.v[0xF].set(1)
        else:
            self.v[0xF].set(0)

        vx_mult_2 = vx_contents * 2

        self.v[vx_register].set(vx_mult_2)

        if self.logging_enabled:
            self.log_opcode(
                opcode,
                "SHL {Vx, Vy}",
                f"",  # TODO: Logging
                implemented=True,
            )

    # 8XY6
    # SHR Vx {, Vy}
    elif (opcode & 0xF00F) == 0x8006:
        vx_register = (opcode & 0x0F00) >> 8
        vy_register = (opcode & 0x00F0) >> 4

        vx_contents = self.v[vx_register].contents
        vy_contents = self.v[vy_register].contents

        vx_lsb = vx_contents & 0x01

        if vx_lsb == 1:
            self.v[0xF].set(1)
        else:
            self.v[0xF].set(0)

        vx_div_2 = int(vx_contents / 2)

        self.v[vx_register].set(vx_div_2)

        if self.logging_enabled:
            self.log_opcode(
                opcode,
                "SHR Vx {, Vy}",
                f"V{vx_register} LSB is {vx_lsb}; V{vx_register} set to {vx_div_2}",
                implemented=True,
            )

    # FX1E
    # ADD I, Vx
    elif (opcode & 0xF0FF) == 0xF01E:
        vx_register = (opcode & 0x0F00) >> 8
        vx_contents = self.v[vx_register].contents

        self.index_register.set(self.index_register.contents + vx_contents)

        if self.logging_enabled:
            self.log_opcode(
                opcode,
                "ADD I, Vx",
                f"",  # TODO: Logging
                implemented=True,
            )
