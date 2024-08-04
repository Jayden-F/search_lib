
class PerfectHeuristic[T]:

    def __init__(self, domain):
        self.name = "perfect_heuristic"
        self.state_to_index = dict()
        self.curr_index = None
        self.lookup_table = list()
        self.domain = domain
        self.grid_expander =

    def __call__(self, start: T, target: T) -> float:
        x1, y1 = start
        x2, y2 = target
        return abs(x2 - x1) + abs(y2 - y1)


    def set_target(self, target):

