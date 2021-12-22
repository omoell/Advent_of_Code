class Puzzle_Input:
    def __init__(self, filename):
        self.filename = filename
        self.list = self.read()

    def read(self):
        with open(self.filename, 'r') as f:
            content_raw = f.readlines()
            # Clean printed newline
        return [line.replace('\n','') for line in content_raw]

class Comparer:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def a_lgt_b(self):
        return self.a > self.b

# Puzzle 1a
txt_file = 'input_1a.txt'
puzzle_input = Puzzle_Input(txt_file)
results = []
for i in range(1, len(puzzle_input.list)):
    previous = puzzle_input.list[i-1]
    current = puzzle_input.list[i]
    result = Comparer(current, previous).a_lgt_b()
    results.append(result)
    #print(f'{current}  {previous}  {result}')
print(len(puzzle_input.list))
print(len(results))
print(sum(results)) # the correct result was 1451 - instead of 1450 (I do not understand the reason)

# Hilariously short solution from reddit thread
print(sum(x < y for x,y in zip(puzzle_input.list, puzzle_input.list[1:])))