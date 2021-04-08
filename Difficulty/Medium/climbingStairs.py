# V1
# 执行用时：40 ms, 在所有 Python3 提交中击败了54.42%的用户
# 内存消耗：14.9 MB, 在所有 Python3 提交中击败了18.96%的用户

class Solution:
    def climbStairs(self, n: int) -> int:
        res = {0:1}
        for i in range(1,n+1):
            if i<=2:
                res[i]=i
            else:
                res[i]=res[i-1]+res[i-2]
        return res[n]

if __name__ == '__main__':
    n = 6
    print(Solution.climbStairs(Solution(), n))