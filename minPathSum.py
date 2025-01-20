from typing import List
from math import inf

class Solution1:
    #简单递归
    def minPathSum(self, grid: List[List[int]]) -> int:
        # 定义递归函数 dfs，计算从 (i, j) 到 (0, 0) 的最小路径和
        def dfs(i: int, j: int) -> int:
            # 如果索引越界，返回无穷大，表示不可能的路径
            if i < 0 or j < 0:
                return inf
            
            # 如果到达起点 (0, 0)，返回该点的值
            if i == 0 and j == 0:
                return grid[i][j]
            
            # 递归计算从左边和上边到达当前点的最小路径和
            return min(dfs(i, j - 1), dfs(i - 1, j)) + grid[i][j]

        # 从右下角开始递归计算最小路径和
        return dfs(len(grid) - 1, len(grid[0]) - 1)
from typing import List
from math import inf
from functools import cache


class Solution2:
    #引入cache记忆化优化搜索
    def minPathSum(self, grid: List[List[int]]) -> int:
        @cache  # 缓存装饰器，避免重复计算 dfs 的结果（记忆化）
        def dfs(i: int, j: int) -> int:
            # 如果索引越界，返回无穷大，表示不可能的路径
            if i < 0 or j < 0:
                return inf
            
            # 如果到达起点 (0, 0)，返回该点的值
            if i == 0 and j == 0:
                return grid[i][j]
            
            # 递归计算从左边和上边到达当前点的最小路径和
            return min(dfs(i, j - 1), dfs(i - 1, j)) + grid[i][j]

        # 从右下角开始递归计算最小路径和
        return dfs(len(grid) - 1, len(grid[0]) - 1)



# 测试用例
if __name__ == "__main__":
    solution = Solution2()
    
    # 测试用例 1
    grid1 = [[1, 3, 1], [1, 5, 1], [4, 2, 1]]
    print(solution.minPathSum(grid1))  # 输出: 7，路径为 1 → 3 → 1 → 1 → 1

    # 测试用例 2
    grid2 = [[1, 2, 3], [4, 5, 6]]
    print(solution.minPathSum(grid2))  # 输出: 12，路径为 1 → 2 → 3 → 6

    # 测试用例 3
    grid3 = [[5]]
    print(solution.minPathSum(grid3))  # 输出: 5，只有一个元素

    # 测试用例 4
    grid4 = [[1, 2], [5, 6], [1, 1]]
    print(solution.minPathSum(grid4))  # 输出: 7，路径为 1 → 2 → 6 → 1

