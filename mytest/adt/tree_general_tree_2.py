"""
general tree
"""

"""
A-B1-C1
 -B2-C2
 -B2-C3-D1
 -B2-C3-D2
 -B3-C4
 -B3-C5
"""


class Node:
    def __init__(self, data=None):
        self.data = data
        self.children = []

    def getChildren(self):
        return self.children

    def getChildrenQty(self):
        return len(self.children)

    def addChild(self, child):
        self.children.append(child)

    def removeChild(self, child):
        self.children.remove(child)

    def isLeaf(self):
        if len(self.children) == 0:
            return True
        else:
            return False

    def __repr__(self):
        # return f"Node[data={self.data},children={len(self.children)},node={self.children}]"
        # return f"Node[data={self.data}]"
        return f"{self.data}"


class Tree:
    def __init__(self, root):
        self.root = root
        self.paths = []

    def insert(self, parent, node):
        parent.addChild(node)

    def getPath(self):
        path = []
        path.append(self.root)

        # get children
        children_stacks = [root.getChildren()]
        # print("children_stacks=",children_stacks)

        # add children to path
        while len(children_stacks) > 0:
            children_stack = children_stacks[-1]
            # print("children_stack=",children_stack)
            while len(children_stack) > 0:
                # print("children_stack=",children_stack)
                child = children_stack.pop()
                path.append(child)
                # print("path=",path)

                # print("child=",child, child.isLeaf())
                if not child.isLeaf():
                    children_stacks.append(child.getChildren())
                    # print("children_stacks=",children_stacks)
                    # path.pop()

                else:
                    self.paths.append(path.copy())
                    path.pop()
            else:
                if len(path)==0:
                    path.pop()


            # children_stack = path.pop().getChildren()

        return self.paths


# create a root node
root = Node('A')

b1 = Node('B1')
b2 = Node('B2')
b3 = Node('B3')

c1 = Node('C1')
c2 = Node('C2')
c3 = Node('C3')
c4 = Node('C4')
c5 = Node('C5')

d1 = Node('D1')
d2 = Node('D2')


# create a tree
mytree = Tree(root)
mytree.insert(root, b1)
mytree.insert(root, b2)
mytree.insert(root, b3)
mytree.insert(b1, c1)
mytree.insert(b2, c2)
mytree.insert(b2, c3)
mytree.insert(b3, c4)
mytree.insert(b3, c5)
mytree.insert(c3, d1)
mytree.insert(c3, d2)

paths = mytree.getPath()
for path in paths:
    print(path)

