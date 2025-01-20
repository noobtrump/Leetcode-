import heapq # 导入heapq模块以使用堆功能
from typing import List

class Solution1:
    def minOperations(self, nums: List[int], k: int) -> int:
        # 使用小根堆来存储元素
        que = []
        
        # 将所有元素推入优先队列
        for x in nums:
            heapq.heappush(que, x)

        ans = 0  # 操作计数器

        # 当优先队列中至少有两个元素且最小元素小于 k 时继续操作
        while len(que) >= 2 and que[0] < k:
            x = heapq.heappop(que)  # 取出最小元素 x
            y = heapq.heappop(que)  # 取出第二小元素 y
            
            # 使用 int 避免溢出（Python 的 int 可以处理大数）
            newValue = min(x, y) * 2 + max(x, y)
            heapq.heappush(que, newValue)  # 将新值推入优先队列
            ans += 1  # 增加操作计数

        return ans  # 返回总操作次数
 

class Solution2:
    def minOperations(self, h: List[int], k: int) -> int:
        # 将列表h转换为最小堆
        heapq.heapify(h)
        ans = 0  # 初始化操作计数
        
        # 当堆顶元素小于目标值k时，继续进行操作
        while h and h[0] < k:
            # 弹出堆顶元素（当前最小值）
            x = heapq.heappop(h)
            # 将新值放回堆中，新的值是当前最小值x乘以2
            heapq.heappush(h, x * 2)
            ans += 1  # 增加操作计数
        
        return ans  # 返回所需的操作次数

# 测试用例
if __name__ == "__main__":
    sol = Solution1()
    
    # 测试用例1
    nums1 = [1, 2, 3, 4]
    k1 = 5
    print("Test Case 1 - Minimum operations:", sol.minOperations(nums1, k1))  # 输出: 应为2
    
    # 测试用例2
    nums2 = [8, 6, 7]
    k2 = 10
    print("Test Case 2 - Minimum operations:", sol.minOperations(nums2, k2))   # 输出: 应为0
    
    # 示例输入
    nums3 = [1999999998, 999999999]
    k3 = 3000000000
    print("Example Test Case - Minimum operations:", sol.minOperations(nums3, k3)) 
