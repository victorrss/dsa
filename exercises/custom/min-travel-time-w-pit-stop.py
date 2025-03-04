# Problem: Minimum Travel Time with Pit Stop

# Description:
# Given a weighted directed graph representing cities and travel times between them, your task is to compute the minimum travel time from a source city S to a destination city T such that the path includes a mandatory pit stop at city P. In other words, you must travel from S to P and then from P to T. You can assume that all travel times (edge weights) are non-negative.

# Input:

# A graph represented as an adjacency list, where each key is a city and its value is a list of tuples (neighbor, travel_time).
# A source city S.
# A pit stop city P.
# A destination city T.
# Output:

# The minimum travel time from S to T that goes through P.
# If there is no valid route that passes through P, return an appropriate indicator (e.g., -1).
# Example:

# Consider the following graph:

# makefile
# A: [(B, 5), (P, 2)]
# P: [(B, 1), (T, 7)]
# B: [(T, 2)]
# T: []
# S = A, P = P, T = T

# Possible routes:
# A → P → T: travel time = 2 + 7 = 9
# A → P → B → T: travel time = 2 + 1 + 2 = 5
# A → B → T: is not valid because it does not pass through P.
# Thus, the minimum travel time that goes through P is 5.

def minimum_travel_time_with_pit_stop(graph: dict, start: str, pit: str, end: str) -> int:
    """
    Computes the minimum travel time from 'start' to 'end' via the 'pit' stop.
    Use an algorithm like Dijkstra's to calculate the shortest paths.
    
    Parameters:
    - graph: dict, where each key is a city and its value is a list of tuples (neighbor, travel_time)
    - start: str, the starting city (S)
    - pit: str, the mandatory pit stop city (P)
    - end: str, the destination city (T)
    
    Returns:
    - int: the minimum travel time from start to end via pit.
           If no valid route exists, return -1.
    """
    # TODO: Implement the function using Dijkstra's algorithm (or a similar approach)
    # 1. Compute the shortest path from 'start' to 'pit'.
    # 2. Compute the shortest path from 'pit' to 'end'.
    # 3. Return the sum of both distances, or -1 if either path is not reachable.
    pass

def run_tests():
    # Test case 1: Basic scenario
    # Graph represented as an adjacency list
    graph = {
        'A': [('B', 5), ('P', 2)],
        'P': [('B', 1), ('T', 7)],
        'B': [('T', 2)],
        'T': []
    }
    
    # S = 'A', P = 'P', T = 'T'
    # Expected route: A -> P -> B -> T = 2 + 1 + 2 = 5
    result = minimum_travel_time_with_pit_stop(graph, 'A', 'P', 'T')
    expected = 5
    print("Test 1:", "Pass" if result == expected else f"Fail (Expected: {expected}, Got: {result})")
    
    # Test case 2: No valid route through the pit stop
    graph2 = {
        'A': [('B', 3)],
        'B': [('T', 4)],
        'T': [],
        'P': []  # Pit stop 'P' is isolated and unreachable
    }
    
    result = minimum_travel_time_with_pit_stop(graph2, 'A', 'P', 'T')
    expected = -1  # Assuming -1 indicates no valid route
    print("Test 2:", "Pass" if result == expected else f"Fail (Expected: {expected}, Got: {result})")

if __name__ == '__main__':
    run_tests()
