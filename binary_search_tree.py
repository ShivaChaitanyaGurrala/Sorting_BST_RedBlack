class BinarySearchTree:
    key = None
    root = None
    left = None
    right = None
    parent = None

    def insert(self, node):
        y = None
        x = self.root
        while x is not None:
            y = x
            if node.key < x.key:
                x = x.left
            else:
                x = x.right
        node.parent = y
        if y is None:
            self.root = node
        elif node.key < y.key:
            y.left = node
        else:
            y.right = node

    def search(self, tree, value):
        if tree is None or value == tree.key:
            return tree
        if value < tree.key:
            return tree.search(tree.left, value)
        else:
            return tree.search(tree.right, value)

    def inorder_walk(self, node):
        if node is not None:
            node.inorder_walk(node.left)
            #   if self.key is not None:
            print(node.key)
            node.inorder_walk(node.right)

    def iterative_search(self, key):
        while self is not None and key is not self.key:
            if key < self.key:
                self = self.left
            else:
                self = self.right
            return self

    def height(self, node):
        if node is None:
            return 0
        else:
            left_height = self.height(node.left)
            right_height = self.height(node.right)
        if left_height > right_height:
            return left_height + 1
        else:
            return right_height + 1

    def minimum(self, node):
        while node.left is not None:
            node = node.left
        return node

    def maximum(self, node):
        while node.right is not None:
            node = node.right
        return node

    def successor(self, node):
        if node.right is not None:
            return node.minimum(node.right)
        y = node.parent
        while y is not None and node == y.right:
            self = y
            y = y.parent
        return y

    def transplant(self, tree, u, v):
        if u.parent is None:
            tree.root = v
        elif u == u.parent.left:
            u.parent.left = v
        else:
            u.parent.right = v
        if v is not None:
            v.parent = u.parent

    def delete(self, tree, node):
        if node is not None:
            if node.left is None:
                node.transplant(tree, node, node.right)
            elif node.right is None:
                node.transplant(tree, node, node.left)
            else:
                y = node.minimum(node.right)
                if y.parent is not node:
                    node.transplant(tree, y, y.right)
                    y.right = node.right
                    y.right.p = y
                node.transplant(tree, node, y)
                y.left = node.left
                y.left.p = y
        else:
            print("Trying to Delete element that does not exist ")

''''======Testing======
import random

bst = BinarySearchTree()
node = BinarySearchTree()
node.key = 8
height_list = []
for i in range(1000):
    node = BinarySearchTree()
    node.key = random.randint(1, 1000)
    bst.insert(node)
    height_list.append(bst.height(bst.root))
    del node

print("--------Inorder-------")
bst.inorder_walk(bst.root)
bst.inorder_walk(bst.root)
print("-----Minimum Val------")
print(bst.minimum(bst.root).key)
print("-----Maximum Val------")
print(bst.maximum(bst.root).key)
print("-------Successor-------")
print(bst.successor(bst.root).key)
print("----Change in Height----")
print(height_list)
print("-------End height-------")
print(bst.height(bst.root))
print("--------Deletion--------")
bst.delete(bst.root, bst.root.left.left)
# bst.inorder_walk(bst.root)
print("New Height :")
print(bst.height(bst.root))
print("----Search------------")
x = bst.search(bst.root, 5)
print(x.key) if x is not None else print("No Element match")
# print(bst.root.left.key)'''
