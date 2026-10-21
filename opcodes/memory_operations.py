def mops_opcodes(self, opcode, opcode_hi_byte, opcode_lo_byte):

    # ANNN
    # LD I, addr
    # Move into register
    if (opcode & 0xF000) == 0xA000:
        address = opcode & 0x0FFF
        self.index_register.set(address)
        self.log_opcode(opcode, "LD I, addr", f"I = {address:03X}", implemented=True)
        return 1

    # FX29
    # LD F, Vx
    # Set I to location of sprite for digit in Vx
    elif (opcode & 0xF0FF) == 0xF029:
        # TODO: Impleement
        self.log_opcode(opcode, "LD F, Vx", f"", implemented=False)
        return 1

    # FX33
    # LD B, Vx
    # Store BCD rep. of Vx at I, I+1, I+2
    elif (opcode & 0xF0FF) == 0xF033:
        vx_number = (opcode & 0x0F00) >> 8

        value = self.v[vx_number].get()

        hundreds = value // 100
        tens = (value // 10) % 10
        ones = value % 10

        self.memory.contents[self.index_register.get()] = hundreds
        self.memory.contents[self.index_register.get() + 1] = tens
        self.memory.contents[self.index_register.get() + 2] = ones

        self.log_opcode(
            opcode,
            "LD B, Vx",
            f"",  # TODO: Logging
            implemented=True,
        )
        return 1

    # FX55
    # LD [I], Vx
    # Store registers V0 through Vx in mem. starting at I
    elif (opcode & 0xF0FF) == 0xF055:
        vx_number = (opcode & 0x0F00) >> 8

        for i in range(vx_number + 1):
            self.memory.contents[self.index_register.get() + i] = self.v[i].get()

        self.log_opcode(
            opcode,
            "LD [I], Vx",
            f"",  # TODO: Logging
            implemented=True,
        )
        return 1

    # FX65
    # LD Vx, [I]
    # Load reg. V0 through Vx from mem. starting at I
    elif (opcode & 0xF0FF) == 0xF065:
        vx_number = (opcode & 0x0F00) >> 8

        for i in range(vx_number + 1):
            self.v[i].set(self.memory.contents[self.index_register.get() + i])

        self.log_opcode(
            opcode,
            "LD [I], Vx",
            f"",  # TODO: Logging
            implemented=True,
        )
        return 1
