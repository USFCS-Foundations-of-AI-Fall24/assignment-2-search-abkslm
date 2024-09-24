import antennae_freqs, mars_planner, routefinder
from search_algorithms import depth_first_search, breadth_first_search
from routefinder import sld, h1

def print_green(print_str: str):
    print("\033[92m" + print_str + "\033[0m")

def demo_antennae_freqs():
    antennae_freqs.main()

def demo_mars_planner(decomposed: bool, search_func=breadth_first_search, limit: int=0):
    print(mars_planner.main(decomposed, search_func, limit))

def demo_routefinder(heuristic=sld):
    print(routefinder.main(heuristic=heuristic))

if __name__ == '__main__':

    print_green("Running \"demo_antennae_freqs()\"")
    demo_antennae_freqs()
    print_green("Finished \"demo_antennae_freqs()\"\n")

    print_green("\nRunning \"demo_mars_planner()\"")
    ## You can play with the parameters here
    # decomposed= True/False
    # search_func= depth_first_search/breadth_first_search
    # limit= dfs limit, ignored when bfs is used as search_func
    demo_mars_planner(decomposed=True, search_func=depth_first_search, limit=10)
    print_green("Finished \"demo_mars_planner()\"\n")

    print_green("\nRunning \"demo_routefinder()\"")
    ## You can change heuristic= to either `h1` or `sld`
    demo_routefinder(heuristic=sld)
    print_green("Finished \"demo_routefinder()\"\n")

