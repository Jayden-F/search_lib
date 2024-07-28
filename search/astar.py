class astar[Domain, Expander, Open, Heuristic]:
    def __init__(
        self, domain: Domain, expander: Expander, open: Open, heuristic: Heuristic
    ) -> None:
        self.domain: Domain = domain
        self.expander: Expander = expander
        self.open: Open = open
        self.heuristic: Heuristic = heuristic

    def search(self, start, target):
        self.header()
        self.configuration(start, target)
        edges = []

        start = self.expander.generate_start(*start)
        self.expander.generate_goal(*target)
        self.open.push(start)

        while not self.open.empty():
            node = self.open.pop()
            node.set_expanded(True)

            self.log(node, "expand")

            if self.expander.goal_check(node):
                path = []
                curr = node
                while curr is not None:
                    path.append(curr)
                    curr = curr.get_parent()
                return path[::-1]

            edges.clear()
            self.expander.expand(node, edges)

            for edge in edges:
                if edge.get_expanded():
                    continue

                g = node.get_g() + 1.0
                f = g + self.heuristic(edge.get_state(), target)

                if self.open.contains(edge):
                    if g < edge.get_g():
                        edge.set_g(g)
                        edge.set_f(f)
                        edge.set_parent(node)
                        self.log(edge, "generate")
                        self.open.decrease_key(edge)

                else:
                    edge.set_g(g)
                    edge.set_f(f)
                    edge.set_parent(node)
                    self.log(edge, "generate")
                    self.open.push(edge)

            self.log(node, "close")

        return None

    def log(self, node, type):
        x, y = node.get_state()
        byte, bit = self.domain.index(x, y)
        id = byte * 8 + bit

        pid = None
        if node.get_parent() is not None:
            px, py = node.get_parent().get_state()
            pbyte, pbit = self.domain.index(px, py)
            pid = pbyte * 8 + pbit
        print(
            f"  - {{ type: {type}, id: {id}, g: {node.get_g()}, h: {node.get_h()}, f: {node.get_f()}, x: {x}, y: {y}, pId: {pid} }}"
        )

    def header(self):
        print("""version: 1.4.0
views:
  cell:
    - $: rect
      width: 1
      height: 1
      fill: '#ffff00'
      alpha: 1
      x: ${{ $.x }}
      y: ${{ $.y }}
    - $: rect
      width: 1
      height: 1
      x: ${{ $.x }}
      y: ${{ $.y }}
      alpha: ${{ ($.value / 4) ** 2.2 }}
      fill: '#ff0000'
  main:
    - $: cell
      value: ${{ events.slice(0, step).filter(c=>c.id === $.id).length }}
pivot:
  x: ${{ $.x + 0.5 }}
  y: ${{ $.y + 0.5 }}
  scale: 1
events:""")

    def configuration(self, start, target):
        sx, sy = start
        sbyte, sbit = self.domain.index(sx, sy)
        sid = sbyte * 8 + sbit

        print(f"  - {{ type: source, id: {sid}, x: {sx}, y: {sy} }}")

        tx, ty = target
        tbyte, tbit = self.domain.index(tx, ty)
        tid = tbyte * 8 + tbit

        print(f"  - {{ type: destination, id: {tid}, x: {tx}, y: {ty} }}")
