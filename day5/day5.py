POLYMER = []


# part 1

def is_opposite(left, right):
    return abs(ord(left) - ord(right)) == 32


def add_char_to_polymer(character):
    global POLYMER
    if len(POLYMER) != 0 and is_opposite(character, POLYMER[-1]):
        POLYMER = POLYMER[:-1]
    else:
        POLYMER.append(character)


with open('input.txt', 'r') as f:
    while True:
        char = f.read(1)
        if not char or not char.isalpha():
            break
        add_char_to_polymer(char)

print(len(POLYMER))

# part 2

alpha = "abcdefghijklmnopqrstuvxyz"

with(open('input.txt', 'r')) as f:
    input_data = f.read()
    for character in iter(alpha):
        manipulated_input = input_data.replace(character, '').replace(character.upper(), '')
        POLYMER.clear()
        for char_iterator in iter(manipulated_input):
            if char_iterator.isalpha():
                add_char_to_polymer(char_iterator)
        print(character, ':', len(POLYMER))
