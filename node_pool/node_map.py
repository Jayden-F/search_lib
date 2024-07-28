from node.search_number import SearchNumber
from node.state import State
from typing import Callable


class NodeMap[T: SearchNumber]:
    def __init__(self, factory: Callable[..., T]):
        self.search_number = 0
        self.nodes: dict[State, T] = dict()
        self.factory: Callable[..., T] = factory

    def generate(self, state: State) -> T:
        if state not in self.nodes:
            node: T = self.factory()
            node.set_search_number(self.search_number)
            node.set_state(state)
            self.nodes[state] = node
            return node

        node = self.nodes[state]
        assert node.get_state() == state
        if node.get_search_number() != self.search_number:
            node.reset()
        return node

    def reset(self) -> None:
        self.search_number += 1

    def metrics(self) -> int:
        return len(self.nodes)
