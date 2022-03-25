from matplotlib import pyplot as plt
from matplotlib.backend_bases import MouseButton
import matplotlib.image as mpimg
from PIL import Image
import os

COUNTER = [0,0]
COORDINATES = [None,None]
IMAGE_NAME = "maze4.png"
X,Y = 0,0

class Node:
    def __init__(self, x, y, parent=None):
        self.x = x
        self.y = y
        self.parent = parent

    def __str__(self):
        return f"({self.x},{self.y})"

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

def search(array,element):
    for i in range(len(array)):
        if array[i] == element:
            return True
    return False

#Solving the maze with bfs
def solve():
    global X
    global Y
    maze = {}
    image = Image.open(IMAGE_NAME)
    image = image.convert('RGB')
    X,Y = image.size[0]-1,image.size[1]-1
    for y in range(image.height):
        for x in range(image.width):
            r,g,b = image.getpixel((x,y))
            if r == 255 and g == 255 and b == 255:
                maze[(x,y)] = " "
            else:
                maze[(x,y)] = "#"
    frontier = [Node(COORDINATES[0][0],COORDINATES[0][1])]
    explored = [Node(COORDINATES[0][0],COORDINATES[0][1])]
    while len(frontier) > 0:
        current = frontier.pop(0)
        if current.x == COORDINATES[1][0] and current.y == COORDINATES[1][1]:
            print(current)
            break
        neighbors = get_neighbors(current,maze)
        for neighbor in neighbors:
            if search(explored, neighbor):
                pass
            else:
                frontier.append(neighbor)
                explored.append(neighbor)
    path = []
    while current.parent is not None:
        path.append(current)
        current = current.parent
    path.reverse()
    os.system("cls")
    print("Path:")
    for node in path:
        print(node,end=" ")
    print()
    for node in path:
        plt.plot(node.x,node.y,'b.', markersize=4)
    fig.canvas.draw()

def get_neighbors(node,maze):
    neighbors = []
    if node.x > 0 and maze[(node.x-1,node.y)] == " ":
        neighbors.append(Node(node.x-1,node.y,node))
    if node.x < X and maze[(node.x+1,node.y)] == " ":
        neighbors.append(Node(node.x+1,node.y,node))
    if node.y > 0 and maze[(node.x,node.y-1)] == " ":
        neighbors.append(Node(node.x,node.y-1,node))
    if node.y < Y and maze[(node.x,node.y+1)] == " ":
        neighbors.append(Node(node.x,node.y+1,node))
    return neighbors

#Setting the starting and ending points
def onclick(event):
    global COUNTER
    global COORDINATES
    global IMAGE_NAME
    if event.button is MouseButton.LEFT and COUNTER[0] == 0:
        circle=plt.Circle((round(event.xdata),round(event.ydata)),.5,color='red')
        ax.add_patch(circle)
        fig.canvas.draw()
        COUNTER[0] = 1
        COORDINATES[0] = (round(event.xdata),round(event.ydata))
    elif event.button is MouseButton.RIGHT and COUNTER[1] == 0:
        plt.plot(round(event.xdata),round(event.ydata),'r+', markersize=12)
        fig.canvas.draw()
        COUNTER[1] = 1
        COORDINATES[1] = (round(event.xdata),round(event.ydata))
    elif event.button is MouseButton.MIDDLE:
        ax.patches = []
        plt.cla()
        img = mpimg.imread(IMAGE_NAME)
        ax.imshow(img)
        ax.set_title('Maze')
        fig.canvas.draw()
        COUNTER = [0,0]
        COORDINATES = [None,None]
    elif COUNTER[0] == 1 and COUNTER[1] == 1:
        solve()

fig, ax = plt.subplots()
ax.set_title("Maze")
img = mpimg.imread(IMAGE_NAME)
ax.imshow(img)
cid = fig.canvas.mpl_connect('button_press_event',onclick)
plt.show()