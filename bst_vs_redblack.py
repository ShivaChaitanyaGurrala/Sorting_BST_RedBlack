import binary_search_tree
import red_black
import random
#import matplotlib.pyplot as plt

bst = binary_search_tree.BinarySearchTree()
rb = red_black.RedBlack()
bst_height_list = []
rb_height_list = []
for i in range(1000):
    node = binary_search_tree.BinarySearchTree()
    value = random.randint(1, 1000)
    node.key = value
    bst.insert(node)
    rb.insert(rb, value)
    bst_height_list.append(bst.height(bst.root))
    rb_height_list.append(rb.height(rb.root))
    del node
print("Change of heights over 1000 random inserts: ")
print(bst_height_list)
print(rb_height_list)

'''---Matplotlib is not installed on linprog
------ And hence commenting out this code----
plt.plot(bst_height_list)
plt.plot(rb_height_list)
plt.title('Height on no.of insertions')
plt.xlabel('Num of Iteration')
plt.ylabel('Height')
plt.legend(['BST', 'RedBlack'])
plt.savefig('Analysis.png')'''
print("------------------------------")
print("Create new instance of size 17 to check deletion")
bst = binary_search_tree.BinarySearchTree()
rb = red_black.RedBlack()
for i in range(17):
    node = binary_search_tree.BinarySearchTree()
    value = random.randint(1, 15)
    node.key = value
    bst.insert(node)
    rb.insert(rb, value)
    bst_height_list.append(bst.height(bst.root))
    rb_height_list.append(rb.height(rb.root))
    del node
'''print("Inorder Traversals Before Deletion :")
print("BST")
bst.inorder_walk(bst.root)
print("-------------------------------------")
print("Red Black")
rb.inorder_walk(rb.root)'''
print("-------------------------------------")
print("Deleting BST left node ")
bst.delete(bst.root, bst.root.left)
print("Height : {0}".format(bst.height(bst.root)))
print("Deleting BST root node ")
bst.delete(bst.root, bst.root)
print("Height : {0}".format(bst.height(bst.root)))
print("Deleting BST root -> right node ")
bst.delete(bst.root, bst.root.right)
print("Height : {0}".format(bst.height(bst.root)))
print("----------------------------------")
print("Deleting red Black left node ")
rb.delete(rb, rb.root.left)
print("Height : {0}".format(rb.height(rb.root)))
print("Deleting red Black root-> right node ")
rb.delete(rb, rb.root.right)
print("Height : {0}".format(rb.height(rb.root)))
print("Deleting red Black left node ")
rb.delete(rb, rb.root.right)
print("Height : {0}".format(rb.height(rb.root)))
print("--------------------------------")
