import numpy as np

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
        if self.type == 'int' and rolling > 0: # Note: following implementation does not work properly - any value > 1
            # instead of a dynamic rolling window
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

    def binary_diagnostics(self, binary_list):
        counts = []
        for i in range(len(binary_list[0])):
            zero = 0
            one = 0
            for binary in binary_list:
                if binary[i] == '0':
                    zero += 1
                else: one += 1
            counts.append([zero, one])
        gamma_rate_binary = ''.join(['1' if x[1] >= x[0] else '0' for x in counts])
        epsilon_rate_binary = ''.join(['0' if x[0] < x[1] else '1' for x in counts])
        co2_scrubber_binary = ''.join(['0' if x[0] <= x[1] else '1' for x in counts])
        return {'gamma_rate_binary': gamma_rate_binary,
                'epsilon_rate_binary': epsilon_rate_binary,
                'co2_scrubber_binary': co2_scrubber_binary
                }

    def find_binaries(self, binary_type):
        binary_list = self.list.copy()
        for i in range(len(binary_list[0])):
            binary = self.binary_diagnostics(binary_list)[binary_type]
            binary_list = list(filter(lambda x: x[i:i+1] == binary[i:i+1], binary_list))
            if len(binary_list) == 1:
                return binary_list[0]
        print(binary_list)

    def power_consumption(self):
        binary_list = self.list.copy()
        rates = self.binary_diagnostics(binary_list)
        gamma_rate = int(rates['gamma_rate_binary'], 2)
        epsilon_rate = int(rates['epsilon_rate_binary'], 2)
        return gamma_rate * epsilon_rate

    def ratings(self):
        oxygen_generator_binary = self.find_binaries('gamma_rate_binary')
        co2_scrubber_binary = self.find_binaries('co2_scrubber_binary')
        print(oxygen_generator_binary)
        print(co2_scrubber_binary)
        oxygen_generator_rate = int(oxygen_generator_binary, 2)
        co2_scrubber_rate = int(co2_scrubber_binary, 2)
        return oxygen_generator_rate * co2_scrubber_rate

# Puzzle 1
puzzle1_file = 'input_1.txt'
#puzzle1 = Puzzle_Input(puzzle1_file, 'int')
#print(f'Solution for 1a: {puzzle1.drop_speed()}')
#print(f'Solution for 1b: {puzzle1.drop_speed(3)}')

# Puzzle 2
puzzle2_file = 'input_2.txt'
#puzzle_2 = Puzzle_Input(puzzle2_file, 'string')
#print(f'Solution for 2a: {puzzle_2.final_position()}')
#print(f'Solution for 2b: {puzzle_2.final_position_w_aim()}')

# Puzzle 3
puzzle3_file = 'input_3.txt'
puzzle3 = Puzzle_Input(puzzle3_file, 'string')
print(f'Solution for 3a: {puzzle3.power_consumption()}')
print(f'Solution for 3b: {puzzle3.ratings()}')
