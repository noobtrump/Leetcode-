from typing import List  # 导入List以便使用类型提示
import itertools  # 导入itertools模块以使用组合功能

class Solution1:
    #DFS去遍历方法，然后递归
    def letterCombinations(self, digits: str) -> List[str]:
        # 数字到字母的映射
        MAPPING = {
            '2': 'abc', 
            '3': 'def', 
            '4': 'ghi', 
            '5': 'jkl',
            '6': 'mno', 
            '7': 'pqrs', 
            '8': 'tuv', 
            '9': 'wxyz'
        }
        
        n = len(digits)  # 获取输入数字字符串的长度
        if n == 0:  # 如果输入为空，返回空列表
            return []
        
        ans = []  # 初始化结果列表
        path = [''] * n  # 创建一个长度为n的路径列表，用于存储当前组合
        
        def dfs(i: int) -> None:
            if i == n:  # 当索引i等于数字长度时，说明已完成一个组合
                ans.append(''.join(path))  # 将当前组合添加到结果中
                return
            
            for c in MAPPING[digits[i]]:  # 遍历当前数字对应的字母
                path[i] = c  # 将字母放入路径中
                dfs(i + 1)  # 递归调用，处理下一个数字
        
        dfs(0)  # 从索引0开始进行深度优先搜索
        return ans  # 返回所有可能的字母组合


class Solution2:
    #迭代和队列，使用phone列表来泰国ASCII码映射字母
    #详情：在 ASCII 码中，数字字符 '0' 到 '9' 的 ASCII 码值是 48 到 57，而使用 ord(digit) - 50 来计算当前数字对应的字母索引。
    #例子：对于数字字符 '2'，其 ASCII 值为 50，因此 ord('2') - 50 的结果为 0，这对应于 phone 列表中的第一个元素 'abc'。
    def letterCombinations(self, digits: str) -> List[str]:
        # 如果输入为空，返回空列表
        if not digits:
            return []
        
        # 数字到字母的映射
        phone = ['abc', 'def', 'ghi', 'jkl', 'mno', 'pqrs', 'tuv', 'wxyz']
        queue = ['']  # 初始化队列，开始时包含一个空字符串
        
        # 遍历每个数字
        for digit in digits:
            # 当前队列的长度
            for _ in range(len(queue)):
                # 从队列中取出当前组合
                tmp = queue.pop(0)
                # 获取当前数字对应的字母
                for letter in phone[ord(digit) - 50]:  # 使用ASCII码计算索引
                    queue.append(tmp + letter)  # 将新组合添加到队列
        
        return queue  # 返回所有可能的字母组合
    
# 测试用例
if __name__ == "__main__":
    solution = Solution2()
    
    # 测试用例1：输入 "23"，应输出所有可能的字母组合
    print("Test Case 1 Output:", solution.letterCombinations("23"))  
    # 输出: ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"]

    # 测试用例2：输入 ""（空字符串），应返回空列表
    print("Test Case 2 Output:", solution.letterCombinations(""))  
    # 输出: []

    # 测试用例3：输入 "2"，应输出对应的字母组合 ["a", "b", "c"]
    print("Test Case 3 Output:", solution.letterCombinations("2"))  
    # 输出: ["a", "b", "c"]
