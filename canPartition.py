from typing import List
from functools import cache

class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        @cache  # 使用缓存装饰器来避免重复计算
        def dfs(i: int, j: int) -> bool:
            if i < 0:  # 如果索引小于0，表示没有更多元素可用
                return j == 0  # 检查是否能够找到和为0的子集
            
            # 考虑当前元素 nums[i]
            # 如果当前元素可以用于达到目标 j，则继续递归
            return (j >= nums[i] and dfs(i - 1, j - nums[i])) or dfs(i - 1, j)

        s = sum(nums)  # 求出数组所有元素的总和
        # 检查总和是否为偶数，并尝试找到一个子集使其和为 s // 2
        return s % 2 == 0 and dfs(len(nums) - 1, s // 2)

# 测试用例
if __name__ == "__main__":
    solution = Solution()
    
    # 测试用例 1
    test_nums1 = [1, 5, 11, 5] 
    result1 = solution.canPartition(test_nums1)
    print(f"Test case {test_nums1}: {result1} (Expected: True)")

    # 测试用例 2
    test_nums2 = [1, 2, 3, 5] 
    result2 = solution.canPartition(test_nums2)
    print(f"Test case {test_nums2}: {result2} (Expected: False)")

    # 测试用例 3
    test_nums3 = [2, 2, 1, 1] 
    result3 = solution.canPartition(test_nums3)
    print(f"Test case {test_nums3}: {result3} (Expected: True)")

    # 测试用例 4
    test_nums4 = [] 
    result4 = solution.canPartition(test_nums4)
    print(f"Test case {test_nums4}: {result4} (Expected: True)") # 空数组可以被分割成两个空子集

    # 测试用例 5
    test_nums5 = [10] 
    result5 = solution.canPartition(test_nums5)
    print(f"Test case {test_nums5}: {result5} (Expected: False)") # 单个元素无法分割

