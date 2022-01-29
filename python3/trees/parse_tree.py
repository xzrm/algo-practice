import operator


class Node:
    def __init__(self, value, left_child=None, right_child=None):
        self.value = value
        self.left_child = left_child
        self.right_child = right_child


def build_parse_tree(expr):
    fp_list = expr.split()
    stack = []
    tree = Node("")
    stack.append(tree)
    curr_tree = tree

    for i in fp_list:
        if i == "(":
            curr_tree.left_child = Node("")
            stack.append(curr_tree)
            curr_tree = curr_tree.left_child

        elif i in ["+", "-", "*", "/"]:
            curr_tree.value = i
            curr_tree.right_child = Node("")
            stack.append(curr_tree)
            curr_tree = curr_tree.right_child

        elif i == ")":
            curr_tree = stack.pop()

        elif i not in ["+", "-", "*", "/", ")"]:
            try:
                curr_tree.value = int(i)
                parent = stack.pop()
                curr_tree = parent

            except ValueError:
                raise ValueError("token '{}' is not a valid integer".format(i))

    return tree


def evaluate(parse_tree):
    operators = {
        "+": operator.add,
        "-": operator.sub,
        "*": operator.mul,
        "/": operator.truediv,
    }

    if parse_tree.left_child and parse_tree.right_child:
        fn = operators[parse_tree.value]
        return fn(evaluate(parse_tree.left_child), evaluate(parse_tree.right_child))
    return parse_tree.value


# note: spaces between chars required for .split() to work
# else some additional actions required to obtain a list of allowed chars
s = "( 3 + ( 4 * 5 ) )"
s = "( ( 10 + 5 ) * 3 )"
pt = build_parse_tree(s)
print(evaluate(pt))
