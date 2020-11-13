n, m, distance = map(int, input().split())
jasad = list(map(int, input().split()))
isJasad = [False for i in range(n)]
for i in range(len(jasad)):
    isJasad[jasad[i]-1] = True
adj = [[] for i in range(n)]
for i in range(n-1):
    x, y = map(int, input().split())
    adj[x-1].append(y-1)
    adj[y-1].append(x-1)


def bfs(node, jasad, n):
    global adj
    marked = [False for i in range(n)]
    marked[node] = True
    stack = [node]
    lastJasad = node
    while len(stack) != 0:
        node = stack[0]
        if jasad[node]:
            lastJasad = node
        for i in range(len(adj[node])):
            if not marked[adj[node][i]]:
                stack.append(adj[node][i])
                marked[adj[node][i]] = True
        stack.remove(stack[0])

    return lastJasad


def findOK(node, distance, n):
    depth = [0] * n
    marked = [False for i in range(n)]
    marked[node] = True
    stack = [node]
    parent = [i for i in range(n)]
    while len(stack) != 0:
        node = stack[0]
        depth[node] = depth[parent[node]] + 1
        if depth[node] >= distance:
            break
        for i in range(len(adj[node])):
            if not marked[adj[node][i]]:
                stack.append(adj[node][i])
                parent[adj[node][i]] = node
                marked[adj[node][i]] = True
        stack.remove(stack[0])
    return marked


firstJasad = bfs(0, isJasad, n)
secondJasad = bfs(firstJasad, isJasad, n)

firstOKs = findOK(firstJasad, distance+1, n)
secondOKs = findOK(secondJasad, distance+1, n)
counter = 0
for i in range(n):
    if firstOKs[i] and secondOKs[i]:
        counter += 1

print(counter)
