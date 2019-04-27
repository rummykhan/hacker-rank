import sys


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

    queue = {}

    def get_elements(self, root, index):

        if index not in self.queue:
            self.queue[index] = []

        if root.left is not None:
            self.queue[index].append(root.left.data)

        if root.right is not None:
            self.queue[index].append(root.right.data)

        if root.left is not None:
            index += 1
            self.get_elements(root.left, index)

        if root.right is not None:

            if root.left is None:
                index += 1
            self.get_elements(root.right, index)

    def levelOrder(self, root):

        self.get_elements(root, 0)

        output = [root.data]
        for k, v in self.queue.items():
            output += v

        print(' '.join(str(x) for x in output))


myTree = Solution()
root = None
for data in [20, 50, 35, 44, 9, 15, 62, 11, 13]:
    root = myTree.insert(root, data)

myTree.levelOrder(root)
