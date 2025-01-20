from typing import List, Optional

# 定义树节点类
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val      # 节点的值
        self.left = left    # 左子节点
        self.right = right  # 右子节点

class Solution:
    # 中序遍历的递归方法
    def inorder(self, root: Optional[TreeNode], res: List[int]) -> None:
        # 如果当前节点为空，直接返回
        if not root:
            return
        
        # 递归遍历左子树
        self.inorder(root.left, res)
        
        # 访问当前节点，将其值添加到结果列表中
        res.append(root.val)
        
        # 递归遍历右子树
        self.inorder(root.right, res)

    # 主方法，执行中序遍历并返回结果
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        res = []  # 初始化结果列表，用于存储遍历结果
        self.inorder(root, res)  # 调用递归方法进行中序遍历
        return res  # 返回结果列表

# 测试用例
if __name__ == "__main__":
    # 创建一个示例二叉树：
    #      1
    #       \
    #        2
    #       /
    #      3
    root = TreeNode(1)                   # 创建根节点，值为1
    root.right = TreeNode(2)             # 创建右子节点，值为2
    root.right.left = TreeNode(3)        # 创建左子节点，值为3，作为2的左子节点

    sol = Solution()                      # 创建 Solution 类的实例
    print("Inorder Traversal:", sol.inorderTraversal(root))  # 输出中序遍历结果: [1, 3, 2]
