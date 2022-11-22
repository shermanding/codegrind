from extratypes import Tree

def traverse(sub_tree, height):
    left_height = 0
    right_height = 0
    
    if sub.l:
        left_height = traverse(sub.l, height + 1)
    if sub.r:
        right_height = traverse(sub.r, height + 1)

    if sub.l or sub.r:
        return max(left_height, right_height)
    else:
        return height

def solution(T):
    return traverse(T, 0)
