def mops_opcodes(self, opcode, opcode_hi_byte, opcode_lo_byte):
    
    # ANNN
    # LD I, addr
    # Move into register
    if (opcode & 0xF000) == 0xA000:
        address = opcode & 0x0FFF
        self.index_register.set(address)
        self.log_opcode(
            opcode,
            "LD I, addr",
            f"I = {address:03X}",
            implemented = True
        )
        return 1

    # 6XNN
    # LD Vx, byte
    # Set Vx = kk
    if (opcode & 0xF000) == 0x6000:
        x = (opcode & 0x0F00) >> 8
        self.v[x].set(opcode_lo_byte)
        self.log_opcode(
            opcode,
            "LD Vx, byte",
            f"x = {x}, byte = {opcode_lo_byte:02X}",
            implemented = True
        )
        return 1