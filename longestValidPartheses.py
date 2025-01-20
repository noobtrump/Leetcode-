class Solution:
    def longestValidParentheses(self, s: str) -> int:
        n = len(s)
        dp = [0] * n  # dp数组初始化为0
        max_len = 0

        for i in range(1, n):
            if s[i] == ')':  # 只处理右括号
                if s[i - 1] == '(':  # 情况一：形成有效对
                    dp[i] = (dp[i - 2] if i >= 2 else 0) + 2
                elif i - dp[i - 1] > 0 and s[i - dp[i - 1] - 1] == '(':  # 情况二：嵌套有效对
                    dp[i] = dp[i - 1] + (dp[i - dp[i - 1] - 2] if i - dp[i - 1] >= 2 else 0) + 2

                max_len = max(max_len, dp[i])  # 更新最大长度

        return max_len

# 测试用例
if __name__ == "__main__":
    solution = Solution()
    print(solution.longestValidParentheses("(()"))      # 输出: 2
    print(solution.longestValidParentheses(")()())"))   # 输出: 4
    print(solution.longestValidParentheses(""))          # 输出: 0
