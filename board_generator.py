from random import randint

def generate(grid_size):
    grid_size = int(grid_size)
    grid = [[0]*grid_size for i in range(grid_size)]
    return grid

def populate(grid_size, gems, dragons):
    pass


if __name__ == "__main__":
    grid = generate(10)
    for line in grid:
        print(line)