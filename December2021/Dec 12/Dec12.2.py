import json
# Change file name depending on json file you wish to load
with open('main_problem.json') as json_file:
    graph = json.load(json_file)

# Code modified from https://www.python.org/doc/essays/graphs/
def find_all_paths(graph, start, end, path=[], revisit=False):
    path = path + [start]
    if start == end:
        return [path]
    if start not in graph:
        return []
    paths = []

    revisit = False
    for element in set(path):
        if path.count(element) >= 2 and element == element.lower():
            revisit = True
            break

    for node in graph[start]:
        if node not in path or node == node.upper() or revisit == False:
            newpaths = find_all_paths(graph, node, end, path, revisit)
            for newpath in newpaths:
                paths.append(newpath)
    return paths

paths = find_all_paths(graph, 'start', 'end')
print(len(paths))
# 149220