from typing import List

class Solution:
    def zigzagTraversal(self, grid: List[List[int]]) -> List[int]:
        if not grid or not grid[0]:
            return []

        result = []
        m = len(grid)  
        n = len(grid[0])  

        for i in range(m):
            if i % 2 == 0:  
                for j in range(n):
                    if j % 2 == 0:  
                        result.append(grid[i][j])
            else:  
                for j in range(n - 1, -1, -1):
                    if j % 2 == 1:  
                        result.append(grid[i][j])

        return result

# Example usage
if __name__ == "__main__":
    solution = Solution()
    grid = [
        [1, 2, 3, 4],
        [5, 6, 7, 8],
        [9, 10, 11, 12],
        [13, 14, 15, 16]
    ]
    print(solution.zigzagTraversal(grid))  # Output will be the zigzag traversal result
