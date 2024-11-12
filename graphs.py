from typing import Any

class Node:
    def __init__(self, value: Any):
        self.value = value

class Graph:
    def __init__(self, node_list: list[Node]):

        self.node_list = node_list
        self.size = len(node_list)
        self.adj_matrix = [[0 for i in range(self.size)] for j in range(self.size)]
    
    def add_edge(self, node_1: int, node_2: int):
        self.adj_matrix[node_1][node_2] = 1
        self.adj_matrix[node_2][node_1] = 1
    
    def rem_edge(self, node_1: int, node_2: int):
        self.adj_matrix[node_1][node_2] = 0
        self.adj_matrix[node_2][node_1] = 0
    
    def get_neighbors(self, node: int):
        ret_list = []
        for i in range(self.size):
            if self.adj_matrix[node][i]:
                ret_list.append(i)
        
        return ret_list
    
    def display(self):
        for i in range(self.size):
            for j in range(self.size):
                print(self.adj_matrix[i][j], end=" ")
            
            print()
    

def main():
    node_list = [Node(0), Node(1), Node(2), Node(3)]
    bob = Graph(node_list)

    bob.add_edge(0,1)
    bob.add_edge(0,2)
    bob.add_edge(0,3)
    bob.add_edge(2,1)
    bob.add_edge(2,3)

    bob.display()

    bob.rem_edge(2,1)
    bob.rem_edge(2,3)

    print()
    bob.display()

if __name__ == "__main__":
    main()