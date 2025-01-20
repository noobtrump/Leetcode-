from typing import List
class Solution1:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        不返回任何值，直接在原地修改矩阵。
        """
        # 获取矩阵的行数和列数
        row = len(matrix)  # 行数
        col = len(matrix[0])  # 列数
        
        # 创建两个集合，用于存储需要置零的行和列
        row_zero = set()  # 存储需要置零的行索引
        col_zero = set()  # 存储需要置零的列索引

        # 遍历整个矩阵，找到所有值为0的元素
        for i in range(row):
            for j in range(col):
                if matrix[i][j] == 0:  # 如果当前元素为0
                    row_zero.add(i)  # 将该行索引添加到row_zero集合中
                    col_zero.add(j)  # 将该列索引添加到col_zero集合中

        # 再次遍历矩阵，根据row_zero和col_zero集合中的索引将相应的元素置为0
        for i in range(row):
            for j in range(col):
                if i in row_zero or j in col_zero:  # 如果当前行或列在需要置零的集合中
                    matrix[i][j] = 0  # 将当前元素置为0


class Solution2:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        不返回任何值，直接在原地修改矩阵。
        """
        # 用于标记第一列是否需要置零
        flag_col = False  
        
        # 获取矩阵的行数和列数
        row = len(matrix)  # 行数
        col = len(matrix[0])  # 列数
        
        # 第一步：遍历矩阵，记录需要置零的行和列
        for i in range(row):
            # 检查第一列是否有0
            if matrix[i][0] == 0: 
                flag_col = True  # 如果第一列有0，设置标志为True
            
            # 从第二列开始检查当前行的其他元素
            for j in range(1, col):
                if matrix[i][j] == 0:  # 如果当前元素为0
                    matrix[i][0] = 0  # 将当前行的第一列置为0
                    matrix[0][j] = 0  # 将当前列的第一行置为0

        # 第二步：从后往前遍历矩阵，根据第一行和第一列的信息将相应元素置为0
        for i in range(row - 1, -1, -1):  # 从最后一行开始遍历到第一行
            for j in range(col - 1, 0, -1):  # 从最后一列开始遍历到第二列
                if matrix[i][0] == 0 or matrix[0][j] == 0:  # 如果当前行或当前列需要置零
                    matrix[i][j] = 0  # 将当前元素置为0

            # 如果第一列需要置零，根据标志设置第一列的所有元素为0
            if flag_col: 
                matrix[i][0] = 0  

if __name__ == "__main__":
    solution = Solution2()
    
    # 测试用例1
    matrix1 = [
        [0, 1, 2, 0],
        [3, 4, 5, 2],
        [1, 3, 1, 5]
    ]
    
    print("原始矩阵1:")
    for row in matrix1:
        print(row)

    solution.setZeroes(matrix1)

    print("修改后的矩阵1:")
    for row in matrix1:
        print(row)

    # 测试用例2
    matrix2 = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ]
    
    print("\n原始矩阵2:")
    for row in matrix2:
        print(row)

    solution.setZeroes(matrix2)

    print("修改后的矩阵2:")
    for row in matrix2:
        print(row)