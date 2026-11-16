class Solution:
    def numTrees(self, n: int) -> int:
        num = [0] * (n+1)
        num[0] = 1
        for i in range(1, n+1):
            for j in range(i):
                num[i] += num[j] * num[i- 1 - j]
        return num[n]