from math import sqrt


class EuclideanDistance[T]:
    def __init__(self):
        self.name = "euclidean distance"

    def __call__(self, start: T, target: T) -> float:
        x1, y1 = start
        x2, y2 = target
        return sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)
