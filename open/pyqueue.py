from typing import Callable, Protocol


class priority_id(Protocol):
    def get_priority(self) -> int:
        """method to get the priority (index) of the element."""
        ...

    def set_priority(self, priority: int) -> None:
        """method to set the priority (index) of the element."""
        ...


class PriorityQueue[T: Priority_ID]:
    def __init__(self, compare_fn: Callable[[T, T], bool] = lambda a, b: a < b) -> None:
        self.heap: list[T] = []
        self.size: int = 0
        self.compare_fn: Callable[[T, T], bool] = compare_fn

    def swap(self, index_1: int, index_2: int) -> None:
        self.heap[index_1], self.heap[index_2] = self.heap[index_2], self.heap[index_1]
        self.heap[index_1].set_priority(index_1)
        self.heap[index_2].set_priority(index_2)

    def sift_up(self, index: int) -> None:
        while index > 0:
            p_index: int = index - 1 >> 1

            if self.compare_fn(self.heap[index], self.heap[p_index]):
                self.swap(index, p_index)
                index = p_index
            else:
                break

    def sift_down(self, index: int) -> None:
        first_leaf_index: int = self.size >> 1
        while index < first_leaf_index:
            left: int = (index << 1) + 1
            right: int = left + 1
            which: int = left

            if right < self.size and self.compare_fn(self.heap[right], self.heap[left]):
                which = right

            if self.compare_fn(self.heap[which], self.heap[index]):
                self.swap(index, which)
                index = which
            else:
                break

    def build_heap(self, elements: list[T]) -> None:
        self.heap = elements
        self.size = len(elements)

        first_leaf_index = self.size >> 1
        for index in range(first_leaf_index, -1, -1):
            self.sift_down(index)

    def increase_key(self, value: T) -> None:
        self.sift_down(value.get_priority())

    def decrease_key(self, value: T) -> None:
        self.sift_up(value.get_priority())

    def contains(self, value: T) -> bool:
        index: int = value.get_priority()
        if index is None:
            return False
        return index is not None and index < self.size and value == self.heap[index]

    def push(self, value: T) -> None:
        if self.contains(value):
            return None

        self.heap.append(value)
        assert self.heap[self.size] == value
        self.heap[self.size].set_priority(self.size)
        self.sift_up(self.size)
        self.size += 1

    def pop(self) -> T | None:
        if self.size == 0:
            return None

        self.swap(0, self.size - 1)
        self.size -= 1
        self.sift_down(0)

        return self.heap.pop()

    def peek(self) -> T | None:
        if self.size == 0:
            return None

        return self.heap[0]

    def length(self) -> int:
        return self.size

    def empty(self) -> bool:
        return self.length() == 0

    def clear(self) -> None:
        self.size = 0


if __name__ == "__main__":
    test = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
    pqueue = pyqueue[int]()
    pqueue.build_heap(test)

    while not pqueue.empty():
        print(pqueue.pop())
