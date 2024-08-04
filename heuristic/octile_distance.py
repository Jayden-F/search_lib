D = 1
D2 = 2 ** (1 / 2)

class OctileDistance[T]:
    def __init__(self):
        self.name = "octile distance"

    def __call__(self, start: T, target: T) -> float:
        x1, y1 = start
        x2, y2 = target
        dx = abs(x1 - x2)
        dy = abs(y1 - y2)
        return D * (dx + dy) + (D2 - 2 * D) * min(dx, dy)
