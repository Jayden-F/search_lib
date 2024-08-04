from domain.grid_map import GridMap
from node_pool.node_map import NodeMap
from node.node import SearchNode


SQRT_2 = 2 ** (1 / 2)


class grid_expander[Node: SearchNode, Pool: NodeMap[SearchNode], Domain: GridMap]:
    def __init__(self, domain: Domain, node_pool: Pool):
        self.domain: Domain = domain
        self.node_pool: Pool = node_pool
        self.goal: None | SearchNode = None

    def generate_start(self, x: int, y: int) -> SearchNode:
        start = self.node_pool.generate((x, y))
        start.set_state((x, y))
        start.set_g(0)
        start.set_parent(None)
        return start

    def generate_goal(self, x: int, y: int):
        self.goal = self.node_pool.generate((x, y))

    def goal_check(self, node: SearchNode) -> bool:
        assert node is not None
        assert self.goal is not None

        return node.get_state() == self.goal.get_state()

    def expand(self, node: SearchNode, neighbours: list[SearchNode]):
        assert node is not None
        assert node.get_state() is not None

        x, y = node.get_state()

        assert self.domain.get(x, y)

        state = (x, y + 1)
        if north := self.domain.get(*state):
            node: SearchNode = self.node_pool.generate(state)
            neighbours.append((node, 1))

        state = (x, y - 1)
        if south := self.domain.get(*state):
            node: SearchNode = self.node_pool.generate(state)
            neighbours.append((node, 1))

        state = (x + 1, y)
        if self.domain.get(*state):
            node: SearchNode = self.node_pool.generate(state)
            neighbours.append((node, 1))

            state = (x + 1, y + 1)
            if north and self.domain.get(*state):
                node: SearchNode = self.node_pool.generate(state)
                neighbours.append((node, SQRT_2))

            state = (x + 1, y - 1)
            if south and self.domain.get(*state):
                node: SearchNode = self.node_pool.generate(state)
                neighbours.append((node, SQRT_2))

        state = (x - 1, y)
        if self.domain.get(*state):
            node: SearchNode = self.node_pool.generate(state)
            neighbours.append((node, 1))

            state = (x - 1, y - 1)
            if south and self.domain.get(*state):
                node: SearchNode = self.node_pool.generate(state)
                neighbours.append((node, SQRT_2))

            state = (x - 1, y + 1)
            if north and self.domain.get(*state):
                node: SearchNode = self.node_pool.generate(state)
                neighbours.append((node, SQRT_2))
