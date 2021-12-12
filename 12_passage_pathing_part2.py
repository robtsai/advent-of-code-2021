import re
import copy
import pprint
import math
from collections import deque
from collections import defaultdict


pp = pprint.PrettyPrinter(indent=4)


def read_graph(file):
    g = {}
    with open(file, "r") as f:
        for line in f:
            l = line.replace("\n", "")
            source, target = l.split("-")
            if not source in g:
                g[source] = [target]
            elif target not in g[source]:
                g[source].append(target)

            if not target in g:
                g[target] = [source]
            elif source not in g[target]:
                g[target].append(source)
    return g


lowercase = re.compile("[a-z]+")
uppercase = re.compile("[A-Z]+")
start_end = re.compile("(start|end)")


# there is one exception where you can ovverride and visit a small cave twice
def max_visits(g):
    """returns dict with max number of visits"""
    d = {}
    for k in g:
        if start_end.match(k):
            d[k] = 1
        elif lowercase.match(k):
            d[k] = 1
        elif uppercase.match(k):
            d[k] = math.inf
        else:
            raise ValueError("invalid graph")
    return d


def can_visit(curpath, explore, maximum_visits):
    """takes a curpath,  we can visit one small cave"""
    visited = defaultdict(lambda: 0)
    for v in curpath:
        visited[v] += 1
    visited[explore] += 1

    overrides = 0
    for k, v in visited.items():
        if lowercase.match(k):
            if v > 1:
                overrides += v - 1
    return overrides < 2


def traverse(g):

    maximum_visits = max_visits(g)

    allpaths = []
    q = deque()
    q.append(["start"])
    while q:
        curpath = q.popleft()
        node = curpath[-1]
        neighbors = g[node]

        for neighbor in neighbors:
            if neighbor == "end":
                curpathcopy = curpath[:]
                curpathcopy.append("end")
                allpaths.append(curpathcopy)
            elif neighbor == "start":
                continue
            else:
                curpathcopy = curpath[:]
                if can_visit(curpathcopy, neighbor, maximum_visits):
                    curpathcopy.append(neighbor)
                    q.append(curpathcopy)

    return allpaths


if __name__ == "__main__":
    file = "input_files/problem12.txt"
    g = read_graph(file)
    allpaths = traverse(g)
    print(f"the answer to part 2 is {len(allpaths)}")
