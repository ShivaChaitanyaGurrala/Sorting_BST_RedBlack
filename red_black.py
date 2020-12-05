import enum
import random


class col(enum.Enum):
    Red = 1
    Black = 2


class Node:
    def __init__(self, value):
        self.left = None
        self.right = None
        self.parent = None
        self.key = value
        self.color = col.Red


class RedBlack:
    def __init__(self):
        self.NIL = Node(0)
        self.NIL.color = col.Black
        self.NIL.left = None
        self.NIL.right = None
        self.root = self.NIL

    def left_rotate(self, tree, node):
        y = node.right
        node.right = y.left
        if y.left is not None:
            y.left.parent = node
        y.parent = node.parent
        if node.parent is None:
            tree.root = y
        elif node == node.parent.left:
            node.parent.left = y
        else:
            node.parent.right = y
        y.left = node
        node.parent = y

    def insert(self, tree, key):
        node = Node(key)
        node.parent = None
        node.key = key
        node.left = tree.NIL
        node.right = tree.NIL
        y = None
        x = tree.root
        while x is not tree.NIL:
            y = x
            if node.key < x.key:
                x = x.left
            else:
                x = x.right
        node.parent = y
        if y is None:
            tree.root = node
        elif node.key < y.key:
            y.left = node
        else:
            y.right = node
        node.left = tree.NIL
        node.right = tree.NIL
        node.color = col.Red
        if node.parent is None:
            node.color = 0
            return
        if node.parent.parent is None:
            return
        self.insert_fixup(tree, node)

    def right_rotate(self, tree, y):
        x = y.left
        y.left = x.right
        if x.right is not None:
            x.right.parent = y
        x.parent = y.parent
        if y.parent is None:
            tree.root = x
        elif y == y.parent.left:
            y.parent.left = x
        else:
            y.parent.right = x
        x.right = y
        y.parent = x

    def insert_fixup(self, tree, z):
        while z.parent.color == col.Red:
            if z.parent == z.parent.parent.left:
                y = z.parent.parent.right
                if y.color == col.Red:
                    z.parent.color = col.Black
                    y.color = col.Black
                    z.parent.parent.color = col.Red
                    z = z.parent.parent
                else:
                    if z == z.parent.right:
                        z = z.parent
                        self.left_rotate(tree, z)
                    z.parent.color = col.Black
                    z.parent.parent.color = col.Red
                    self.right_rotate(tree, z.parent.parent)
            else:
                y = z.parent.parent.left
                if y.color == col.Red:
                    z.parent.color = col.Black
                    y.color = col.Black
                    z.parent.parent.color = col.Red
                    z = z.parent.parent
                else:
                    if z == z.parent.left:
                        z = z.parent
                        self.right_rotate(tree, z)
                    z.parent.color = col.Black
                    z.parent.parent.color = col.Red
                    self.left_rotate(tree, z.parent.parent)
            if z == tree.root:
                break
        tree.root.color = col.Black

    def inorder_walk(self, tree):
        if tree.key is not 0:
            self.inorder_walk(tree.left)
            print("key is {0} and color is {1}".format(tree.key, tree.color))
            self.inorder_walk(tree.right)

    def height(self, node):
        if node.left is None and node.right is None:
            return 0
        else:
            left_height = self.height(node.left)
            right_height = self.height(node.right)
        if left_height > right_height:
            return left_height + 1
        else:
            return right_height + 1

    def transplant(self, tree, u, v):
        if u.parent == tree.NIL:
            tree.root = v
        elif u == u.parent.left:
            u.parent.left = v
        else:
            u.parent.right = v
        v.parent = u.parent

    def delete(self,tree,z):
        y = z
        y_original_color = y.color
        if z.left == tree.NIL:
            x = z.right
            self.transplant(tree, z, z.right)
        elif z.right == tree.NIL:
            x = z.left
            self.transplant(tree, z, z.left)
        else:
            y = self.minimum(z.right)
            y_original_color = y.color
            x = y.right
            if y.parent == z:
                x.parent = y
            else:
                self.transplant(tree, y, y.right)
                y.right = z.right
                y.right.parent = y
            self.transplant(tree, z, y)
            y.left =z.left
            y.left.parent = y
            y.color = z.color
        if y_original_color is col.Black:
            self.delete_fixup(tree, x)

    def minimum(self, node):
        while node.left is not None:
            node = node.left
        return node.parent

    def maximum(self, node):
        while node.right is not None:
            node = node.right
        return node.parent

    def delete_fixup(self, tree, x):
        while x is not tree.root and x.color is col.Black:
            if x is x.parent.left:
                w = x.parent.right
                if w.color is col.Red:
                    w.color = col.Black
                    x.parent.color = col.Red
                    self.left_rotate(tree, x.parent)
                    w = x.parent.right
                if w.left.color == col.Black and w.right.color == col.Black:
                    w.color = col.Red
                    x = x.parent
                else:
                    if w.right.color == col.Black:
                        w.left.color = col.Black
                        w.color = col.Red
                        self.right_rotate(tree, w)
                        w = x.parent.right
                    w.color = x.parent.color
                    x.parent.color = col.Black
                    w.right.color = col.Black
                    self.left_rotate(tree, x.parent)
                    x = tree.root
            else:
                w = x.parent.left
                if w.color is col.Red:
                    w.color = col.Black
                    x.parent.color = col.Red
                    self.right_rotate(tree, x.parent)
                    w = x.parent.left
                if w.right.color == col.Black and w.left.color == col.Black:
                    w.color = col.Red
                    x = x.parent
                else:
                    if w.left.color == col.Black:
                        w.right.color = col.Black
                        w.color = col.Red
                        self.left_rotate(tree, w)
                        w = x.parent.left
                    w.color = x.parent.color
                    x.parent.color = col.Black
                    w.left.color = col.Black
                    self.right_rotate(tree, x.parent)
                    x = tree.root
        x.color = col.Black





''' ===Testing===
rb = RedBlack()
print(rb.height(rb.root))
for i in range(5):
    x = random.randint(1, 1000)
    rb.insert(rb, x)
rb.inorder_walk(rb.root)
print("------Height-------")
print(rb.height(rb.root))
rb.delete(rb, rb.root.left.left)
rb.delete(rb, rb.root.left)
print("------Height-------")
print(rb.height(rb.root))'''