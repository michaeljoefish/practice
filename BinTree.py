class Node:
    def __init__(self, var: int, left, right):
        self.var = var
        self.left = left
        self.right = right

class IBT:
    def __init__(self):
        self.root = None
    
    def add(self, var: int):
        if self.root == None:
            self.root = Node(var, None, None)
        else:
            self.insert(var, self.root)

    def insert(self, var, node):
        if (var < node.var):
            if node.left == None:
                node.left = Node(var, None, None)
            else:
                self.insert(var, node.left)
        if (var > node.var):
            if node.right == None:
                node.right = Node(var, None, None)
            else:
                self.insert(var, node.right)
    
    def display(self):
        self.RML(self.root, 0)

    def RML(self, node, depth: int):
        if node != None:
            self.RML(node.right, depth+1)

            print(f"{(" "*(depth*3))}{node.var}")
            self.RML(node.left, depth+1)


def main():
    ibt = IBT()

    ibt.add(5)
    print(ibt.root)
    
    ibt.add(3)
    ibt.add(2)
    ibt.add(4)

    ibt.add(7)
    ibt.add(6)
    ibt.add(8)

    ibt.display()

if __name__ == "__main__":
    main()