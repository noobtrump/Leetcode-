class Solution1:
    #DP:在子串大于2的前提下进行动态规划，要列出边界条件即子串长度为1或2
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        if n < 2:
            return s
        
        max_len = 1  # 最长回文子串的长度
        begin = 0    # 最长回文子串的起始位置
        
        # dp[i][j] 表示 s[i..j] 是否是回文串
        dp = [[False] * n for _ in range(n)]
        
        # 初始化：每个单独字符都是回文串
        for i in range(n):
            dp[i][i] = True
        
        # 递推开始
        # 先枚举子串长度
        for L in range(2, n + 1):  # L 是子串的长度
            # 枚举左边界
            for i in range(n):
                j = L + i - 1  # 右边界
                if j >= n:     # 如果右边界越界，就可以退出当前循环
                    break
                    
                if s[i] != s[j]:  # 如果两端字符不相同
                    dp[i][j] = False 
                else:
                    if j - i < 3:   # 如果子串长度为2或3
                        dp[i][j] = True
                    else:
                        dp[i][j] = dp[i + 1][j - 1]
                
                # 更新最长回文子串的信息
                if dp[i][j] and j - i + 1 > max_len:
                    max_len = j - i + 1
                    begin = i
        
        return s[begin:begin + max_len]
class Solution2:
    def expandAroundCenter(self, s: str, left: int, right: int) -> tuple:
        # 扩展中心的方法，返回回文子串的左右边界
        while left >= 0 and right < len(s) and s[left] == s[right]:
            left -= 1
            right += 1
        return left + 1, right - 1  # 返回回文子串的起始和结束索引

    def longestPalindrome(self, s: str) -> str:
        start, end = 0, 0  # 初始化最长回文子串的起始和结束位置
        for i in range(len(s)):
            # 以单个字符为中心扩展
            left1, right1 = self.expandAroundCenter(s, i, i)
            # 以两个相同字符为中心扩展
            left2, right2 = self.expandAroundCenter(s, i, i + 1)
            
            # 更新最长回文子串的边界
            if right1 - left1 > end - start:
                start, end = left1, right1
            if right2 - left2 > end - start:
                start, end = left2, right2
        
        return s[start:end + 1]  # 返回最长回文子串

class Solution3:
    #Manacher 算法，奇偶字符串统一转化为奇数字符串方便找回文中心（偶数字符串，间隔插入#）则
    def expand(self, s, left, right):
        # 扩展中心的方法，返回回文子串的半径长度
        while left >= 0 and right < len(s) and s[left] == s[right]:
            left -= 1
            right += 1
        return (right - left - 2) // 2  # 返回回文半径

    def longestPalindrome(self, s: str) -> str:
        end, start = -1, 0  # 初始化最长回文子串的起始和结束位置
        s = '#' + '#'.join(list(s)) + '#'  # 在每个字符之间插入 '#'
        arm_len = []  # 存储每个字符为中心的回文半径
        right = -1  # 当前已知最右边界
        j = -1  # 当前已知最右回文串的中心
        
        for i in range(len(s)):
            if right >= i:  # 如果当前字符在已知回文串的范围内
                i_sym = 2 * j - i  # 对称位置
                min_arm_len = min(arm_len[i_sym], right - i)  # 最小回文半径
                cur_arm_len = self.expand(s, i - min_arm_len, i + min_arm_len)  # 扩展
            else:
                cur_arm_len = self.expand(s, i, i)  # 从当前字符开始扩展
            
            arm_len.append(cur_arm_len)  # 更新回文半径
            
            if i + cur_arm_len > right:  # 更新右边界和中心
                j = i
                right = i + cur_arm_len
            
            if 2 * cur_arm_len + 1 > end - start:  # 更新最长回文子串的信息
                start = i - cur_arm_len
                end = i + cur_arm_len
        
        return s[start + 1:end + 1:2]  # 返回原字符串中的最长回文子串


# 测试用例
if __name__ == "__main__":
    solution = Solution3()
    
    # 测试用例 1
    print(solution.longestPalindrome("babad"))  # 输出: "bab" 或 "aba"
    
    # 测试用例 2
    print(solution.longestPalindrome("cbbd"))   # 输出: "bb"
    
    # 测试用例 3
    print(solution.longestPalindrome("a"))      # 输出: "a"
    
    # 测试用例 4
    print(solution.longestPalindrome("ac"))     # 输出: "a" 或 "c"
    
    # 测试用例 5
    print(solution.longestPalindrome("racecar"))# 输出: "racecar"
