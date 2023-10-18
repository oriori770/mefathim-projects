import random

# anytree needs to be installed for the next line!
# pip install anytree
from anytree import Node
from anytree.exporter import UniqueDotExporter
from TreeNode import TreeNode

def create_random_binary_tree(length):
    if length == 0:
        return None

    value = random.randint(1, 1000)
    # First You should implement the class "TreeNode"
    node = TreeNode(value)

    if length > 1:
        left_length = random.randint(0, length - 1)
        right_length = length - 1 - left_length
        node.left = create_random_binary_tree(left_length)
        node.right = create_random_binary_tree(right_length)

    return node


# Convert TreeNode to anytree.Node
def convert_to_anytree_node(tree_node):
    if tree_node is None:
        return None
    node = Node(str(tree_node.value))
    if not tree_node.left and not tree_node.right:
        return node
    if tree_node.left:
        node.children += (convert_to_anytree_node(tree_node.left),)
    else:
        node.children += (Node(''),)
    if tree_node.right:
        node.children += (convert_to_anytree_node(tree_node.right),)
    else:
        node.children += (Node(''),)
    return node


# Create a random binary tree
random_tree = create_random_binary_tree(50)  # Change the number as needed

# Convert the random tree to an anytree structure
anytree_root = convert_to_anytree_node(random_tree)

# print(anytree_root)

# Visualize the tree
# graphviz needs to be installed for the next line!
# graphviz
UniqueDotExporter(anytree_root).to_picture('tree.png')
# print(random_tree.left.value)
# print(random_tree.right.value)
# print(random_tree.right)
# print(random_tree.left)
