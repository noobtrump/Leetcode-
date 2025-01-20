from typing import Optional

# 定义树节点类
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val      # 节点的值
        self.left = left    # 左子节点
        self.right = right  # 右子节点

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        # 如果当前节点为空，返回空节点
        if not root:
            return root
        
        # 递归翻转左子树
        left = self.invertTree(root.left)
        
        # 递归翻转右子树
        right = self.invertTree(root.right)
        
        # 交换当前节点的左右子节点
        root.left, root.right = right, left
        
        # 返回翻转后的根节点
        return root

# 测试用例
if __name__ == "__main__":
    # 创建一个示例二叉树：
    #      4
    #     / \
    #    2   7
    #   / \ / \
    #  1  3 6  9
    root = TreeNode(4)
    root.left = TreeNode(2)
    root.right = TreeNode(7)
    root.left.left = TreeNode(1)
    root.left.right = TreeNode(3)
    root.right.left = TreeNode(6)
    root.right.right = TreeNode(9)

    sol = Solution()
    
    # 翻转二叉树并打印结果
    inverted_root = sol.invertTree(root)

    # 定义一个辅助函数用于打印二叉树的层序遍历结果
    def print_tree(node: Optional[TreeNode]):
        if not node:
            return "[]"
        
        result, queue = [], [node]
        
        while queue:
            current = queue.pop(0)
            if current:
                result.append(current.val)
                queue.append(current.left)
                queue.append(current.right)
            else:
                result.append(None)

        # 去掉末尾的 None 值以简化输出
        while result and result[-1] is None:
            result.pop()
        
        return result

    print("Inverted Tree:", print_tree(inverted_root))  
