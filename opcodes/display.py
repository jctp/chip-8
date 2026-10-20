def display_opcodes(opcode):
    match opcode:

        # CLS, clear the display
        case 0x00E0:
            self.log_opcode(opcode, "CLS")
            self.program_counter.inc()
            return 1