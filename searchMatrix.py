from typing import List
from bisect import bisect_left


class Solution1:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # 获取矩阵的行数和列数
        m, n = len(matrix), len(matrix[0]) if matrix else 0
        
        # 如果矩阵为空，直接返回 False
        if m == 0 or n == 0:
            return False
        
        left, right = -1, m * n  # 初始化二分查找的左右边界
        
        while left + 1 < right:  # 当左边界与右边界相邻时停止循环
            mid = (left + right) // 2  # 计算中间索引
            # 将一维索引转换为二维索引
            x = matrix[mid // n][mid % n]
            
            if x == target:  # 如果找到目标值，返回 True
                return True
            
            if x < target:  # 如果当前值小于目标值，移动左边界
                left = mid
            else:  # 如果当前值大于目标值，移动右边界
                right = mid
        
        return False  # 如果未找到目标值，返回 False

class Solution2:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # 获取矩阵的行数和列数
        m, n = len(matrix), len(matrix[0]) if matrix else 0
        
        # 如果矩阵为空，直接返回 False
        if m == 0 or n == 0:
            return False
        
        # 使用 bisect_left 在 range(m * n) 中查找目标值的位置
        # range(m * n) 代表将二维矩阵视为一维数组
        i = bisect_left(range(m * n), target, key=lambda x: matrix[x // n][x % n])
        
        # 检查找到的位置是否在矩阵范围内，并且对应的值是否等于目标值
        return i < m * n and matrix[i // n][i % n] == target
    
class Solution3:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # 获取矩阵的行数和列数
        m, n = len(matrix), len(matrix[0]) if matrix else 0
        
        # 如果矩阵为空，直接返回 False
        if m == 0 or n == 0:
            return False
        
        # 从右上角开始搜索
        i, j = 0, n - 1
        
        # 当行索引小于行数且列索引大于等于0时继续循环
        while i < m and j >= 0:
            if matrix[i][j] == target:  # 如果找到目标值
                return True
            
            if matrix[i][j] < target:  # 当前值小于目标值
                i += 1  # 移动到下一行，因为这一行剩余元素全部小于 target，排除这一行
            else:  # 当前值大于目标值
                j -= 1  # 移动到前一列，因为这一列剩余元素全部大于 target，排除这一列
        
        return False  # 如果未找到目标值，返回 False


# 测试用例
if __name__ == "__main__":
    solution = Solution3()
    
    # 测试用例1：正常情况，目标在矩阵中
    matrix1 = [[1, 3, 5], [7, 9, 11], [12, 14, 16]]
    target1 = 9
    print("Test Case 1 Output:", solution.searchMatrix(matrix1, target1))  
    # 输出: True

    # 测试用例2：正常情况，目标不在矩阵中
    matrix2 = [[1, 3, 5], [7, 9, 11], [12, 14, 16]]
    target2 = 10
    print("Test Case 2 Output:", solution.searchMatrix(matrix2, target2))  
    # 输出: False

    # 测试用例3：空矩阵
    matrix3 = []
    target3 = 5
    print("Test Case 3 Output:", solution.searchMatrix(matrix3, target3))  
    # 输出: False