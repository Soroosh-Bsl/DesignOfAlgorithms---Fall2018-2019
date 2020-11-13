n, m = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
adj = [[] for i in range(n+2)]
CAP = 1000
capacity = [[0 for i in range(n+2)] for i in range(n+2)]
for i in range(m):
    x, y = map(int, input().split())
    adj[x].append(y)
    adj[y].append(x)
    capacity[x][y] = CAP
    capacity[y][x] = CAP
d = [0 for i in range(n+2)]
for i in range(n):
    d[i+1] = a[i]-b[i]
for i in range(1, n+1):
    if d[i] > 0:
        capacity[i][n+1] = d[i]
        adj[i].append(n+1)
    elif d[i] < 0:
        capacity[0][i] = -d[i]
        adj[0].append(i)

def bfs(node, target, parent):
    global n, capacity
    marked = [False for i in range(n+2)]
    marked[node] = True
    queue = [node]
    while len(queue) != 0:
        node = queue[0]
        queue.remove(queue[0])
        for i in range(len(adj[node])):
            if not marked[adj[node][i]] and capacity[node][adj[node][i]] > 0:
                queue.append(adj[node][i])
                marked[adj[node][i]] = True
                parent[adj[node][i]] = node
    return True if marked[target] else False


def ford_fulkerson(source, target):
    global capacity, CAP
    parent = [i for i in range(n+2)]
    while bfs(source, target, parent):
        node = target
        now_flow = CAP
        while node != source:
            now_flow = min(now_flow, capacity[parent[node]][node])
            node = parent[node]
        node = target
        while node != source:
            capacity[parent[node]][node] -= now_flow
            capacity[node][parent[node]] += now_flow
            node = parent[node]


possible = True
ford_fulkerson(0, n+1)
for i in range(n+2):
    if capacity[0][i] != 0:
        possible = False
        break

if possible:
    print("YES")
    for i in range(1, n+1):
        sum = 0
        printing = capacity[i][1:n+1]
        for j in range(len(printing)):
            if printing[j] <= 1000:
                printing[j] = 0
            else:
                printing[j] = printing[j] - 1000
                sum += printing[j]
        printing[i-1] = a[i-1] - sum
        for k in range(len(printing)):
            print(printing[k], end=" ")
        print()
else:
    print("NO")
