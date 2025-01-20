from typing import List
import collections  # 导入collections模块以使用deque

class Solution1:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        # 获取网格的行数和列数
        R, C = len(grid), len(grid[0])

        # 创建一个双端队列用于BFS
        queue = collections.deque()
        
        # 将所有腐烂橘子的坐标加入队列
        for r in range(R):
            for c in range(C):
                if grid[r][c] == 2:
                    queue.append((r, c))  # 将腐烂橘子的坐标加入队列

        # 定义获取相邻单元格的函数
        def neighbors(r, c) -> (int, int):
            for nr, nc in ((r - 1, c), (r, c - 1), (r + 1, c), (r, c + 1)):
                if 0 <= nr < R and 0 <= nc < C:
                    yield nr, nc
        
        d = 0  # 用于记录时间（分钟）
        
        # BFS遍历
        while queue:
            for _ in range(len(queue)):  # 遍历当前层的所有腐烂橘子
                r, c = queue.popleft()  # 从队列中取出当前腐烂橘子的坐标
                for nr, nc in neighbors(r, c):  # 获取相邻单元格
                    if grid[nr][nc] == 1:  # 如果相邻单元格是新鲜橘子
                        grid[nr][nc] = 2  # 将新鲜橘子变为腐烂橘子
                        queue.append((nr, nc))  # 将新的腐烂橘子加入队列
            
            d += 1  # 增加时间（分钟）

        # 检查是否还有新鲜橘子未被腐烂
        if any(1 in row for row in grid):
            return -1
        
        return d - 1 if d > 0 else d  # 返回所需的时间，减去最后一次增加的时间


class Solution2:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        # 统计新鲜橙子的数量
        fresh_num = 0
        
        # 使用双端队列存储腐烂橘子的坐标
        queue = collections.deque()
        
        # 遍历网格，统计新鲜橙子和腐烂橘子
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] == 1:
                    fresh_num += 1  # 新鲜橙子数量加一
                if grid[i][j] == 2:
                    queue.append((i, j))  # 将腐烂橘子的坐标加入队列
        
        minutes = 0  # 初始化分钟数
        
        # 开始进行广度优先搜索（BFS）
        while queue:
            if fresh_num == 0:
                # 如果没有新鲜橙子了，返回所需的分钟数
                return minutes
            
            # 每轮循环表示经过1分钟，周围开始腐烂
            minutes += 1
            size = len(queue)  # 当前队列的大小
            
            for _ in range(size):
                x, y = queue.popleft()  # 从队列中取出一个腐烂橘子的坐标
                
                # 尝试腐烂四个方向的邻居
                fresh_num -= self.rotting(grid, x - 1, y, queue)  # 上方
                fresh_num -= self.rotting(grid, x + 1, y, queue)  # 下方
                fresh_num -= self.rotting(grid, x, y - 1, queue)  # 左方
                fresh_num -= self.rotting(grid, x, y + 1, queue)  # 右方
        
        # 腐烂过程结束，检查是否还有新鲜橙子未被腐烂
        return -1 if fresh_num > 0 else minutes

    def rotting(self, grid: List[List[int]], x: int, y: int, queue: collections.deque) -> int:
        # 检查坐标是否越界或该位置不是新鲜橙子
        if x < 0 or y < 0 or x >= len(grid) or y >= len(grid[0]) or grid[x][y] != 1:
            return 0
        
        # 将新鲜橙子变为腐烂橘子
        grid[x][y] = 2
        queue.append((x, y))  # 将新的腐烂橘子加入队列
        return 1

# 测试用例
if __name__ == "__main__":
    solution = Solution1()
    
    # 测试用例1：存在新鲜橘子，最终会全部腐烂
    grid1 = [[2,1,1],[1,1,0],[0,1,2]]
    print(solution.orangesRotting(grid1))  # 输出：4
    
    # 测试用例2：有新鲜橘子无法腐烂（被空单元隔开）
    grid2 = [[2,1,1],[0,1,1],[1,0,2]]
    print(solution.orangesRotting(grid2))  # 输出：-1
    