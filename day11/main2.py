from collections import defaultdict

directions = {
        direction
        for row in (-1, 0, 1)
        for col in (-1, 0, 1)
        if (direction := row + col*1j)
}

def get_direct_neighbours(seats, unused):
    neighbours = {
            seat: [
                neighbour
                for direction in directions
                if (neighbour := seat + direction) in seats
            ]
            for seat in seats
    }
    return neighbours

def get_indirect_neighbours(seats, size):
    neighbours = defaultdict(list)
    for seat in seats:
        for direction in directions:
            neighbour = seat + direction
            while 0 <= neighbour.real < size and 0 <= neighbour.imag < size:
                if neighbour in seats:
                    neighbours[seat].append(neighbour)
                    break
                neighbour += direction
    return neighbours

def solve(file_path, neighbour_fn, limit):
    with open(file_path) as f:
        text = f.read()
    lines = text.splitlines()

    seats = {
            row + col*1j: False
            for row, line in enumerate(lines)
            for col, char in enumerate(line)
            if char == "L"
    }
    size = len(lines)
    neighbours = neighbour_fn(seats, size)

    while True:
        new_seats = {}
        for seat, occupied in seats.items():
            count = (seats[neighbour] for neighbour in neighbours[seat])
            new_seats[seat] = sum(count) < limit if occupied else not any(count)

        if seats == new_seats:
            return sum(new_seats.values())

        seats = new_seats

assert solve("test.txt", get_direct_neighbours, 4) == 37
print(solve("input.txt", get_direct_neighbours, 4))
print(solve("input.txt", get_indirect_neighbours, 5))
