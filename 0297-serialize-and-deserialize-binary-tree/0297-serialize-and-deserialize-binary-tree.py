# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        ans = []
        que = [root]
        while(que):
            node = que.pop(0)
            if node:
                que.append(node.left)
                que.append(node.right)
                ans.append(str(node.val))
            else:
                ans.append('#')
        print(",".join(ans))
        return ",".join(ans)
        

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        bt = data.split(',')
        print(bt)
        if bt[0] == '#':
            return None
        val = bt.pop(0)
        root = TreeNode(val)
        que = []
        que.append(root)
        while(que):
            node = que.pop(0)
            val = bt.pop(0)
            if val == '#':
                node.left = None
            else:
                l = TreeNode(val)
                node.left = l
                que.append(node.left)
            val = bt.pop(0)
            if val == '#':
                node.right = None
            else:
                l = TreeNode(val)
                node.right = l
                que.append(node.right)
        return root
                
        
        
        
        

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))