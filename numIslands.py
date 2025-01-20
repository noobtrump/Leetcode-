from typing import List
from typing import Deque

class Solutio1:
    #DFS递归地探索每个岛屿
    def numIslands(self, grid: List[List[str]]) -> int:
        m, n = len(grid), len(grid[0])  # 获取网格的行数和列数

        def dfs(i: int, j: int) -> None:
            # 出界，或者不是 '1'，就不再往下递归
            if i < 0 or i >= m or j < 0 or j >= n or grid[i][j] != '1':
                return
            grid[i][j] = '2'  # 标记为已访问
            # 递归访问上下左右四个方向
            dfs(i, j - 1)  # 往左走
            dfs(i, j + 1)  # 往右走
            dfs(i - 1, j)  # 往上走
            dfs(i + 1, j)  # 往下走

        ans = 0  # 岛屿计数器
        for i in range(m):
            for j in range(n):
                if grid[i][j] == '1':  # 找到了一个新的岛
                    dfs(i, j)  # 深度优先搜索，标记这个岛屿
                    ans += 1   # 增加岛屿计数
        return ans  # 返回岛屿数量

from typing import List
from typing import Deque

class Solution2:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0
        m, n = len(grid), len(grid[0])  # 获取网格的行数和列数
        
        def bfs(i: int, j: int) -> None:
            queue =Deque([(i,j)])  # 初始化队列，将起始点入队
            while queue:
                x, y = queue.popleft()   # 从队列中取出元素
                for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:  # 上下左右移动
                    nx, ny = x + dx, y + dy
                    if 0 <= nx < m and 0 <= ny < n and grid[nx][ny] == '1':
                        grid[nx][ny] = '2'      # 标记为已访问
                        queue.append((nx, ny))   # 将新坐标入队

        ans = 0  # 岛屿计数器
        for i in range(m):
            for j in range(n):
                if grid[i][j] == '1':  # 找到新的岛屿
                    bfs(i, j)           # 广度优先搜索
                    ans += 1           # 增加岛屿计数
        
        return ans
    
# 测试用例
if __name__ == "__main__":
    sol = Solution2()
    
    # 测试用例1 (3)
    grid1 = [
        ["1", "1", "0", "0", "0"],
        ["1", "0", "0", "1", "1"],
        ["0", "0", "0", "0", "0"],
        ["0", "1", "1", "0", "0"]
    ]
    print("Number of islands (Test Case 1):", sol.numIslands(grid1))  # 输出: 3

    # 测试用例2  (2)
    grid2 = [
        ["1", "1", "1"],
        ["0", "0", "0"],
        ["1", "1", "1"]
    ]
    print("Number of islands (Test Case 2):", sol.numIslands(grid2))  # 输出: 2
