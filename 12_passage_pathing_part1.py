import re
import copy
import pprint
import math
from collections import deque
from collections import defaultdict


pp = pprint.PrettyPrinter(indent = 4)

def read_graph(file):
    g = {}
    with open(file, "r") as f:
        for line in f:
            l = line.replace("\n", "")
            source, target = l.split("-")
            print(source, target)
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


def max_visits(g):
    """ returns dict with max number of visits"""
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
    """ takes a curpath, which we know is valid, and adds an explore node
    returns whether the new path would be valid"""
    visited = defaultdict(lambda: 0)
    for v in curpath:
        visited[v] += 1
    visited[explore] += 1
    return visited[explore] <= maximum_visits[explore]
       


def traverse(g):

    maximum_visits = max_visits(g)
    
    allpaths = []
    q = deque()
    # we will only append to q if we know it can be explored
    q.append(["start"])
    while q:
        curpath = q.popleft()
        node = curpath[-1]
        neighbors = g[node]

        for neighbor in neighbors:
            curpathcopy = curpath[:]
            if neighbor == "end":
                curpathcopy.append("end")
                allpaths.append(curpathcopy)
            elif can_visit(curpathcopy, neighbor, maximum_visits):
                curpathcopy.append(neighbor)
                q.append(curpathcopy)
    return allpaths

    




if __name__ == "__main__":
    file = "input_files/problem12.txt"
    g = read_graph(file)
    allpaths = traverse(g)
    pp.pprint(allpaths)
    print(f"the answer to part 1 is {len(allpaths)}")