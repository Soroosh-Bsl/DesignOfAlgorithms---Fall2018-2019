n, m = map(int, input().split())
first = []
second = []

for i in range(m):
    x, y = map(int, input().split())
    if x > y:
        x, y = y, x
    first.append(x)
    second.append(y)

neighbours = [[] for i in range(len(first))]
for i in range(len(first)):
    for j in range(i+1, len(first)):
        if first[i] < first[j] < second[i] < second[j] or first[j] < first[i] < second[j] < second[i]:
            neighbours[i].append(j)
            neighbours[j].append(i)


in_or_out = [0 for i in range(m)]


def bfs_bipartite(node):
    global in_or_out
    in_or_out[node] = 1
    queue = []
    queue.append(node)
    while queue:
        x = queue.pop()
        for neighbour in neighbours[x]:
            if in_or_out[neighbour] == 0:
                in_or_out[neighbour] = -in_or_out[x]
                queue.append(neighbour)
            elif in_or_out[neighbour] == in_or_out[x]:
                return False
    return True


def bfs_all():
    for i in range(len(in_or_out)):
        if in_or_out[i] == 0:
            if not bfs_bipartite(i):
                return False
    return True


answer = ""
if bfs_all():
    for how in in_or_out:
        if how == 1:
            answer += "I"
        else:
            answer += "O"
    print(answer)
else:
    print("Impossible")