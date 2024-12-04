
# dfs
# given a graph, find the target using dfs
graph = {
    1: [2, 3, 4],
    2: [1],
    3: [1, 4],
    4: [1, 3]
}
start = 1
target = 4

# stack
def dfsthing(start, target, graph):
    visited = set()
    stack = [start]
    while stack:
        state = stack.pop()
        visited.add(state)
        if state in visited:
            continue
        if state == target:
            return True
        for neighbor in graph[state]:
            if neighbor not in visited:
                stack.append(neighbor)
    return False
    

# queue
# bfs
from queue import Queue
from collections import deque
def bfsthing(start, target, graph):
    q = deque()
    q.append((start,0))
    visited = set()
    while q:
        state,step = q.popleft()
        visited.add(state)
        if state in visited:
            continue
        if state == target:
            return step
        for neighbor in graph[state]:
            if neighbor not in visited:
                q.append((neighbor,step + 1))
    return -1


graph = {
    'a': [(6, 'b'), (2, 'c'), (3, 'd')],
    'b': [(6, 'a'), (2, 'd'), (4, 'e')],
    'c': [(2, 'a')],
    'd': [(2, 'b'), (3, 'a')],
    'e': [(4, 'b')]
}
# mst
import heapq

def msthing(graph):
    hpq = []
    total = 0
    visited = set()
    heapq.heappush(hpq,(0,'a'))
    while hpq:
        length,state = heapq.heappop(hpq)
        if state in visited:
            continue
        visited.add(state)
        total += length
        for neighbor_length, neighbor in graph[state]:
            if neighbor not in visited:
                heapq.heappush(hpq,(neighbor_length, neighbor))

        print(hpq)
    return total

# dijkstra
start, end = 'a', 'e'
def djthing(start, end, graph):
    hq = []
    heapq.heappush(hq,(0,start))
    visited = set()
    while hq:
        length, state = heapq.heappop(hq)
        if state in visited:
            continue
        visited.add(state)
        if state == end:
            return length
        for length_neighbor, neighbor in graph[state]:
            if neighbor not in visited:
                heapq.heappush(hq,(length_neighbor + length, neighbor))
    return -1


print(djthing(start,end,graph))