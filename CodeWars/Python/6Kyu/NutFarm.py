def shake_tree(tree):
    for index, item in enumerate(tree):
        index+=2
        print(index)
    # return '\n'.join(tree)

a = [' o o o  ', ' /    / ', '   /    ', '  /  /  ', '   ||   ', '   ||   ', '   ||   ']

print(shake_tree(a))