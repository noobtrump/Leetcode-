from typing import List
import itertools

class Solution1:
#库函数法：permutations是itertool里的全排列算法器，返回的是迭代器
    def permute(self, nums: List[int]) -> int:
        return list(itertools.permutations(nums))


class Solution2:
#回溯算法，
    def permute(self, nums: List[int]) -> List[List[int]]:
        result = []  # 用于存储所有排列结果
        
        def backtrack(start: int):
            if start == len(nums):  # 如果当前索引等于列表长度，说明一个排列完成
                result.append(nums[:])  # 将当前排列添加到结果中
                return
            
            for i in range(start, len(nums)):
                # 交换当前元素与起始元素
                nums[start], nums[i] = nums[i], nums[start]
                backtrack(start + 1)  # 递归调用，生成下一个位置的排列
                # 回溯，恢复原来的顺序
                nums[start], nums[i] = nums[i], nums[start]
        
        backtrack(0)  # 从索引0开始生成排列
        return result  # 返回所有生成的排列

# 测试用例
if __name__ == "__main__":
    solution = Solution1()
    print(solution.permute([1, 2, 3]))  # 输出所有[1, 2, 3]的排列