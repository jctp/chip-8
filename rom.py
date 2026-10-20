class Chip8Rom:
    def __init__(self, file_path, debug_logger):
        self.logger = debug_logger
        with open(file_path, "rb") as file:
            self.contents = file.read()
        self.logger.debug(f"Loaded {file_path}, length {len(self.contents)}.")