import string

with open('input.txt', 'r') as f:
    input_lines = f.readlines()
    input_data = [x.strip('\n') for x in input_lines]

#part 1
threes = 0
twos = 0

for line in input_data:
    two_iter = 0
    three_iter = 0
    letter_count = dict.fromkeys(string.ascii_lowercase, 0)

    for alpha in line:
        letter_count[alpha] += 1

    for entry in letter_count:
        if letter_count[entry] == 2 and two_iter == 0:
                two_iter += 1
                twos += 1
        elif letter_count[entry] == 3 and three_iter == 0:
                three_iter += 1
                threes += 1

print(twos * threes)

# part 2

found = False
for outer in range(len(input_data)):
    for inner in range(len(input_data)):
        if inner != outer and not found:
            error_count = 0
            for x in range(len(input_data[outer])):
                if input_data[outer][x] != input_data[inner][x]:
                        error_count += 1
            if error_count <= 1:
                in_common = list(filter(lambda x: x in input_data[inner], input_data[outer]))
                in_common_str = ''.join(in_common)
                print(in_common_str)
                found = True
