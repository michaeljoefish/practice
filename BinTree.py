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
        elif (var > node.var):
            if node.right == None:
                node.right = Node(var, None, None)
            else:
                self.insert(var, node.right)

    def minNode(self, node):
        """
        Precondition: node can't be None
        """
        node_ptr = node
        while node_ptr.left != None:
            node_ptr = node_ptr.left
        return node_ptr

    def maxNode(self, node):
        """
        Precondition: node can't be None
        """
        node_ptr = node
        while node_ptr.right != None:
            node_ptr = node_ptr.right
        return node_ptr
    
    def delete(self, var):
        self.root = self.remove(var, self.root)

    def remove(self, var, node):
        if not node:
            return None
        
        if node.var == var:
            new_node = None
            if (node.left == None) and (node.right):
                new_node = node.right
            elif (node.left) and (node.right == None):
                new_node = node.left
            elif (node.left) and (node.right):
                new_node = node.right
                self.minNode(node.right).left = node.left
            return new_node
        
        elif var < node.var:
            node.left = self.remove(var, node.left)
        else:
            node.right = self.remove(var, node.right)
        return node

    
    def display(self):
        self.RML(self.root, 0)

    def RML(self, node, depth: int):
        if node != None:
            self.RML(node.right, depth+1)

            print(f"{(" "*(depth*3))}{node.var}")
            self.RML(node.left, depth+1)

    def height(self):
        return self._height(self.root, 0)

    def _height(self, node, h) -> int:
        if node == None:
            return h
        h_left = self._height(node.left, h+1)
        h_right = self._height(node.right, h+1)

        return max(h_left, h_right)
    
    def search(self, var):
        return self._search(self.root, var)

    def _search(self, node, var):
        if node == None:
            return False
        if node.var == var:
            return True
        elif var < node.var:
            return self._search(node.left, var)
        else:
            return self._search(node.right, var)

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
    
    print()
    print()
    ibt.delete(2)
    ibt.display()

    print()
    print()
    ibt.delete(7)
    ibt.display()

    print()
    print()
    ibt.delete(5)
    ibt.display()

    

if __name__ == "__main__":
    main()