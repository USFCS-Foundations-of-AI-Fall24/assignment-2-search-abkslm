from queue import PriorityQueue
import Graph
from math import sqrt

class map_state() :
    ## f = total estimated cost
    ## g = cost so far
    ## h = estimated cost to goal
    def __init__(self, location="", mars_graph=None,
                 prev_state=None, g=0,h=0):
        self.location = location
        self.mars_graph = mars_graph
        self.prev_state = prev_state
        self.g = g
        self.h = h
        self.f = self.g + self.h

    def __eq__(self, other):
        return self.location == other.location

    def __hash__(self):
        return hash(self.location)

    def __repr__(self):
        return "(%s)" % (self.location)

    def __lt__(self, other):
        return self.f < other.f

    def __le__(self, other):
        return self.f <= other.f

    def is_goal(self):
        return self.location == '1,1'


def a_star(start_state, heuristic_fn, goal_test, use_closed_list=True) :
    search_queue = PriorityQueue()
    closed_list = set() if use_closed_list else None
    search_queue.put((start_state.f, start_state))

    while not search_queue.empty():
        current_f, current_state = search_queue.get()
        
        if goal_test(current_state):
            path = []
            while current_state:
                path.append(current_state)
                current_state = current_state.prev_state
            return path[::-1]
        
        if use_closed_list:
            closed_list.add(current_state)

        for edge in current_state.mars_graph.get_edges(current_state.location):
            neighbor = edge.dest

            g_cost = current_state.g + edge.val
            h_cost = heuristic_fn(neighbor)
            neighbor_state = map_state(
                location=neighbor,
                mars_graph=current_state.mars_graph,
                prev_state=current_state,
                g=g_cost,
                h=h_cost
               )

            if use_closed_list and neighbor_state in closed_list:
                continue

            search_queue.put((neighbor_state.f, neighbor_state))

    return None


## default heuristic - we can use this to implement uniform cost search
def h1(state) :
    return 0

## you do this - return the straight-line distance between the state and (1,1)
def sld(state) :
    goal_position = (1, 1)

    if not state.location:
        current_position = (0, 0)
    else:
        current_position = tuple(map(int, state.location.split(',')))


    return sqrt((current_position[0] - goal_position[0]) ** 2 + (current_position[1] - goal_position[1]) ** 2)

## you implement this. Open the file filename, read in each line,
## construct a Graph object and assign it to self.mars_graph().
def read_mars_graph(filename, map_state):
    graph = Graph.Graph()

    with open(filename, 'r') as file:
        for line in file:
            key, values = line.strip().split(':')
            key_tuple = tuple(map(int, key.split(',')))
            value_list = [tuple(map(int, value.split(','))) for value in values.strip().split()]

            graph.add_node(key_tuple)
            for value in value_list:
                edge = Graph.Edge(key_tuple, value)
                graph.add_edge(edge)

    map_state.mars_graph = graph
    return graph


if __name__ == "__main__":
    test_map_state = map_state()
    read_mars_graph("MarsMap", test_map_state)
    print(test_map_state)