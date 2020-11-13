n, p = map(int, input().split())
a = list(map(int, input().split()))

X_ORs = []
first_v = []
second_v = []

for i in range(n):
    for j in range(i+1, n):
        X_ORs.append(a[i] ^ a[j])
        first_v.append(i)
        second_v.append(j)

X_ORs, first_v, second_v = zip(*sorted(zip(X_ORs, first_v, second_v), reverse=True))
X_ORs, first_v, second_v = list(X_ORs), list(first_v), list(second_v)

v = [-1 for i in range(n)]
v_rank = [0 for i in range(n)]


def find(x):
    global v
    if v[x] != -1:
        v[x] = find(v[x])
        return v[x]
    else:
        return x


def union(x, y):
    tmp_x = find(x)
    tmp_y = find(y)
    if tmp_x == tmp_y:
        return False
    if v_rank[tmp_x] < v[tmp_y]:
        tmp_x, tmp_y = tmp_y, tmp_x
    v[tmp_y] = tmp_x
    if v_rank[tmp_x] == v_rank[tmp_y]:
        v_rank[tmp_x] += 1
    return True


minimum_edge = 0
for i in range(len(X_ORs)):
    if union(first_v[i], second_v[i]):
        minimum_edge = X_ORs[i]

print(minimum_edge)
