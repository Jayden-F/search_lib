class ZeroHeuristic[T]:
    def __init__(self):
        self.name = "Zero Heuristic"

    def __call__(self, start: T, target: T) -> float:
        return 0
