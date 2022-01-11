from __future__ import annotations


class Node:
    def __init__(self, value: int, left_child: Node = None, right_child: Node = None):
        self.value = value
        self.left_child = left_child
        self.right_child = right_child


def greatest_node(root: Node) -> int:
    v_root = root.value

    v_left = greatest_node(root.left_child) if root.left_child else 0
    v_right = greatest_node(root.right_child) if root.right_child else 0

    return max(v_root, v_left, v_right)


if __name__ == "__main__":
    tree = Node(2)

    tree.left_child = Node(3)
    tree.left_child.left_child = Node(5)
    tree.left_child.right_child = Node(8)

    tree.right_child = Node(4)
    tree.right_child.right_child = Node(11)

    print(f"{greatest_node(tree)=}")
