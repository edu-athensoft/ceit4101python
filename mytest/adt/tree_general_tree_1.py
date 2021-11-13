"""
general tree

https://blog.csdn.net/romeo12334/article/details/81451698

https://blog.csdn.net/weixin_43314519/article/details/106981900


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


    def __repr__(self):
        return f"Node[data={self.data},children={len(self.children)},node={self.children}]"


class GeneralTree:
    def __init__(self,root=None):
        self.root = root

    def insert(self, parent, node):
        """
        insert a node directly under the parent node
        :param parent:
        :param node:
        :return:
        """
        parent.addChild(node)

    def preorder(self, root):
        """
        recursion
        :param root:
        :return:
        """
        if not root:
            return []
        if not root.children:
            return [root.data]
        result = [root.data]
        for child in root.children:
            result += self.preorder(child)
        return result

    def preorder2(self, root):
        pass


if __name__ == '__main__':
    # create a root node
    root = Node('root')
    print(root)

    # create a node
    node1 = Node('node1')
    node2 = Node('node2')
    node21 = Node('node21')
    node22 = Node('node22')
    node3 = Node('node3')
    node31 = Node('node31')
    node32 = Node('node32')
    node33 = Node('node33')
    node331 = Node('node331')
    node332 = Node('node332')

    # create a tree
    mytree = GeneralTree()
    mytree.insert(root, node1)
    mytree.insert(root, node2)
    mytree.insert(node2, node21)
    mytree.insert(node2, node22)
    mytree.insert(root, node3)
    mytree.insert(node3, node31)
    mytree.insert(node3, node32)
    mytree.insert(node3, node33)
    mytree.insert(node33, node331)
    mytree.insert(node33, node332)
    # print(mytree)

    print(mytree.preorder(root))


