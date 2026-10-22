def input_opcodes(self, opcode, opcode_hi_byte, opcode_lo_byte):

    # FX0A
    # LD Vx, K
    # Wait for key press, store key in Vx
    if (opcode & 0xF0FF) == 0xF00A:
        vx_number = (opcode & 0x0F00) >> 8

        for key, pressed in enumerate(self.io.keys):
            if pressed:
                self.v[vx_number].set(key)
                if self.logging_enabled:
                    self.log_opcode(
                        opcode,
                        "LD Vx, K",
                        f"Stored key {key:X} in V{vx_number:X}",
                        implemented=True,
                    )
                return 1

        self.program_counter.dec(2)
        return 1

    # EX9E
    # SKP Vx
    # Skip next instruction if key with value of Vx pressed
    elif (opcode & 0xF0FF) == 0xE09E:
        vx_number = (opcode & 0x0F00) >> 8

        if self.io.keys[self.v[vx_number].get()]:
            self.program_counter.inc(2)
            if self.logging_enabled:
                self.log_opcode(
                    opcode,
                    "SKP Vx",
                    f"Key {vx_number:X} pressed, skipping",
                    implemented=True,
                )
            return 1

        if self.logging_enabled:
            self.log_opcode(
                opcode,
                "SKP Vx",
                f"Key {vx_number:X} not pressed, not skipping",
                implemented=True,
            )
        return 1

    # EXA1
    # SKNP Vx
    # Skip next instruction if key with value of Vx not pressed
    elif (opcode & 0xF0FF) == 0xE0A1:
        vx_number = (opcode & 0x0F00) >> 8

        if not self.io.keys[self.v[vx_number].get()]:
            self.program_counter.inc(2)
            if self.logging_enabled:
                self.log_opcode(
                    opcode,
                    "SKNP Vx",
                    f"Key {vx_number:X} not pressed, skipping",
                    implemented=True,
                )
            return 1
        if self.logging_enabled:
            self.log_opcode(
                opcode,
                "SKNP Vx",
                f"Key {vx_number:X} pressed, not skipping",
                implemented=True,
            )
        return 1
