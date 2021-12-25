class Puzzle_Input:
    def __init__(self, filename, type='string'):
        self.filename = filename
        self.type = type
        self.list = self.read(type)

    def read(self, type):
        with open(self.filename, 'r') as f:
            content_raw = f.readlines()
            # Clean printed newline
        return [int(line.replace('\n','')) if type == 'int' else (line.replace('\n','')) for line in content_raw]

    def drop_speed(self, rolling=1):
        if self.type == 'int' and rolling > 0:
            data = puzzle_input.list if rolling == 1 else [sum(x) for x in zip(puzzle_input.list, puzzle_input.list[1:], puzzle_input.list[2:])]
        else: sys.exit(f'type of data has to be "numbers" and "rolling" must be a positive value.')

        return sum(y > x for x, y in zip(data, data[1:])) # this one line solution was copied from reddit thread - author not known anymore


# Puzzle 1a
txt_file = 'input_1a.txt'
puzzle_input = Puzzle_Input(txt_file, 'int')
print(f'Solution for 1a: {puzzle_input.drop_speed()}')
print(f'Solution for 1b: {puzzle_input.drop_speed(3)}')
