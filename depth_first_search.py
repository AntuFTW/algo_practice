import numpy as np
from graph_matrix import Graph


def depth_first_search(graph: Graph, start: int, visited: list[bool]):
    """matrix is the 2D adjacent matrix of the graph, start is the starting node number"""
    if visited[start]:
        return
    else:
        visited[start] = True
        print(f'visited {start}')

    for i in range(graph.matrix[start, :].size):
        if graph.get(start, i) == 1:
            depth_first_search(graph, i, visited)

    return


if __name__ == '__main__':
    size = 5

    matrix_in_src = [0, 1, 1, 2, 2, 4, 4]
    matrix_in_dst = [1, 2, 4, 3, 4, 0, 2]

    graph = Graph(size)
    for i, j in zip(matrix_in_src, matrix_in_dst):
        graph.add_link(i, j)

    # graph.add_link(1, 1)
    print(graph.matrix)
    visited = [False] * size

    depth_first_search(graph, 0, visited)
