from itertools import combinations

class Solution:
    def maximumValue(self, nums, k):
        n = len(nums)
        max_val = 0

        # 遍历所有长度为 2 * k 的组合
        for comb in combinations(range(n), 2 * k):
            left_or = 0
            right_or = 0
            
            # 分成两部分
            for i in range(k):
                left_or |= nums[comb[i]]
            for i in range(k, 2 * k):
                right_or |= nums[comb[i]]
            
            # 更新最大值
            max_val = max(max_val, left_or ^ right_or)

        return max_val

# 示例使用
sol = Solution()
nums = [1, 2, 3, 4, 5]
k = 2
print("Maximum value:", sol.maximumValue(nums, k))
