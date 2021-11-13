"""
tree

https://blog.csdn.net/xuelians/article/details/79999284

"""

class TreeNode:
    def __int__(self, data, parent=None):
        self.data = data
        self.parent = parent
        self.children = []

    def setParent(self, node):
        self.parent = node

    def addChild(self, childNode):
        pass


if __name__ == '__main__':
    root = TreeNode()



