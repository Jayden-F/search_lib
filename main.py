from search.astar import astar
from domain.grid_map import GridMap
from expander.grid_4_connected import grid_expander
from open.pyqueue import PriorityQueue
from node.state import State
from node.node import SearchNode, compare
from node_pool.node_map import NodeMap
from heuristic.manhattan_distance import ManhattanDistance


domain: GridMap = GridMap(1000, 1000)
domain.write("test.map")
node_pool: NodeMap[SearchNode] = NodeMap(SearchNode)
expander: grid_expander[SearchNode, NodeMap[SearchNode], GridMap] = grid_expander(
    domain, node_pool
)


open: PriorityQueue[SearchNode] = PriorityQueue(compare)
heuristic: ManhattanDistance[State] = ManhattanDistance()

search = astar(domain, expander, open, heuristic)

start: State = (1, 1)
target: State = (999, 999)

path: list[SearchNode] | None = search.search(start, target)
