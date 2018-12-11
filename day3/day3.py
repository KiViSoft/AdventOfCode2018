# part 1

class Coordinates2D(object):
    def __init__(self, ix: int, iy: int) -> None:
        self.x = ix
        self.y = iy

    def __str__(self):
        return str(self.x) + ',' + str(self.y)

    def __eq__(self, other):
        if self.x == other.x and self.y == other.y:
            return True

    def __hash__(self):
        return hash((self.x, self.y))


class SmallRect(object):
    def __init__(self, iid: int, ix: int, iy: int, iw: int, ih: int) -> None:
        self.id = iid
        self.x = ix
        self.y = iy
        self.w = iw
        self.h = ih
        self.left = self.x
        self.right = self.x + self.w
        self.top = self.y
        self.bottom = self.y + self.h

    def __str__(self):
        return str(self.x) + " " + str(self.y) + " " + str(self.w) + " " + str(self.h)

    def __repr__(self):
        return str(self.x) + " " + str(self.y) + " " + str(self.w) + " " + str(self.h)

    def __eq__(self, other):
        return self.id == other.id

    def intersects(self, other):
        if self != other:
            # https://developer.mozilla.org/kab/docs/Games/Techniques/2D_collision_detection
            if self.x < other.right and self.right > other.x and self.y < other.bottom and self.bottom > other.y:
                return True
        return False


def parse_data(input_data):
    id = input_data[input_data.find('#') + 1: input_data.find(' ')]
    x = input_data[input_data.find('@') + 1: input_data.find(',')]
    y = input_data[input_data.find(',') + 1: input_data.find(':')]
    w = input_data[input_data.find(':') + 1: input_data.find('x')]
    h = input_data[input_data.find('x') + 1:]
    return int(id), int(x), int(y), int(w), int(h)

with open('input.txt', 'r') as f:
    input_lines = f.readlines()
    input_lines = [x.strip() for x in input_lines]
    squares = list(map(lambda x: SmallRect(*parse_data(x)), input_lines))

overlapped_claims = set()

for i_index in range(len(squares)):
    for j_index in range(len(squares)):
        if squares[i_index].intersects(squares[j_index]):
            # https://stackoverflow.com/questions/27152904/calculate-overlapped-area-between-two-rectangles
            x_coord = max(squares[i_index].x, squares[j_index].x)
            y_coord = max(squares[i_index].y, squares[j_index].y)
            width = min(squares[i_index].right, squares[j_index].right) - x_coord
            height = min(squares[i_index].bottom, squares[j_index].bottom) - y_coord

            for h in range(height):
                for w in range(width):
                    coord = Coordinates2D(w+x_coord, h+y_coord)
                    if coord != Coordinates2D(0, 0):
                        overlapped_claims.add(coord)

print(len(overlapped_claims))

# part 2

overlaps = False

for i_index in range(len(squares)):
    for j_index in range(len(squares)):
        if squares[i_index].intersects(squares[j_index]):
            overlaps = True
            j_index = 0
            break
    if overlaps:
        overlaps = False
    else:
        print(squares[i_index].id)
