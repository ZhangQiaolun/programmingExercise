class BinarySearchTree(object):
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None

    def find(self, x):
        if x==self.key:
            return self
        elif x<self.key and self.left:
            return self.left.find(x)
        elif x>self.key and self.right:
            return self.right.find(x):
        else:
            return None

    def findMin(self):
        if self.left:
            return self.left.findMin()
        else return self

    # 递归形式的findMax
    def findMax(self):
        if self.right:
            return self.right.findMax()
        else return self

    # 非递归形式的findMax
    def findMax2(self):
        tree = self
        if tree:
            while tree.right:
                tree = tree.right
        return tree


