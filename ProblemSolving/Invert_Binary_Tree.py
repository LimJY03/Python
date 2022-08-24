'''
Given the root of a binary tree, invert the tree, and return its root.

Example 1:
> Input: root = [4, 2, 7, 1, 3, 6, 9]
> Output: [4, 7, 2, 9, 6, 3, 1]

Example 2:
> Input: root = [2, 1, 3]
> Output: [2, 3, 1]

Example 3:
> Input: root = []
> Output: []

Constraints:
> The number of nodes in the tree is in the range [0, 100].
> -100 <= Node.val <= 100

src: "https://leetcode.com/problems/invert-binary-tree/"
'''

def invert_tree(root: list) -> list:

    # Example 3
    if not root: return root

    temp = inverted = []
    i = 0

    while root:
        temp = root[0:(2 ** i)]
        root = root[(2 ** i):]
        inverted.extend(temp[::-1])
        i += 1

    return inverted

print(
    invert_tree(root=[1, 3, 5, 2, 4, 5, 6 ,9, 7 ,8, 9, 2, 1, 6, 5]),
    invert_tree(root=[4, 2, 7, 1, 3, 6, 9]),
    invert_tree(root=[2, 1, 3]),
    invert_tree(root=[])
)