# User function Template for python3
import heapq
class Solution:
    # Function to return the minimum cost of connecting the ropes.
    def minCost(self, arr, n):
        # Create a min-heap from the array of rope lengths
        heapq.heapify(arr)

        total_cost = 0

        # Continue until the heap has more than one rope
        while len(arr) > 1:
            # Extract the two smallest ropes
            first = heapq.heappop(arr)
            second = heapq.heappop(arr)

            # The cost to connect these two ropes
            cost = first + second
            total_cost += cost

            # Push the resulting rope back into the heap
            heapq.heappush(arr, cost)

        return total_cost

arr = [4, 3, 2, 6]
n = 4
sol = Solution()
print(sol.minCost(n=n, arr=arr))