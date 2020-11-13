n = int(input())
array = list(map(int, input().split()))
visited = []
possible = 0
last_fact = 1
for i in range(2, n):
    last_fact = (last_fact * i)

for i in range(n):
    seen_less = 0
    for x in visited:
        if x < array[i]:
            seen_less += 1

    possible += ((array[i] - 1) - seen_less) * last_fact
    last_fact //= n-i-1 if n-i-1 > 0 else 1
    visited.append(array[i])

print((possible+1)%(10**9+7))