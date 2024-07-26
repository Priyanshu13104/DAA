from typing import List
def findContentChildren(g: List[int], s: List[int]) -> int:
    g.sort()
    s.sort()
    N = len(g)
    M = len(s)

    i, j = 0, 0
    count = 0
    while i < N and j < M:
        if g[i] <= s[j]:
            count += 1
            i += 1
        j += 1
    return count


g = [1,2,3]
s = [1,3]
print(findContentChildren(g, s))