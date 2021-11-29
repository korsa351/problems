import json
from collections import deque

js = json.loads(input())
graph = {}
total_link = {}
queue = deque()
for class_ in js:
    graph[class_["name"]] = set(class_["parents"])
    total_link[class_["name"]] = 0
for name, parent in graph.items():
    queue.extendleft(parent)
    while queue:
        pers = queue.pop()
        if name != pers:
            total_link[pers] += 1
        queue.extendleft(graph[pers])
total_link = sorted(total_link.items(), key=lambda x: x[0])
for pers in total_link:
    print(f"{pers[0]} : {pers[1] + 1}")
