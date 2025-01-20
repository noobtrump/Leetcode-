from typing import List

class Solution1:
    def minOperations(self, nums: List[int], k: int) -> int:
        # 初始化结果计数器
        res = 0
        
        # 遍历列表中的每个数字
        for num in nums:
            # 如果当前数字小于 k，计数器加一
            if num < k:
                res += 1
        
        # 返回小于 k 的数字总数
        return res

class Solution2:
    #简便的一行
    def minOperations(self, nums: List[int], k:int) ->int:
        return sum(x < k for x in nums)

def test_minOperations():
    solution = Solution2()
    
    # 测试用例 1
    nums1 = [1, 2, 3, 4, 5]
    k1 = 3
    print(solution.minOperations(nums1, k1))  # 输出: 2 (1 和 2 小于 3)
    
    # 测试用例 2
    nums2 = [5, 6, 7, 8]
    k2 = 5
    print(solution.minOperations(nums2, k2))  # 输出: 0 (没有数字小于 5)
    
    # 测试用例 3
    nums3 = [0, -1, -2, 3]
    k3 = 1
    print(solution.minOperations(nums3, k3))  # 输出: 3 (0, -1 和 -2 小于 1)
    
    # 测试用例 4
    nums4 = [10, 20, 30]
    k4 = 100
    print(solution.minOperations(nums4, k4))  # 输出: 3 (所有数字都小于100)
    
    # 测试用例 5
    nums5 = []
    k5 = 5
    print(solution.minOperations(nums5, k5))  # 输出: 0 (空列表)

# 执行测试用例
test_minOperations()
