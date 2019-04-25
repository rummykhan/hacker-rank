class BTreeNode():
    left = None
    right = None
    value = None
    parent = None

    def __init__(self, value):
        self.value = value


def add_node(root, data):
    new_node = BTreeNode(data)

    if root is None:
        return new_node

    parent = None

    current = root

    while current is not None:

        parent = current

        if new_node.value > current.value:
            current = current.right
        else:
            current = current.left

    if new_node.value > parent.value:
        parent.right = new_node
    else:
        parent.left = new_node

    return root


def populate_tree():
    numbers = [10, 5, 5, 19, 39, 20, 1, 100]

    root = None
    for number in numbers:
        root = add_node(root, number)

    return root


def traverse_tree(root, P):
    if root is None:
        return

    print("{} - {}".format(P, root.value))

    traverse_tree(root.left, 'L')
    traverse_tree(root.right, 'R')


if __name__ == '__main__':
    root = populate_tree()
    traverse_tree(root, 'C')
