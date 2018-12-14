POLYMER = []
count = 0

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
        count += 1
        if not char or not char.isalpha():
            break
        add_char_to_polymer(char)

print(len(POLYMER))
