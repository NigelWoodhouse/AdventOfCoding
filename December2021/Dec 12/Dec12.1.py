import json
# Change file name depending on json file you wish to load
with open('main_problem.json') as json_file:
    graph = json.load(json_file)

def find_paths(graph, start, end, path=[]):
    path = path + [start]
    if start == end:
        return [path]
    if start not in graph:
        return []
    paths = []

    for node in graph[start]:
        if node not in path or node == node.upper():
            newpaths = find_paths(graph, node, end, path)
            for newpath in newpaths:
                paths.append(newpath)
    return paths

paths = find_paths(graph, 'start', 'end')
print(paths)
print(len(paths))
# 5104