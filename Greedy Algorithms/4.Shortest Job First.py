class Solution:
    def solve(self, bt):
        wt = 0
        time = 0
        bt.sort()
        for i in range(len(bt)-1):
            time += bt[i]
            wt += time
        return wt//len(bt)

bt = [4,3,7,1,2]
sol = Solution()
print(sol.solve(bt=bt))