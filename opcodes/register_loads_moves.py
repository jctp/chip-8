def register_opcodes(self, opcode, opcode_hi_byte, opcode_lo_byte):
    
    # 6XNN
    # LD Vx, byte
    # Set Vx = NN
    if (opcode & 0xF000) == 0x6000:

        x = (opcode & 0x0F00) >> 8
        self.v[x].set(opcode_lo_byte)
        self.log_opcode(

            opcode,
            "LD Vx, NN",
            f"x = {x}, NN = {opcode_lo_byte:02X}",
            implemented = True
        )
        return 1

    # 8XY0
    # LD Vx, Vy
    # Set Vx = Vy
    elif (opcode & 0xF00F) == 0x8000:

        x = (opcode & 0x0F00) >> 8
        y = (opcode & 0x00F0) >> 4

        self.v[x].set(
            self.v[y].contents
        )
        
        self.log_opcode(
            opcode,
            "LD Vx, Vy",
            f"Set v{x} to value in v{y} ({self.v[x].contents:02X})",
            implemented = True
        )
        return 1