from collections import deque
from typing import Optional
class Solution1:
    def maxDepth(self, root):
        if root is None:
            return 0
        else:
            left_height = self.maxDepth(root. left)
            right_height = self.maxDepth(root. right)
            return max(left_height, right_height) + 1

# 定义树节点类
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val      # 节点的值
        self.left = left    # 左子节点
        self.right = right  # 右子节点

class Solution2:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        # 如果根节点为空，则树的深度为0
        if root is None:
            return 0
        
        # 使用队列进行广度优先搜索（BFS）
        Q = deque()  # 初始化一个双端队列
        Q.append(root)  # 将根节点入队
        
        ans = 0  # 深度计数器
        
        # 当队列不为空时，继续遍历树的每一层
        while Q:
            sz = len(Q)  # 当前层的节点数量
            
            # 遍历当前层的所有节点
            for _ in range(sz):
                node = Q.popleft()  # 从队列中取出当前节点
                
                # 如果当前节点有左子节点，将其入队
                if node.left:
                    Q.append(node.left)
                
                # 如果当前节点有右子节点，将其入队
                if node.right:
                    Q.append(node.right)
            
            ans += 1  # 每遍历一层，深度加1
        
        return ans  # 返回树的最大深度

# 测试用例
if __name__ == "__main__":
    # 创建一个示例二叉树：
    #      1
    #     / \
    #    2   3
    #   / \
    #  4   5
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    root.left.right = TreeNode(5)

    sol = Solution1()
    print("Maximum Depth:", sol.maxDepth(root))  # 输出: Maximum Depth: 3

                 