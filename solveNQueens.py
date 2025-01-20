from typing import List

class Solution1:
    #基于集合的回溯算法：用三个集合分别记录列及两个方向上的斜线上是否有皇后
    def solveNQueens(self, n: int) -> List[List[str]]:
        # 生成当前皇后布局的棋盘
        def generateBoard() -> List[str]:
            board = []  # 用于存储棋盘布局
            for i in range(n):
                # 将当前行的皇后位置标记为 'Q'
                row = ["."] * n  # 初始化当前行
                row[queens[i]] = "Q"  # 在对应列放置皇后
                board.append("".join(row))  # 将行加入棋盘
            return board

        # 回溯函数，尝试在每一行放置皇后
        def backtrack(row: int):
            if row == n:  # 如果所有皇后都已放置
                board = generateBoard()  # 生成当前棋盘布局
                solutions.append(board)  # 将布局加入结果集
            else:
                for i in range(n):  # 遍历每一列
                    # 检查当前列和对角线是否可以放置皇后
                    if i in columns or (row - i) in diagonal1 or (row + i) in diagonal2:
                        continue  # 如果冲突则跳过
                    
                    queens[row] = i  # 在当前行放置皇后
                    columns.add(i)  # 标记当前列为已占用
                    diagonal1.add(row - i)  # 标记左对角线为已占用
                    diagonal2.add(row + i)  # 标记右对角线为已占用
                    
                    backtrack(row + 1)  # 尝试放置下一行的皇后
                    
                    # 回溯，移除标记，尝试其他可能性
                    columns.remove(i)
                    diagonal1.remove(row - i)
                    diagonal2.remove(row + i)

        solutions = []  # 存储所有解决方案
        queens = [-1] * n  # 存储每一行皇后的位置
        columns = set()  # 存储已占用的列
        diagonal1 = set()  # 存储已占用的左对角线（row - col）
        diagonal2 = set()  # 存储已占用的右对角线（row + col）
        
        backtrack(0)  # 从第0行开始回溯
        return solutions  # 返回所有解决方案

from typing import List

class Solution2:
#基于位运算的回溯：每次放置皇后时，三个整数的按位或运算的结果即为不能放置皇后的位置，其余位置即为可以放置皇后的位置。
#x & (−x) 可以获得 x 的二进制表示中的最低位的 1 的位置；x & (x−1) 可以将 x 的二进制表示中的最低位的 1 置成 0。
#记录皇后信息的空间复杂度由O（N）降到O（1）
    def solveNQueens(self, n: int) -> List[List[str]]:
        # 生成当前皇后布局的棋盘
        def generateBoard() -> List[str]:
            board = []  # 用于存储棋盘布局
            for i in range(n):
                row = ["."] * n  # 初始化当前行
                row[queens[i]] = "Q"  # 在对应列放置皇后
                board.append("".join(row))  # 将行加入棋盘
            return board

        # 回溯函数，尝试在每一行放置皇后
        def solve(row: int, columns: int, diagonals1: int, diagonals2: int):
            if row == n:  # 如果所有皇后都已放置
                board = generateBoard()  # 生成当前棋盘布局
                solutions.append(board)  # 将布局加入结果集
            else:
                # 计算可用位置：所有位置都为1，然后与已占用的列和对角线取反
                availablePositions = ((1 << n) - 1) & (~(columns | diagonals1 | diagonals2))
                while availablePositions:
                    # 找到最低位的1，表示可以放置皇后的列
                    position = availablePositions & (-availablePositions)
                    availablePositions = availablePositions & (availablePositions - 1)  # 移除已占用的位置
                    
                    column = bin(position - 1).count("1")  # 获取当前放置皇后的列索引
                    queens[row] = column  # 在当前行记录皇后的位置
                    
                    # 递归调用，更新已占用的列和对角线信息
                    solve(row + 1, columns | position, (diagonals1 | position) << 1, (diagonals2 | position) >> 1)

        solutions = []  # 存储所有解决方案
        queens = [-1] * n  # 存储每一行皇后的位置
        
        solve(0, 0, 0, 0)  # 从第0行开始回溯
        return solutions  # 返回所有解决方案

class Solution3:
#回溯+覆盖：queens 数组用于存储每一行皇后的位置，直接在数组中覆盖，无需回溯恢复现场。通过 enumerate(col) 遍历列的可用性，判断当前列是否可以放置皇后。
#使用简单的布尔数组来管理状态，不需要复杂的位运算，逻辑清晰，易于理解
 
    def solveNQueens(self, n: int) -> List[List[str]]:
        ans = []  # 存储所有有效的 N 皇后布局
        queens = [0] * n  # queens[r] 表示第 r 行皇后放置在第 c 列
        col = [False] * n  # 用于标记每一列是否被占用
        diag1 = [False] * (n * 2 - 1)  # 用于标记从左上到右下的对角线是否被占用
        diag2 = [False] * (n * 2 - 1)  # 用于标记从右上到左下的对角线是否被占用

        def dfs(r: int) -> None:
            if r == n:  # 如果已经放置了 n 个皇后
                # 将当前布局转换为棋盘格式并添加到结果中
                ans.append(['.' * c + 'Q' + '.' * (n - 1 - c) for c in queens])
                return
            
            # 在第 r 行放置皇后
            for c, ok in enumerate(col):  # 遍历每一列
                if not ok and not diag1[r + c] and not diag2[r - c]:  # 判断能否放置皇后
                    queens[r] = c  # 将皇后放在第 r 行的第 c 列
                    col[c] = diag1[r + c] = diag2[r - c] = True  # 标记列和对角线为占用
                    
                    dfs(r + 1)  # 尝试放置下一行的皇后
                    
                    # 恢复现场，移除标记，尝试其他可能性
                    col[c] = diag1[r + c] = diag2[r - c] = False  

        dfs(0)  # 从第0行开始回溯
        return ans  # 返回所有有效的 N 皇后布局
    
# 测试用例
if __name__ == "__main__":
    solution = Solution3()
    
    # 测试用例1：输入 n = 4，应该返回两个解决方案
    print("Test Case 1 Output:", solution.solveNQueens(4))  
    # 输出: [[".Q..", "...Q", "Q...", "..Q."], ["..Q.", "Q...", "...Q", ".Q.."]]

    # 测试用例2：输入 n = 1，只有一个解决方案
    print("Test Case 2 Output:", solution.solveNQueens(1))  
    # 输出: [["Q"]]

    # 测试用例3：输入 n = 5，应该返回多个解决方案（具体数量依赖于实现）
    print("Test Case 3 Output:", solution.solveNQueens(5))  
    # 输出: 多个解决方案，例如 [["Q....", "...Q.", ".Q...", "....Q", "..Q.."], ...]
