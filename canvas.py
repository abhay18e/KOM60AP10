from tkinter import Canvas
from tree import root, height, width

radius =40
no_of_node = width
dis_btw_node = 25
node_verticle_distance = 25
width_px = no_of_node*2*radius + (no_of_node+1)*dis_btw_node
height_px = 2*radius + (height-1)*(radius*2 + node_verticle_distance)
print(height_px, width_px)

# creating canvas
canvas_bg_color = "white"
node_fill_color = "red"
canvas = Canvas(height=height_px, width=width_px, bg=canvas_bg_color)
canvas.pack()


def linspace(start, end, n):
    gap = end-start
    step = gap//(n+1)
    arr = []
    temp = start
    # print(step)
    for i in range(0, n):
        temp += step
        arr.append(temp)
    #print(n, "-->", arr)
    return arr


def drawCircle(x, y, r, text):
    x1 = x-r
    x2 = x+r
    y1 = y-r
    y2 = y+r
    canvas.create_oval(
        x1, y1, x2, y2,outline=node_fill_color, fill=node_fill_color)
    canvas.create_text(x, y, text=text,font=("Purisa", radius//2),fill=canvas_bg_color)


def connectLine(x1, y1, x2, y2):
    canvas.create_line(x1, y1, x2, y2, width=radius//10, fill=node_fill_color)


def setLocOfNodes(root, x, y):
    if root is not None:
        root.loc["x"] = x
        root.loc["y"] = y
        y_next = y + node_verticle_distance + 2*radius

        level = root.level + 1

        basePreorder = 2**level
        positionsForNodes = linspace(0, width_px, basePreorder)
        if root.left is not None:
            preorder = root.left.preorder
            index = preorder - basePreorder
            x_left = positionsForNodes[index]
            setLocOfNodes(root.left, x_left, y_next)
            connectLine(x, y, x_left, y_next)

        if root.right is not None:
            preorder = root.right.preorder
            index = preorder - basePreorder
            x_right = positionsForNodes[index]
            setLocOfNodes(root.right, x_right, y_next)
            connectLine(x, y, x_right, y_next)


def displayNode(root):
    if root is not None:
        drawCircle(root.loc["x"], root.loc["y"], radius, root.data)

        displayNode(root.left)
        displayNode(root.right)


setLocOfNodes(root, width_px/2, radius)
displayNode(root)
canvas.mainloop()
