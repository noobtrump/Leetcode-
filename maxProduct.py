from typing import List
class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        if not nums: return
        # 目前的累乘
        cur_pro = 1
        # 前面最小的正数
        min_pos = 1
        # 前面最大的负数
        max_neg = float("-inf")
        # 结果
        res = float("-inf")
        for num in nums:
            cur_pro *= num
            # 考虑三种情况
            # 大于0
            if cur_pro > 0:
                res = max(res, cur_pro // min_pos)
                min_pos = min(min_pos, cur_pro)
            # 小于0
            elif cur_pro < 0:
                if max_neg != float("-inf"):
                    res = max(res, cur_pro // max_neg)
                else:
                    res = max(res, num)
                max_neg = max(max_neg, cur_pro)
            # 等于0 
            else:
                cur_pro = 1
                min_pos = 1
                max_neg = float("-inf")
                res = max(res, num)
        return res 
if __name__ == "__main__":
    solution = Solution()
    test_nums = [2, 3, -2, 4]  # 示例输入
    result = solution.maxProduct(test_nums)
    print("Maximum product of subarray:", result)  # 输出结果