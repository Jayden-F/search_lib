class ManhattanDistance[T]:

    def __init__(self):
        self.name = "manhattan_distance"

    def __call__(self, start: T, target: T) -> float:
        x1, y1 = start
        x2, y2 = target
        return abs(x2 - x1) + abs(y2 - y1)

