# 定义二叉树节点结构
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def sumNumbers(self, root: TreeNode) -> int:
        def dfs(node, cur_num):
            if not node:
                return 0
            cur_num = cur_num * 10 + node.val
            # 到达叶子节点，返回当前拼接的数字
            if not node.left and not node.right:
                return cur_num
            # 递归遍历左右子树，累加结果
            return dfs(node.left, cur_num) + dfs(node.right, cur_num)

        return dfs(root, 0)


# 测试示例1
# 构建树 [1,2,3]
root1 = TreeNode(1)
root1.left = TreeNode(2)
root1.right = TreeNode(3)
sol = Solution()
print(f"示例1输出：{sol.sumNumbers(root1)}")  # 输出 25

# 测试示例2
# 构建树 [4,9,0,5,1]
root2 = TreeNode(4)
root2.left = TreeNode(9)
root2.right = TreeNode(0)
root2.left.left = TreeNode(5)
root2.left.right = TreeNode(1)
print(f"示例2输出：{sol.sumNumbers(root2)}")  # 输出 1026