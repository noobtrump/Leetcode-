from typing import List

class Solution1:
    #回溯算法+动态规划预处理（双指针判断回文串及长度）
    def partition(self, s: str) -> List[List[str]]:
        n = len(s)  # 获取字符串的长度
        # 创建一个n x n的布尔矩阵f，f[i][j]表示s[i:j+1]是否是回文串
        f = [[True] * n for _ in range(n)]

        # 填充布尔矩阵f
        for i in range(n - 1, -1, -1):  # 从后往前遍历字符串
            for j in range(i + 1, n):  # 从当前位置向后遍历
                f[i][j] = (s[i] == s[j]) and f[i + 1][j - 1]  # 判断是否为回文串

        ret = list()  # 存储最终结果
        ans = list()  # 存储当前路径（当前分割的回文串）

        def dfs(i: int):
            if i == n:  # 如果到达字符串末尾，说明找到了一种有效分割
                ret.append(ans[:])  # 将当前路径的副本添加到结果中
                return
            
            for j in range(i, n):  # 遍历从i到n的所有位置
                if f[i][j]:  # 如果s[i:j+1]是回文串
                    ans.append(s[i:j+1])  # 将回文串添加到当前路径中
                    dfs(j + 1)  # 深度优先搜索下一个位置
                    ans.pop()  # 回溯，移除最后添加的回文串

        dfs(0)  # 从索引0开始进行深度优先搜索
        return ret  # 返回所有有效的回文分割结果


from functools import cache  # 导入缓存装饰器以优化回文检查
class Solution2:
    def partition(self, s: str) -> List[List[str]]:
        n = len(s)  # 获取字符串的长度

        ret = list()  # 存储所有有效的回文分割结果
        ans = list()  # 存储当前路径（当前分割的回文串）

        @cache  # 使用缓存装饰器来优化isPalindrome函数
        def isPalindrome(i: int, j: int) -> int:
            # 检查子字符串s[i:j+1]是否为回文
            if i >= j:
                return 1  # 如果i大于等于j，说明是回文（单个字符或空字符串）
            return isPalindrome(i + 1, j - 1) if s[i] == s[j] else -1  # 如果首尾字符相同，递归检查内部字符

        def dfs(i: int):
            if i == n:  # 如果到达字符串末尾，说明找到了一种有效分割
                ret.append(ans[:])  # 将当前路径的副本添加到结果中
                return
            
            for j in range(i, n):  # 遍历从i到n的所有位置
                if isPalindrome(i, j) == 1:  # 如果s[i:j+1]是回文串
                    ans.append(s[i:j+1])  # 将回文串添加到当前路径中
                    dfs(j + 1)  # 深度优先搜索下一个位置
                    ans.pop()  # 回溯，移除最后添加的回文串

        dfs(0)  # 从索引0开始进行深度优先搜索
        isPalindrome.cache_clear()  # 清除缓存，以防影响后续调用
        return ret  # 返回所有有效的回文分割结果


# 测试用例
if __name__ == "__main__":
    solution = Solution2()
    
    # 测试用例1：输入 "aab"，应输出 [["aa", "b"], ["a", "a", "b"]]
    print("Test Case 1 Output:", solution.partition("aab"))  
    
    # 测试用例2：输入 "a"，应输出 [["a"]]
    print("Test Case 2 Output:", solution.partition("a"))  
    
    # 测试用例3：输入 "abba"，应输出 [["a", "b", "b", "a"], ["a", "bb", "a"], ["abba"]]
    print("Test Case 3 Output:", solution.partition("abba"))  