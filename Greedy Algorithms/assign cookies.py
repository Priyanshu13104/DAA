def findContentChildren(g:list[int], s:list[int]) -> int:
    N = len(g)
    M = len(s)

    g.sort()
    s.sort()

    i, j = 0, 0
    count = 0

    while i < N and j < M:
        if g[i] <= s[j]:
            count += 1
            i += 1
        j += 1
    return count


g = [1,2,4]
s = [4,1,2,3]
print(findContentChildren(g, s))
