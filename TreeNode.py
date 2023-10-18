from anytree import Node
from anytree.exporter import UniqueDotExporter


class TreeNode:
    def __init__(self, value=None, left=None, right=None):
        self.value = value
        self.left = None
        self.right = None
    pass


node1 = TreeNode(50)


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


anytree_root = convert_to_anytree_node(node1)
UniqueDotExporter(anytree_root).to_picture('tree.png')
