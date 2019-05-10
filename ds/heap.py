def swap_element(arr: [], index_1: int, index_2: int) -> []:
    tmp = arr[index_1]
    arr[index_1] = arr[index_2]
    arr[index_2] = tmp

    return arr


def get_parent(index) -> int:
    if (index - 2) % 2 == 0:
        return (index - 2) // 2

    return (index - 1) // 2


def get_right_index(index):
    return (index * 2) + 2


def get_left_index(index):
    return (index * 2) + 1


def get_val(heap, index):
    if len(heap) >= index:
        return heap[index]

    return -1


def heapify(heap, index):
    if len(heap) == 1:
        return heap

    while index > 0 and heap[index] > get_val(heap, get_parent(index)):
        heap = swap_element(heap, index, get_parent(index))
        index = get_parent(index)

    return heap


def max_heapify(heap, index):
    left = get_left_index(index)
    right = get_right_index(index)
    largest = index

    if left <= len(heap) and heap[largest] < heap[left]:
        largest = left

    if right <= len(heap) and heap[largest] < heap[right]:
        largest = right

    if largest is not index:
        heap = swap_element(heap, index, largest)
        return max_heapify(heap, largest)

    return heap


def extract(heap, index):
    current_index = 0
    heap[current_index] = get_val(heap, index)

    return max_heapify(heap, current_index)


def start():
    arr = [15, 18, 20, 25, 27, 53, 1]
    heap = []
    index = 0

    for value in arr:
        # insert O(1)
        heap.append(value)

        # Heapify O(Log N)
        heap = heapify(heap, index)

        index += 1

    print(heap)

    for x in range(1, 3):
        print('{} - {}'.format(index, heap))
        heap = extract(heap, index - 1)
        del heap[index - 1]
        index -= 1

    print(heap)


if __name__ == '__main__':
    start()
