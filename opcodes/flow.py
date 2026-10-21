def flow_opcodes(self, opcode, opcode_hi_byte, opcode_lo_byte):

    # 2NNN
    # CALL NNN
    # Call subroutine at NNN
    if (opcode & 0xF000) == 0x2000:
        subroutine_address = opcode & 0x0FFF

        _old_stack_counter = self.program_counter.get()

        self.stack.append(self.program_counter.get() + 2)

        self.program_counter.set(subroutine_address)
        self.program_counter.dec(2)  # Will be incremented in same cycle by caller

        self.log_opcode(
            opcode,
            "CALL NNN",
            f"Added 1 to stack pointer, jumped from {_old_stack_counter:04X} to {self.program_counter.get():04X}",
            implemented=True,
        )
        return 1

    # 00EE
    # RET
    # Return from a subroutine
    elif (opcode & 0xFFFF) == 0x00EE:
        _old_stack_counter = self.program_counter.get()

        self.program_counter.set(self.stack.pop())
        self.program_counter.dec(2)  # Will be incremented in same cycle by caller

        self.log_opcode(
            opcode,
            "RET",
            f"Subtracted 1 from stack pointer, jumped from {_old_stack_counter:04X} to {self.program_counter.get():04X}",
            implemented=True,
        )
        return 1

    # 1NNN
    # JP NNN
    # Jump to address NNN
    elif (opcode & 0xF000) == 0x1000:
        address = opcode & 0x0FFF
        self.program_counter.set(address)
        self.program_counter.dec(2)  # Will be incremented in same cycle by caller

        self.log_opcode(
            opcode, "JP NNN", f"Set program counter to {address:04X}", implemented=True
        )
        return 1

    # BNNN
    # JP V0, NNN
    # Jump to NNN + V0
    elif (opcode & 0xF000) == 0xB000:
        opcode_destination = opcode & 0x0FFF
        v0 = self.v[0].contents
        jump_destination = (opcode_destination + v0) & 0xFFFF
        self.program_counter.set(jump_destination)
        self.log_opcode(
            opcode,
            "JP V0, NNN",
            f"Jumped to {self.program_counter.contents:04X} ({opcode_destination:04X} + {v0:04X})",
            implemented=True,
        )
        return 1
