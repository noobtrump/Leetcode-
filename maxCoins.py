from typing import List

class Solution:
    def maxCoins(self, coins: List[List[int]]) -> int:
        if not coins or not coins[0]:
            return 0
        
        m, n = len(coins), len(coins[0])
        
        # dp[i][j][k]: 到达 (i,j) 时感化 k 个强盗能获得的最大金币数
        dp = [[[-float('inf')] * 3 for _ in range(n)] for _ in range(m)]
        
        # 初始化起点
        if coins[0][0] >= 0:
            dp[0][0][0] = coins[0][0]
        else:
            dp[0][0][1] = -coins[0][0]  # 感化第一个强盗
        
        # 填充 dp 表
        for i in range(m):
            for j in range(n):
                for k in range(3):
                    if i == 0 and j == 0:
                        continue
                    
                    # 当前单元格金币数
                    current_value = coins[i][j]
                    
                    # 从上方移动
                    if i > 0:
                        if current_value >= 0:
                            dp[i][j][k] = max(dp[i][j][k], dp[i-1][j][k] + current_value)
                        elif k > 0:  # 感化强盗
                            dp[i][j][k] = max(dp[i][j][k], dp[i-1][j][k-1] + current_value)
                        if k < 2:  # 不感化
                            dp[i][j][k] = max(dp[i][j][k], dp[i-1][j][k] - abs(current_value))
                    
                    # 从左方移动
                    if j > 0:
                        if current_value >= 0:
                            dp[i][j][k] = max(dp[i][j][k], dp[i][j-1][k] + current_value)
                        elif k > 0:  # 感化强盗
                            dp[i][j][k] = max(dp[i][j][k], dp[i][j-1][k-1] + current_value)
                        if k < 2:  # 不感化
                            dp[i][j][k] = max(dp[i][j][k], dp[i][j-1][k] - abs(current_value))

        # 获取最大金币数
        return max(dp[m-1][n-1])

# 示例用法
if __name__ == "__main__":
    solution = Solution()
    coins = [
        [0, -2, 3],
        [-4, -5, 6],
        [7, -8, 9]
    ]
    print(solution.maxCoins(coins))  # 输出最大金币数
