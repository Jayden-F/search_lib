from bitarray import bitarray
from random import random


class GridMap:
    def __init__(self, width: int, height: int) -> None:
        self.width: int = width
        self.height: int = height

        self.padded_width_bytes = width // 8 + 1
        self.padded_width_bits = self.padded_width_bytes * 8
        bits = self.padded_width_bits * (height + 2) + 8
        bytes = 8 + bits // 8 + 8
        self.grid = bitarray(bytes * 8)
        self.grid.setall(0)

        for i in range(width):
            for j in range(height):
                if random() <= 0.0:
                    self.set(i, j, 0)
                else:
                    self.set(i, j, 1)

    def get_width(self) -> int:
        return self.width

    def get_height(self) -> int:
        return self.height

    def set(self, x: int, y: int, value):
        bit = self.index(x, y)
        self.grid[bit] = value

    def get(self, x: int, y: int):
        bit = self.index(x, y)
        return self.grid[bit] != 0

    def index(self, x: int, y: int):
        padded_y = y + 1
        padded_x = x + 1
        bit = padded_x % 8
        byte = (padded_x // 8 + padded_y * self.padded_width_bytes) + 8
        return byte * 8 + bit

    def write(self, name):
        with open(name, "w") as f:
            f.write("type octile\n")
            f.write(f"height {self.height}\n")
            f.write(f"width {self.width}\n")
            f.write(f"map\n")
            for i in range(self.height):
                row = ""
                for j in range(self.width):
                    row += str(["T", "."][self.get(j, i)])
                f.write(row + "\n")
