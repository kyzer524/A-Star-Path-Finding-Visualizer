import pygame
import math
from queue import PriorityQueue

# setting up the window
width = 900
window = pygame.display.set_mode((width, width))
pygame.display.set_caption("A* Path-Finding Algorithm")

# colour library
red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 255, 0)
cyan = (0, 255, 255)
yellow = (255, 255, 0)
white = (255, 255, 255)
black = (0, 0, 0)
purple = (128, 0, 128)
orange = (255, 165, 0)
grey = (128, 128, 128)
turquoise = (64, 224, 208)


# making a grid
class Block:
    def __init__(self, row, col, width, total_rows):
        self.row = row
        self.col = col
        self.width = width
        self.x = row * width
        self.y = col * width
        self.colour = white
        self.neighbors = []
        self.total_rows = total_rows

    # gets the positioning
    def get_pos(self):
        return self.row, self.col

    # modules intialised to return color of block
    def make_start(self):
        return self.colour == yellow

    def is_closed(self):
        return self.colour == red

    def is_open(self):
        return self.colour == green

    def is_barrier(self):
        return self.colour == black

    def is_start(self):
        return self.colour == yellow

    def is_end(self):
        return self.colour == turquoise

    def reset(self):
        self.colour == white

    # modules intialised to assign color to each block
    def make_closed(self):
        self.colour = red

    def make_open(self):
        self.colour = green

    def make_barrier(self):
        self.colour = black

    def make_end(self):
        self.colour = turquoise

    def make_path(self):
        self.colour = cyan

    # draws the rectangle window where the alogorithm runs
    def draw(self, window):
        pygame.draw.rect(window, self.colour, (self.x, self.y, self.width, self.width))

    # solve later
    def update_neighbors(self, grid):
        pass

    # solve later
    def __lt__(self, other):
        return False


# manhattan heuristic used
# can't we just use the Pythagoras formula??
# what about euclidean heuristic
def h(p1, p2):
    p1 = x1, y1
    p2 = x2, y2
    return abs(x1 - x2) + abs(y1 - y2)


# pass block class into the grid
def make_grid(rows, width):
    grid = []
    gap = width // rows
    for i in range(rows):
        grid.append([])
        for j in range(rows):
            block = Block(i, j, gap, rows)
            grid[i].append(block)

    return grid


# grid is now made


# drawing the grid lines for the grid
def draw_grid(window, rows, width):
    gap = width // rows
    for i in range(rows):
        pygame.draw.line(window, grey, (0, i * gap), (width, i * gap))
    # no need for this ?
    # for j in range(rows):
    # pygame.draw.line(window, grey, (j * gap, 0), (j * gap, width))


# draws everthing else
def draw(window, grid, rows, width):
    # paint the entire window white
    window.fill(white)

    # draws all of the spots on top of the grid
    for row in grid:
        for block in row:
            block.draw(window)

    draw_grid(window, rows, width)
    pygame.display.update()


def hget_clicled_pos(pos, rows, width):
    gap = width // rows
    y, xx = pos

    row = y // gap
    col = x // gap

    return row, col


# core heart of the algorithm
def main(win, width):
    rows = 70
    grid = make_grid(rows, width)

    start = None
    end = None

    run = True
    started = True

    while run:
        draw(window, grid, rows, width)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

            if started:
                continue
                # prevents any misclicks while algorithm is running

                if pygame.mouse.get_pressed()[0]:  # LEFT mouse button
                    pos = pygame.mouse.get_pos()
                    row, col = get_clikced_pos(pos, ROWS, width)
                    block = grid[row][col]

                    if not start:
                        start = block
                        start.make_start
                    # can combine line 175 with 176 maybe

                    elif not end:
                        end = block
                        end.make_end()

                    elif block != end and block != start:
                        spot.make_barrier()


                elif pygame.mouse.get_pressed()[2]:  # RIGHT mouse button
                    pass
        pygame.quit()


main(window, width)
