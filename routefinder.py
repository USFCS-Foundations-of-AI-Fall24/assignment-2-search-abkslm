from queue import PriorityQueue
import Graph

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
    closed_list = {}
    search_queue.put(start_state)
    ## you do the rest.


## default heuristic - we can use this to implement uniform cost search
def h1(state) :
    return 0

## you do this - return the straight-line distance between the state and (1,1)
def sld(state) :
    sqt(a^ + b2)
    pass

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