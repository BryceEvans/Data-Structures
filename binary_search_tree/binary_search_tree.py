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
        pass

    def get_max(self):
        pass

    def for_each(self, cb):
        pass