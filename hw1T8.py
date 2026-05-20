class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def recoverTree(self, root: TreeNode) -> None:
        # 记录错误节点
        self.first = None
        self.second = None
        # 记录前一个节点
        self.prev = TreeNode(float('-inf'))

        # 中序遍历
        def inorder(node):
            if not node:
                return
            inorder(node.left)

            # 检测逆序
            if self.first is None and self.prev.val > node.val:
                self.first = self.prev
            if self.first is not None and self.prev.val > node.val:
                self.second = node
            self.prev = node

            inorder(node.right)

        inorder(root)
        # 交换两个错误节点的值
        self.first.val, self.second.val = self.second.val, self.first.val


# 辅助函数：列表转树（方便测试）
def build_tree(nodes):
    if not nodes:
        return None
    from collections import deque
    root = TreeNode(nodes[0])
    q = deque([root])
    i = 1
    while q and i < len(nodes):
        node = q.popleft()
        if nodes[i] is not None:
            node.left = TreeNode(nodes[i])
            q.append(node.left)
        i += 1
        if i < len(nodes) and nodes[i] is not None:
            node.right = TreeNode(nodes[i])
            q.append(node.right)
        i += 1
    return root


# 辅助函数：树转列表（方便输出）
def tree_to_list(root):
    if not root:
        return []
    res = []
    from collections import deque
    q = deque([root])
    while q:
        node = q.popleft()
        if node:
            res.append(node.val)
            q.append(node.left)
            q.append(node.right)
        else:
            res.append(None)
    # 去掉末尾的None
    while res and res[-1] is None:
        res.pop()
    return res


# 测试示例1
root1 = build_tree([1, 3, None, None, 2])
sol = Solution()
sol.recoverTree(root1)
print("示例1输出:", tree_to_list(
    root1))  # [3, 1, None, None, 2] 修正后为 [3, 1, None, None, 2] → 交换1和3 → [1, 3, None, None, 2] 对应输出 [1,3,None,None,2]

# 测试示例2
root2 = build_tree([3, 1, 4, None, None, 2])
sol.recoverTree(root2)
print("示例2输出:", tree_to_list(root2))  # [3, 1, 4, None, None, 2] 修正后为 [2, 1, 4, None, None, 3]