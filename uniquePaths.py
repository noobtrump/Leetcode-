import math
class Solution1:
    def uniquePaths(self, m: int, n: int) -> int:
        # 创建一个 m x n 的二维列表，初始化为 0
        f = [[0] * n for _ in range(m)]
        
        # 第一行和第一列的路径数都为 1
        for i in range(m):
            f[i][0] = 1
        for j in range(n):
            f[0][j] = 1
        
        # 填充 dp 数组
        for i in range(1, m):
            for j in range(1, n):
                f[i][j] = f[i - 1][j] + f[i][j - 1]  # 当前单元格的路径数等于上方和左方单元格的路径数之和

        # 返回右下角单元格的路径数
        return f[m - 1][n - 1]


class Solution2:
    def uniquePaths(self, m: int, n: int):
        #使用组合公式计算从（m+n-2）中选择（n - 1）
        return math.comb(m + n -2, n - 1)
# 测试用例
if __name__ == "__main__":
    solution = Solution2()
    print(solution.uniquePaths(3, 7))  # 输出: 28
    print(solution.uniquePaths(3, 2))  # 输出: 3
