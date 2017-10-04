from random import randrange
from collections import deque

BOARD_SIZE = 100


class Node(object):
    def __init__(self, tile):
        self._tile = tile
        self._siblings = []

    def add_sibling(self, s):
        self._siblings.append(s)

    def get_siblings(self):
        return self._siblings


class SnakesAndLadders(object):
    def __init__(self):
        self._graph = [Node(x) for x in range(BOARD_SIZE)]
        self._tile = [x for x in range(BOARD_SIZE)]

        for i in range(int(input())):
            start, end = [int(x)-1 for x in input().split(' ')]
            self._tile[start] = end

        for i in range(BOARD_SIZE):
            for j in range(i+1, i+7 if i+7 < BOARD_SIZE else BOARD_SIZE):
                self._graph[i].add_sibling(self._graph[self._tile[j]])

    def search(self):
        # Implementation of a breadth-first search.
        start = self._graph[0]
        goal = self._graph[BOARD_SIZE-1]

        frontier = deque()
        frontier.append(start)
        came_from = {}
        came_from[start] = None

        while len(frontier) != 0:
            current = frontier.popleft()

            if current == goal:
                break

            for next in current.get_siblings():
                if next not in came_from:
                    frontier.append(next)
                    came_from[next] = current

        # Construct the optimal path from the came_from dictionary.
        optimal_path = []
        curr_node = goal
        while curr_node != start:
            optimal_path.append(curr_node)
            curr_node = came_from[curr_node]
        optimal_path.append(start)

        return optimal_path[::-1]


snl = SnakesAndLadders()
for i in snl.search():
    print(i._tile+1, end=' ')
