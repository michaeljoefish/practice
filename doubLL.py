class Node:
    def __init__(self, var, prev, next):
        self.var = var
        self.prev = prev
        self.next = next

class DLL:
    def __init__(self):
        self.head = None
        self.tail = None
    
    def add_tail(self, var):
        if(self.head == None):
            self.head = Node(var, None, None)
            self.tail = self.head
        else:
            temp = Node(var, prev=self.tail, next=None)
            self.tail.next = temp
            self.tail = temp
    def add_head(self, var):
        if(self.head == None):
            self.head = Node(var, None, None)
            self.tail = self.head
        else:
            temp = Node(var, prev=None, next=self.head)
            self.head.prev = temp
            self.head = temp
    def pop_head(self):
        if self.head != None:
            if self.head == self.tail:
                var = self.head.var
                self.head = None
                self.tail = None
                return var
            else:
                var = self.head.var
                self.head = self.head.next
                self.head.prev = None
                return var
        return None
    def pop_tail(self):
        if self.tail != None:
            if self.head == self.tail:
                var = self.tail.var
                self.head = None
                self.tail = None
                return var
            else:
                var = self.tail.var
                self.tail = self.tail.prev
                self.tail.next = None
                return var
        return None

    def __str__(self):
        temp_lst = []
        node_ptr = self.head
        while(node_ptr != None):
            temp_lst.append(str(node_ptr.var))
            node_ptr = node_ptr.next
        
        return f"[{', '.join(temp_lst)}]"

def main():
    dll = DLL()
    dll.add_tail(5)
    dll.add_tail(6)
    dll.add_tail(7)
    print(dll)
    dll.pop_head()
    print(dll)
    dll.pop_head()
    print(dll)
    dll.pop_head()
    print(dll)
    dll.pop_head()
    print(dll)
    dll.add_tail(7)
    dll.add_head(8)
    print(dll)
    dll.pop_tail()
    print(dll)
    dll.pop_tail()
    print(dll)
    dll.pop_tail()
    print(dll)

    dll.add_head(1)
    dll.add_tail(2)
    dll.add_head(3)
    print(dll)



if __name__ == "__main__":
    main()
