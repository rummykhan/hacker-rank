class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class Solution:
    def insert(self, head, data):
        p = Node(data)
        if head == None:
            head = p
        elif head.next == None:
            head.next = p
        else:
            start = head
            while (start.next != None):
                start = start.next
            start.next = p
        return head

    def display(self, head):
        current = head
        while current:
            print(current.data, end=' ')
            current = current.next

    def removeDuplicates(self, head):
        duplicates = {}

        current = head

        while current is not None:

            if current.data not in duplicates:
                duplicates[current.data] = 0

            duplicates[current.data] += 1

            current = current.next

        current = head

        while current.next is not None:

            if current.next.data in duplicates and duplicates[current.next.data] > 1:

                duplicates[current.next.data] -= 1

                if current.next.next is None:
                    current.next = None
                else:
                    current.next = current.next.next
            else:
                current = current.next

        print(' '.join('{}'.format(key) for key, value in duplicates.items()))


# iterate over link list
# if current.next >  1
# then current =  current.next.next
# else
# current = current.next

mylist = Solution()
T = int(6)
head = None
for data in [1, 2, 2, 3, 3, 4]:
    head = mylist.insert(head, data)
head = mylist.removeDuplicates(head)
mylist.display(head)
