import antennae_freqs, mars_planner, routefinder, search_algorithms
from search_algorithms import depth_first_search, breadth_first_search

def print_green(print_str: str):
    print("\033[92m" + print_str + "\033[0m")

def demo_antennae_freqs():
    antennae_freqs.main()

def demo_mars_planner(decomposed: bool, search_func=breadth_first_search, limit: int=0):
    print(mars_planner.main(decomposed, search_func, limit))

def demo_routefinder():
    print(routefinder.main())

if __name__ == '__main__':

    print_green("Running \"demo_antennae_freqs()\"")
    demo_antennae_freqs()
    print_green("Finished \"demo_antennae_freqs()\"\n")

    print_green("\nRunning \"demo_mars_planner()\"")
    # You can change the parameters here, limit is ignored when using bfs
    demo_mars_planner(decomposed=True, search_func=depth_first_search, limit=10)
    print_green("Finished \"demo_mars_planner()\"\n")

    print_green("\nRunning \"demo_routefinder()\"")
    demo_routefinder()
    print_green("Finished \"demo_routefinder()\"\n")

