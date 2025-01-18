from graph_matrix import Graph
import numpy as np


def breadth_first_search(graph, start, visited):
    queue = [start]
    visited[start] = True
    while len(queue) != 0:
        start = queue[0]
        print(queue.pop(0))
        for i in range(graph.matrix[0, :].size):
            if graph.matrix[start, i] == 1 and not visited[i]:
                visited[i] = True
                queue.append(i)


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

    breadth_first_search(graph, 0, visited)
