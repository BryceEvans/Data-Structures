class BinarySearchTree:
    def __init__(self, value):
        # the value at the current node
        self.value = value
        # reference to this node's left child
        self.left = None
        # reference to this node's right child
        self.right = None

    def insert(self, value):
        # 1. Check if the new node's value is less than
        # a. Is there a child? If not, insert new Node
        # b. Repeat the process (recursion)
        if value <= self.value:
            if not self.left:
                self.left = BinarySearchTree(value)
            else:
                self.left.insert(value)
        # 2. Check if new node's value is greater than
        # a. Is there a child? If not, insert ner node
        # b. Repeat the process (recursion)
        elif value > self.value:
            if not self.right:
                self.right = BinarySearchTree(value)
            else:
                self.right.insert(value)

    def contains(self, target):
        # if target equals value, return true
        if self.value == target:
            return True
        # if target greater than value and what's left, search left with recursion
        elif self.value > target and self.left:
            return self.left.contains(target)
        # if target greater than value and what's right, search right with recursion
        elif self.value < target and self.right:
            return self.right.contains(target)
        # if not found, return false
        else:
            return False
        
    def get_max(self):
        # If nothing to right, return value
        if not self.right:
            return self.value
        # If something to the right, go right recursively
        if self.right:
            return self.right.get_max()

    def for_each(self, cb):
        # if left, go left
        if self.left:
            self.left.for_each(cb)
        # if right, go right
        if self.right:
            self.right.for_each(cb)
        cb(self.value)
        
        