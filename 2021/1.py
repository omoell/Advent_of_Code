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
            data = self.list if rolling == 1 else [sum(x) for x in zip(self.list, self.list[1:], self.list[2:])]
        else: sys.exit(f'type of data has to be "numbers" and "rolling" must be a positive value.')

        return sum(y > x for x, y in zip(data, data[1:])) # this one line solution was copied from reddit thread - author not known anymore

    def steps(self):
        steps_raw = [step.split(' ') for step in self.list]
        return [[direction, (-int(value) if direction == 'up' else int(value))] for direction, value in steps_raw]

    def final_position(self):
        horizontal = 0
        depth = 0
        steps = self.steps()
        for direction, value in steps:
            if direction == 'forward':
                horizontal = horizontal + value
            else:
                depth = depth + value
        return horizontal * depth

    def final_position_w_aim(self):
        horizontal = 0
        aim = 0
        depth = 0
        steps = self.steps()
        for direction, value in steps:
            if direction == 'forward':
                depth = depth + (aim * value)
                horizontal = horizontal + value
            else:
                aim = aim + value
        return horizontal * depth

# Puzzle 1
puzzle1_file = 'input_1.txt'
puzzle1 = Puzzle_Input(puzzle1_file, 'int')
print(f'Solution for 1a: {puzzle1.drop_speed()}')
print(f'Solution for 1b: {puzzle1.drop_speed(3)}')

# Puzzle 2
puzzle2_file = 'input_2.txt'
puzzle_2 = Puzzle_Input(puzzle2_file, 'string')
print(f'Solution for 2a: {puzzle_2.final_position()}')
print(f'Solution for 2b: {puzzle_2.final_position_w_aim()}')
