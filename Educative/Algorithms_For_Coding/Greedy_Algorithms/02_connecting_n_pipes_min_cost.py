"""
Given n pipes, find the minimum cost of connecting them.
"""
# normal solution
def min_cost(pipes):
    """
    This function finds the minimum cost of connecting n pipes
    :param pipes: A list of n pipes
    :return: The minimum cost of connecting n pipes
    """

    # Write your code here!
    pipes.sort()
    total_cost = 0

    while len(pipes) > 1:
        cost = pipes[0] + pipes[1]
        total_cost += cost
        pipes = pipes[2:] + [cost]
        pipes.sort()

    return total_cost


# heaping solution
import heapq
def min_cost_heapify(pipes):
    """
    This function finds the minimum cost of connecting n pipes
    :param pipes: A list of n pipes
    :return: The minimum cost of connecting n pipes
    """

    # Write your code here!
    heapq.heapify(pipes)
    total_cost = 0

    while len(pipes) > 1:
        cost = heapq.heappop(pipes) + heapq.heappop(pipes)
        total_cost += cost
        heapq.heappush(pipes, cost)

    return total_cost


# Main program to test above function
if __name__ == "__main__":

    pipes = [4, 3, 2, 6]

    print(min_cost(pipes))
    print(min_cost_heapify(pipes))