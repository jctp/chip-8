def display_opcodes(self, opcode, opcode_hi_byte, opcode_lo_byte):
    
    # 00E0
    # CLS
    # Clear the display
    if opcode == 0x00E0:
        self.display.clear()
        self.log_opcode(
            opcode,
            "CLS",
            f"SCREEN CLEAR",
            implemented = True
        )
        return 1

    # DXYN
    # DRW Vx, Vy, N
    elif (opcode & 0xF000) == 0xD000:
        x = (opcode & 0x0F00) >> 8
        y = (opcode & 0x00F0) >> 4
        n = (opcode & 0x000F)

        # Get coordinates
        vx = self.v[x].contents
        vy = self.v[y].contents

        # Clear collision flag
        collision = False
        for row in range(n):
            sprite_byte = self.memory.contents[
                self.index_register.contents + row
            ]
            for bit in range(8):
                if sprite_byte & (0x80 >> bit):
                    screen_x = vx + bit
                    screen_y = vy + row

                    if self.display.xor(
                        x = screen_x,
                        y = screen_y
                    ):
                        collision = True
        
        # Set collision register if collision is found
        self.v[0xF].set(int(collision))

        