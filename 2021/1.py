class Puzzle_Input:

    def __init__(self, filename):
        self.filename = filename

    def read(self):
        with open(self.filename, 'r') as f:
            content_raw = f.readlines()
            # Clean printed newline
            content = [line.replace('\n','') for line in content_raw]
        return content

# Puzzle 1a
txt_file = 'input_1a.txt'
puzzle_input = Puzzle_Input(txt_file)
print(puzzle_input.read())