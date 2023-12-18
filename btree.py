def isTree(algo) -> bool:

    if not isinstance(algo, list):
        return False

    if len(algo) != 3:
        return False
    
    left_node = algo[1]
    right_node = algo[2]
    
    if not left_node and right_node: 
        return False
 
    return True

if __name__ == "__main__":

    bt1 = [None, None, None] # True
    bt2 = [22, None, None]   # True
    bt3 = [22, [11, None, None], None]   # True
    bt4 = [22, [11, None, None], [33, None, None]]   # True
    bt5 = [22, [33, None, None]] # False

    print(isTree(bt1))   # True
    print(isTree(bt2))   # True
    print(isTree(bt3))   # True
    print(isTree(bt4))   # True
    print(isTree(bt5))   # False


