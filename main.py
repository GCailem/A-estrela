import numpy
import numpy as np


class Node:
    def __init__(self, parent=None, position=None):
        self.parent = parent
        self.position = position

        self.g = 0
        self.h = 0
        self.f = 0

    def __eq__(self, other):
        return self.position == other.position


# Função para retornar o caminho (path) que o algoritmo percorreu
# no "mapa.txt" informado.
def return_path(current_node, maze):
    path = []
    no_rows, no_columns = np.shape(maze)

    # here we create the initialized result maze with -1 in every position
    result = [[-1 for i in range(no_columns)] for j in range(no_rows)]
    current = current_node
    while current is not None:
        path.append(current.position)
        current = current.parent

    # Return reversed path as we need to show from start to end path
    path = path[::-1]
    start_value = 0

    # we update the path of start to end found by A-star serch with every step incremented by 1
    for i in range(len(path)):
        result[path[i][0]][path[i][1]] = start_value
        start_value += 1
    return result


def search(maze, cost, start, end):
    # Create start and end node with initized values for g, h and f
    start_node = Node(None, tuple(start))
    start_node.g = start_node.h = start_node.f = 0
    end_node = Node(None, tuple(end))
    end_node.g = end_node.h = end_node.f = 0

    #nodes ainda não visitados pelo algorítmo
    yet_to_visit_list = []

    #nodes já visitados
    visited_list = []

    # node de inicio
    yet_to_visit_list.append(start_node)

    # número máximo de iterações -> evitar ficar preso em loop
    outer_iterations = 0
    max_iterations = (len(maze) // 2) ** 5

    move = [[-1, 0],  # go up
            [0, -1],  # go left
            [1, 0],  # go down
            [0, 1]]  # go right

    # find maze has got how many rows and columns
    no_rows, no_columns = np.shape(maze)

    # Iterações até encontrar o destino
    while len(yet_to_visit_list) > 0:

        # Every time any node is referred from yet_to_visit list, counter of limit operation incremented
        outer_iterations += 1

        # Get the current node
        current_node = yet_to_visit_list[0]
        current_index = 0
        for index, item in enumerate(yet_to_visit_list):
            if item.f < current_node.f:
                current_node = item
                current_index = index

        # Limite de iterações atingido pela aplicação.
        if outer_iterations > max_iterations:
            print("Limite de caminhos atingido.")
            return return_path(current_node, maze)

        # Pop current node out off yet_to_visit list, add to visited list
        yet_to_visit_list.pop(current_index)
        visited_list.append(current_node)

        # test if goal is reached or not, if yes then return the path
        if current_node == end_node:
            return return_path(current_node, maze)

        # Generate children from all adjacent squares
        children = []

        for new_position in move:

            # Get node position
            node_position = (current_node.position[0] + new_position[0], current_node.position[1] + new_position[1])

            # Make sure within range (check if within maze boundary)
            if (node_position[0] > (no_rows - 1) or
                    node_position[0] < 0 or
                    node_position[1] > (no_columns - 1) or
                    node_position[1] < 0):
                continue

            # Make sure walkable terrain
            if maze[node_position[0]][node_position[1]] != 0:
                continue

            # Create new node
            new_node = Node(current_node, node_position)

            # Append
            children.append(new_node)

        # Loop through children
        for child in children:

            # Child is on the visited list (search entire visited list)
            if len([visited_child for visited_child in visited_list if visited_child == child]) > 0:
                continue

            # Create the f, g, and h values
            child.g = current_node.g + cost

            # Cálculo de custo da Heuristic
            child.h = (((child.position[0] - end_node.position[0]) ** 2) +
                       ((child.position[1] - end_node.position[1]) ** 2))

            child.f = child.g + child.h

            # Child is already in the yet_to_visit list and g cost is already lower
            if len([i for i in yet_to_visit_list if child == i and child.g > i.g]) > 0:
                continue

            # Add the child to the yet_to_visit list
            yet_to_visit_list.append(child)


if __name__ == '__main__':
    maze = np.loadtxt('mapa.txt')
    start = [0, 0]  # starting position
    end = [13, 13]  # ending position
    cost = 1  # cost per movement

    path = search(maze, cost, start, end)
    print(np.matrix(path))


    pathMatrix = np.matrix(path)
    with open('path.txt', 'wb') as f:
        for line in pathMatrix:
            np.savetxt(f, line, fmt='%.0f')

