import math

n, k = map(int, input().split())
num_tree_vertices = 2**(k+1) - 1
x = [0 for i in range(n)]
y = [0 for j in range(n)]

for i in range(n):
    x[i], y[i] = map(int, input().split())


def tree_maker(root, area):
    global x, y, num_tree_vertices, n, k

    if len(area) == 2:
        index[area[0]] = index[root] * 2
        index[area[1]] = index[root] * 2 + 1
        return

    m = []
    m_ind = []

    for i in range(len(area)):
        dif_x = x[root] - x[area[i]]
        dif_y = y[root] - y[area[i]]
        if dif_x != 0:
            tmp = (dif_y / dif_x)
            tmp = math.atan(tmp)
        else:
            if dif_y < 0:
                tmp = math.pi/2
            else:
                tmp = -math.pi/2
        m.append(tmp)
        m_ind.append(area[i])

    m, m_ind = zip(*sorted(zip(m, m_ind)))
    m, m_ind = list(m), list(m_ind)
    more_pts = [x for x in m_ind[:len(m_ind)//2]]
    less_pts = [x for x in m_ind[len(m_ind)//2:]]

    tmp_x = []
    for i in range(len(more_pts)):
        tmp_x.append(x[more_pts[i]])
    _, more_pts = zip(*sorted(zip(tmp_x, more_pts)))
    more_pts = list(more_pts)
    more_root, more_pts = more_pts[0], more_pts[1:]

    tmp_x = []
    for i in range(len(less_pts)):
        tmp_x.append(x[less_pts[i]])
    _, less_pts = zip(*sorted(zip(tmp_x, less_pts)))
    less_pts = list(less_pts)
    less_root, less_pts = less_pts[0], less_pts[1:]

    index[more_root] = index[root] * 2
    index[less_root] = index[root] * 2 + 1
    tree_maker(more_root, more_pts)
    tree_maker(less_root, less_pts)


index = [0 for i in range(n)]
index_array = [i for i in range (0, n)]

ZIP = zip(x, y, index_array)

new_x, new_y, new_ind = zip(*sorted(ZIP))

index[new_ind[0]] = 1
tree_maker(new_ind[0], new_ind[1:num_tree_vertices])

for i in range(n):
    print(index[i])