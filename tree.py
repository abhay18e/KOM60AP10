class tree():
    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right
        self.level = 0
        self.preorder = 1
        self.loc = {"x": 0, "y": 0}

    def insertL(self, data, left=None, right=None):
        newNode = tree(data, left, right)

        self.left = newNode
        self.left.level = self.level + 1
        self.left.preorder = self.preorder * 2
        return self.left

    def insertR(self, data, left=None, right=None):
        newNode = tree(data, left, right)

        self.right = newNode
        self.right.level = self.level + 1
        self.right.preorder = self.preorder * 2 + 1
        return self.right

    def showTree(self, currentNode=None):
        if currentNode == None:
            currentNode = self

        print(" (", end="")

        if currentNode.left != None:
            self.showTree(currentNode.left)

        print(str(currentNode.data+currentNode.loc["x"])+"", end="")

        if currentNode.right != None:
            self.showTree(currentNode.right)

        print(") ", end="")


root = None  # createNodeTree functon creates a tree and assign its value to root


def createNodeTree(value, _root=None):
    global root
    if _root == None:
        _root = tree(value)
        root = _root

    newValue = value // 2

    if newValue >= 1:
        tl = _root.insertL(newValue)
        tr = _root.insertR(newValue)
        createNodeTree(newValue, tl)
        createNodeTree(newValue, tr)
    else:
        return


height = 0  # setHeight functon set height


def setHeight(tree):
    global height
    if tree is not None:
        if height < tree.level:
            height = tree.level
        setHeight(tree.left)
        setHeight(tree.right)
    else:
        return


createNodeTree(16)
# root.right.right.right.right.insertL(45)
setHeight(root)

width = 2**(height-1)

'''  
root.showTree()
print("\n------Height : ", height, "\n-------Width : ", width)
'''
