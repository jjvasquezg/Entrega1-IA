from Util import print_route

import time
import heapq

class Node:
    def __init__(self, position, parent=None, cost = 0, path_cost=0):
        self.position = position
        self.parent = parent
        self.cost = cost
        self.path_cost = path_cost

    def __lt__(self, other):
        return self.path_cost < other.path_cost

class Problem:
    def __init__(self, initial, goal, actions):
        self.initial = initial
        self.goal = goal
        self.actions = actions

def reconstruct_path(node):
    path = []
    path_cost = []
    while node:
        path.append(node.position)
        path_cost.append(node.path_cost)
        node = node.parent
    path.reverse()
    path_cost.reverse()
    return path, path_cost

def manhatan_distance(pos, goal):
        return (abs(pos[0] - goal[0]) + abs(pos[1] - goal[1]))

def get_neighbors(pos):
    neighbors = []
    movements = []
    for key in problem.actions.keys():
        move = problem.actions[key]  
        neighbor = (pos[0] + move[0], pos[1] + move[1])
        if grid[neighbor[0]][neighbor[1]] != "#" and neighbor != pos:
            movements.append(key)
            neighbors.append(neighbor)
    return neighbors

def find_exit():

    start_node = Node(start, path_cost=0)
    frontier = [(manhatan_distance(start, goal), start_node)]
    heapq.heapify(frontier) #Convierte la lista frontier en una cola de prioridad (heap)
    reached = {start: start_node}

    while frontier:
        _, node = heapq.heappop(frontier)
        if node.position == goal:
            return reconstruct_path(node)

        for neighbor in get_neighbors(node.position):
            if grid[neighbor[0]][neighbor[1]] == "▲":
                node_cost = 3
                new_cost = node.path_cost + 3
            else:
                node_cost = 1
                new_cost = node.path_cost + 1
            if neighbor not in reached or new_cost < reached[neighbor].path_cost:
                reached[neighbor] = Node(neighbor, parent=node, cost=node_cost, path_cost=new_cost)
                heapq.heappush(frontier, (manhatan_distance(neighbor, goal)+new_cost, reached[neighbor]))

    return None  # No se encontró salida

start = (5, 1)
goal = (3, 6)

grid = [
    ['#', '#', '#', '#', '#', '#', '#', '#'],
    ['#', '▲', ' ', '▲', '▲', ' ', '#', '#'],
    ['#', '#', ' ', ' ', '▲', '▲', ' ', '#'],
    ['#', ' ', ' ', '▲', '#', '#', 'E', '#'],
    ['#', ' ', '▲', ' ', '#', ' ', '▲', '#'],
    ['#', 'S', '▲', '▲', '▲', ' ', '▲', '#'],
    ['#', '#', ' ', '▲', ' ', '#', '#', '#'],
    ['#', '#', '#', '#', '#', '#', '#', '#'],
]

actions = {
        'up' : [-1,0],
        'down' : [1,0],
        'right' : [0,1],
        'left' : [0,-1],
        'upper_right' : [-1,1],
        'upper_left' : [-1,-1],
        'lower_right' : [1,1],
        'lower_left' : [1,-1]
}

start_time = time.perf_counter()
problem = Problem(start, goal, actions)
solution = find_exit()
end_time = time.perf_counter()
if solution:
    final_time = f"This solution was found in: {(end_time - start_time)*1000:.8f} milliseconds"
    key = input("A solution was found.\nPress enter to continue with the route animation: ")
    if key == "":
        print_route(grid, solution, final_time)
else:
    print("There's no solution for this problem")
