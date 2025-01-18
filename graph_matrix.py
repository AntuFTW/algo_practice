import numpy as np


class Graph:
    def __init__(self, size: int):
        self.matrix = np.zeros((size, size))

    def add_link(self, src: int, dst: int):
        """src is source and dst is destination"""
        self.matrix[src, dst] = 1

    def get(self, src: int, dst: int):
        return self.matrix[src, dst]


if __name__ == "__main__":
    graph_class = Graph(5)
    print(graph_class.matrix)
    if graph_class.get(1, 2) == 0:
        print(graph_class.get(1, 2))
