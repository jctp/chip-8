def timer_opcodes(self, opcode, opcode_hi_byte, opcode_lo_byte):

    # FX07
    # LD Vx, DT
    # Set Vx = Delay Timer
    if (opcode & 0xF0FF) == 0xF007:
        vx_number = (opcode & 0x0F00) >> 8
        self.v[vx_number].set(self.delay_timer.timer_register.contents)
        if self.logging_enabled:
            self.log_opcode(opcode, f"LD Vx, DT", f"", implemented=True)  # TODO: Logging
        return 1

    # FX15
    # LD DT, Vx
    # Set Delay Timer = Vx
    if (opcode & 0xF0FF) == 0xF015:
        vx_number = (opcode & 0x0F00) >> 8
        self.delay_timer.timer_register.set(self.v[vx_number].contents)
        if self.logging_enabled:
            self.log_opcode(opcode, f"LD DT, Vx", f"", implemented=True)  # TODO: Logging
        return 1

    # FX18
    # LD ST, Vx
    # Set Sound Timer = Vx
    if (opcode & 0xF0FF) == 0xF018:
        vx_number = (opcode & 0x0F00) >> 8
        self.sound_timer.timer_register.set(self.v[vx_number].contents)
        if self.logging_enabled:
            self.log_opcode(opcode, f"LD ST, Vx", f"", implemented=True)  # TODO: Logging
        return 1
