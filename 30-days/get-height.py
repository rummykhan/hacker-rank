class Node:
    def __init__(self, data):
        self.right = self.left = None
        self.data = data


class Solution:
    def insert(self, root, data):
        if root == None:
            return Node(data)
        else:
            if data <= root.data:
                cur = self.insert(root.left, data)
                root.left = cur
            else:
                cur = self.insert(root.right, data)
                root.right = cur
        return root

    heights = []
    best_height = None

    def get_height(self, node, height):

        if node.left is not None:
            height += 1
            self.get_height(node.left, height)

        if node.right is not None:
            if node.left is not None:
                height -= 1

            height += 1
            self.get_height(node.right, height)

        if self.best_height is None or height > self.best_height:
            self.best_height = height

    def getHeight(self, root):

        if root is None or root.data is None:
            return 0

        self.get_height(root, 0)

        return self.best_height


T = 7
myTree = Solution()
root = None

for data in [3, 5, 2, 1, 4, 6, 7]:
    root = myTree.insert(root, data)

height = myTree.getHeight(root)

print(height)
