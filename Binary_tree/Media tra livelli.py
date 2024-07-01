def visiting_tree_iterative(tree: dict[int, list[int]], root: int):
    stack: list[int] = [root]
    while stack: # while len(stack) != 0
        curr_node = stack.pop(0)
        if curr_node:
            print(curr_node)
            left_child, right_child =\
                tree[curr_node]
            if left_child:
                stack.append(left_child)
            if right_child:
                stack.append(right_child)