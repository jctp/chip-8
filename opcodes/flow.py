def flow_opcodes(self, opcode, opcode_hi_byte, opcode_lo_byte):
    
    # 00EE
    # RET
    # Return from a subroutine
    if (opcode & 0xFFFF) == 0x00EE:
        # TODO: Implement
        self.log_opcode(
            opcode,
            "RET",
            f"",
            implemented = False
        )
        return 1

    # 1NNN
    # JP NNN
    # Jump to address NNN
    elif (opcode & 0xF000) == 0x1000:
        # TODO: Implement
        self.log_opcode(
            opcode,
            "JP NNN",
            f"",
            implemented = False
        )
        return 1

    # 2NNN
    # CALL NNN
    # Call subroutine at NNN
    elif (opcode & 0xF000) == 0x2000:
        # TODO: Implement
        self.log_opcode(
            opcode,
            "CALL NNN",
            f"",
            implemented = False
        )
        return 1

    # BNNN
    # JP V0, NNN
    # Jump to NNN + V0
    elif (opcode & 0xF000) == 0xB000:
        # TODO: Implement
        self.log_opcode(
            opcode,
            "JP V0, NNN",
            f"",
            implemented = False
        )
        return 1