from typing import Protocol


class SearchNumber(Protocol):
    def get_search_number(self) -> int:
        """method to get the search_number (index) of the element."""
        ...

    def set_search_number(self, search_number: int) -> None:
        """method to set the search_number (index) of the element."""
        ...

    def reset(self) -> None: ...
