from typing import List

# 定义四个移动方向：右、下、左、上
DIRS = (0, 1), (1, 0), (0, -1), (-1, 0)  # 右下左上

class Solution1:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        # 获取矩阵的行数和列数
        m, n = len(matrix), len(matrix[0])
        ans = []  # 用于存储结果
        i = j = di = 0  # 初始化行索引i，列索引j，方向索引di
        
        for _ in range(m * n):  # 一共走 m*n 步
            ans.append(matrix[i][j])  # 将当前元素添加到结果中
            matrix[i][j] = None  # 标记当前元素为已访问（设置为None）
            # 计算下一步的位置
            x, y = i + DIRS[di][0], j + DIRS[di][1]
            # 如果 (x, y) 出界或者已经访问过
            if x < 0 or x >= m or y < 0 or y >= n or matrix[x][y] is None:
                di = (di + 1) % 4  # 右转90°
            # 更新当前元素的位置
            i += DIRS[di][0]
            j += DIRS[di][1]
        
        return ans  # 返回结果列表


class Solution2:
    #不标记法
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        # 获取矩阵的行数和列数
        m, n = len(matrix), len(matrix[0])
        size = m * n  # 矩阵中元素的总数
        ans = []  # 用于存储结果
        i, j, di = 0, -1, 0  # 初始化行索引i，列索引j，方向索引di，从(0, -1)开始
        
        while len(ans) < size:  # 当结果列表长度小于总元素数时继续循环
            dx, dy = DIRS[di]  # 获取当前方向的增量
            
            for _ in range(n):  # 遍历当前方向，走n步（注意n会减少）
                i += dx  # 更新行索引
                j += dy  # 更新列索引
                ans.append(matrix[i][j])  # 将当前元素添加到结果中
            
            di = (di + 1) % 4  # 右转90°，更新方向索引
            n, m = m - 1, n  # 减少后面的循环次数（步数），更新剩余行数和列数
        
        return ans  # 返回螺旋顺序的结果列表

if __name__ == "__main__":
    solution = Solution2()
    
    # 测试用例1
    matrix1 = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ]
    result1 = solution.spiralOrder(matrix1)
    print("测试用例1的结果:", result1)  
    # 输出应为 [1, 2, 3, 6, 9, 8, 7, 4, 5]

    # 测试用例2
    matrix2 = [
        [1, 2],
        [3, 4]
    ]
    result2 = solution.spiralOrder(matrix2)
    print("测试用例2的结果:", result2)  
    # 输出应为 [1, 2, 4, 3]

    # 测试用例3
    matrix3 = [
        [1]
    ]
    result3 = solution.spiralOrder(matrix3)
    print("测试用例3的结果:", result3)  
    # 输出应为 [1]
