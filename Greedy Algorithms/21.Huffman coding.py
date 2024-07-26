from heapq import heappush, heappop
class Node:
    def __init__(self, freq, data):
        self.freq = freq
        self.data = data
        self.left = None
        self.right = None

    def __lt__(self, other):
        return self.freq < other.freq


class Solution:
    def preorder(self, root, partial, collection):
        if not root.left and not root.right:
            collection.append("".join(partial))
            return

        if root.left:
            partial.append("0")
            self.preorder(root.left, partial, collection)
            partial.pop()

        if root.right:
            partial.append("1")
            self.preorder(root.right, partial, collection)
            partial.pop()

    def huffmanCodes(self, S, f, N):
        heap = []

        for i in range(N):
            heappush(heap, [f[i], Node(f[i], S[i])])

        while len(heap) > 1:
            f1, n1 = heappop(heap)
            f2, n2 = heappop(heap)

            node = Node(n1.freq + n2.freq, n1.data + n2.data)
            node.left = n1
            node.right = n2

            heappush(heap, [f1 + f2, node])

        root = heappop(heap)[1]

        partial, collection = [], []
        self.preorder(root, partial, collection)

        return collection

S = "abcdef"
f = [5, 9, 12, 13, 16, 45]
N = len(f)
sol = Solution()
print(sol.huffmanCodes(S, f, N))