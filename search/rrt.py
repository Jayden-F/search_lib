from node.node import SearchNode
from utils.kdtree import KDTree
from random import randrange


Point = tuple[int, ...]


class RRT[Domain, NodePool, Heuristic]:
    def __init__(self, domain: Domain, node_pool: NodePool, heuristic: Heuristic):
        self.domain: Domain = domain
        self.node_pool: NodePool = node_pool
        self.heuristic: Heuristic = heuristic

    def search(self, start, target, iterations: int):
        self.header()
        self.configuration(start, target)
        kd_tree = KDTree([], 2)
        kd_tree.add_point(start)

        k = 0

        while k < iterations:
            new_point: Point = self.random_point()
            new_node: SearchNode = self.node_pool.generate(new_point)

            (
                distance,
                closest_point,
            ) = kd_tree.get_nearest(new_point, True)
            closest_node: SearchNode = self.node_pool.generate(closest_point)
            self.log(closest_node, "expanding")

            new_node.set_parent(closest_node)
            new_node.set_g(closest_node.get_g() + distance)
            kd_tree.add_point(new_point)
            self.log(new_node, "generating")

            if self.heuristic(new_point, target) < 8:
                path = []
                curr = new_node
                while curr is not None:
                    path.append(curr)
                    curr = curr.get_parent()
                return path[::-1]

            self.log(closest_node, "closing")

        return None

    def random_point(self) -> Point:
        x = randrange(0, self.domain.get_width())
        y = randrange(0, self.domain.get_height())
        return (x, y)

    def log(self, node, type):
        x, y = node.get_state()
        id = self.domain.index(x, y)

        pid = None
        if node.get_parent() is not None:
            px, py = node.get_parent().get_state()
            pid = self.domain.index(px, py)
        print(
            f"  - {{ type: {type}, id: {id}, g: {node.get_g()}, h: {node.get_h()}, f: {node.get_f()}, x: {x}, y: {y}, pId: {pid} }}"
        )

    def header(self):
        print("""version: 1.4.0
views:
  node:
    - $: circle
      radius: 1
      x: ${{ $.x }}
      y: ${{ $.y }}
      fill: ${{ color[$.type] }}
  line:
    - $: path
      points:
        - x: ${{ parent.x }}
          y: ${{ parent.y }}
        - x: ${{ $.x }}
          y: ${{ $.y }}
      fill: ${{ color[$.type] }}
      lineWidth: 1
      $if: ${{ !!parent }}
  main:
    - $: node
    - $: line
pivot:
  x: ${{ $.x + 0.5 }}
  y: ${{ $.y + 0.5 }}
  scale: 3
events:
  """)

    def configuration(self, start, target):
        sx, sy = start
        sid = self.domain.index(sx, sy)

        print(f"  - {{ type: source, id: {sid}, x: {sx}, y: {sy} }}")

        tx, ty = target
        tid = self.domain.index(tx, ty)

        print(f"  - {{ type: destination, id: {tid}, x: {tx}, y: {ty} }}")
