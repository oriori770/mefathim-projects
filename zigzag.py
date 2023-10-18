import tree_utils
from anytree.exporter import UniqueDotExporter

random_tree = tree_utils.create_random_binary_tree(10)
anytree_root = tree_utils.convert_to_anytree_node(random_tree)
UniqueDotExporter(anytree_root).to_picture('tree2.png')


def max_zigzap(tree, direction=None):
    if tree is None:
        return -1
    sum_zz_right = max_zigzap(tree.right, 'right')
    sum_zz_left = max_zigzap(tree.left, 'left')
    if direction is None:
        return max(sum_zz_left, sum_zz_right)
    elif direction == 'left':
        return sum_zz_right + 1
    elif direction == 'right':
        return sum_zz_left + 1


def is_leaf(node):
    return not (node.left and node.right)


def len_trre(trre):
    if is_leaf(trre):
        return 0
    return max(len_trre(trre.right), len_trre(trre.left)) + 1


# print(len_trre(random_tree))
print(max_zigzap(random_tree))
print(random_tree.value)