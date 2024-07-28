from node.state import State
from node.search_number import SearchNumber
from typing import Self

Cost = float


class SearchNode(SearchNumber):
    def __init__(
        self,
        state: State | None = None,
        g: Cost = float("inf"),
        f: Cost = float("inf"),
        parent_id: Self | None = None,
    ):
        self._state: State | None = state
        self._g: Cost = g
        self._f: Cost = f
        self._parent_id: Self | None = parent_id
        self._status: bool = False
        self._priority: int = None
        self._search_number: int = 0

    def get_state(self) -> State | None:
        return self._state

    def set_state(self, state: State) -> None:
        self._state = state

    def get_g(self) -> Cost:
        return self._g

    def set_g(self, g: Cost) -> None:
        self._g = g

    def get_h(self) -> Cost:
        return self._f - self._g

    def get_f(self) -> Cost:
        return self._f

    def set_f(self, f: Cost) -> None:
        self._f = f

    def get_parent(self) -> Self | None:
        return self._parent_id

    def set_parent(self, parent_id: Self) -> None:
        self._parent_id = parent_id

    def get_expanded(self) -> bool:
        return self._status

    def set_expanded(self, status: bool) -> None:
        self._status = status

    def get_priority(self) -> int:
        return self._priority

    def set_priority(self, priority: int) -> None:
        self._priority = priority

    def get_search_number(self) -> int:
        return self._search_number

    def reset(self) -> None:
        self._state = None
        self._g = float("inf")
        self._f = float("inf")
        self._parent_id = None
        self._status = False
        self._priority = 0
        self._search_number = 0

    def __copy__(self):
        raise NotImplementedError("Copying of this class is not allowed")

    def __deepcopy__(self):
        raise NotImplementedError("Deep copying of this class is not allowed")

    def __str__(self) -> str:
        return f"state: {self._state}, g: {self._g}, f: {self._f}"


def compare(a, b) -> bool:
    if a.get_f() < b.get_f():
        return True
    if a.get_f() > b.get_f():
        return False

    if a.get_g() > b.get_g():
        return True
    return False
