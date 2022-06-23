#-PLAN------------------------------------------------------------------------
# Grid
# Starting point
# Generate maze
    # two lists (stack and visited)
    # add starting point (SP) to visited list
    # check surrounding grid cells around SP (neighbour cells)
    # randomly select one unvisited neighbour cell 
    # add chosen cell to visited list
    # create a link between SP and chosen cell
    # push new location to top of the stack
    # repeat until there are no unvisited cells surrounding current cell
    # if there are no unvisited neighbours 
        # backtrack
        # remove the top value of stack list
        # new top value of stack is the new current location
        # check again for unvisited neighbours
        # if there is unvisited neighbours, repeat steps above
        # if there is no unvisited neighbours, backtrack again
#------------------------------------------------------------------------------

import random, time, pygame

#window measurements
width = 600
height = 600

#colours
black = (0,0,0)
gray = (127,127,127)
white = (255,255,255)
lightPurple = (171,130,255)
darkPurple = (104,34,139)

#pygame initialisation
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Maze Generator")
clock = pygame.time.Clock()

#maze variables
x = 0           # x axis
y = 0           # y axis
w = 20          # width of single cell
grid = []
stack = []
visited = []
GridSize = 9    # size of maze + 1

#building the grid
def BuildGrid(x, y, w):
    for i in range(1,GridSize):
        x = 20
        y = y + 20
        for j in range(1,GridSize):
            pygame.draw.line(screen, white, [x,y],[x + w, y])
            pygame.draw.line(screen, white, [x + w, y], [x + w, y + w])
            pygame.draw.line(screen, white, [x + w, y + w], [x, y + w])
            pygame.draw.line(screen, white, [x, y + w], [x, y])
            grid.append((x,y))
            x = x + 20

#functions animating wall removal
def PushRight(x, y):
    pygame.draw.rect(screen, lightPurple, (x + 1, y + 1, 39, 19), 0)
    pygame.display.update()

def PushLeft(x, y):
    pygame.draw.rect(screen, lightPurple, (x - w + 1, y + 1, 39, 19), 0)
    pygame.display.update()

def PushUp(x, y):
    pygame.draw.rect(screen, lightPurple, (x + 1, y - w + 1, 19, 39), 0)
    pygame.display.update()

def PushDown(x, y):
    pygame.draw.rect(screen, lightPurple, (x + 1, y + 1, 19, 39), 0)
    pygame.display.update()

# current cell
def SingleCell(x, y):
    pygame.draw.rect(screen, darkPurple, (x + 1, y + 1, 18, 18), 0)
    pygame.display.update()


def BacktrackingCell(x, y):
    pygame.draw.rect(screen, lightPurple, (x + 1, y + 1, 18, 18), 0)

#creating the maze
def CreateMaze(x, y):
    SingleCell(x, y)                        # start position of maze
    stack.append((x, y))                    # add starting cell to stack list
    visited.append((x, y))                  # add starting cell to visited list
    while len(stack) > 0:
        time.sleep(.01)                     #alter speed
        cell = []
        if (x + w, y) not in visited and (x + w, y) in grid:
            cell.append("right")

        if (x - w, y) not in visited and (x - w, y) in grid:
            cell.append("left")

        if (x, y + w) not in visited and (x, y + w) in grid:
            cell.append("down")

        if (x, y - w) not in visited and (x, y - w) in grid:
            cell.append("up")

        if len(cell) > 0:
            ChosenCell = (random.choice(cell))
        
            if ChosenCell == "right":
                PushRight(x, y)
                x = x + w
                visited.append((x, y))
                stack.append((x, y))

            elif ChosenCell == "left":
                PushLeft(x, y)
                x = x - w
                visited.append((x, y))
                stack.append((x, y))

            elif ChosenCell == "down":
                PushDown(x, y)
                y = y + w
                visited.append((x, y))
                stack.append((x, y))

            elif ChosenCell == "up":
                PushUp(x, y)
                y = y - w
                visited.append((x, y))
                stack.append((x, y))
        
        else:
            x, y = stack.pop()
            SingleCell(x, y)
            time.sleep(.01)
            BacktrackingCell(x, y)

x, y = 20, 20
BuildGrid(0, 0, 20)
CreateMaze(x, y)

# loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.quit:
            running = False