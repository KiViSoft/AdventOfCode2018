from functools import reduce

# part 1
with open('input.txt', 'rb') as f:
    input_lines = f.readlines()
    input_data = [int(x) for x in input_lines]
    print(reduce(lambda x, y: x + y, input_data))

# part 2
freq = 0
freqs = set()

while True:
    found = False
    for val in input_data:
        freq += val
        if freq not in freqs:
            freqs.add(freq)
        else:
            print(freq)
            found = True
            break
    if found:
        break
