def bar(matrix: list) -> None:
    no_of_rows = len(matrix)
    for i in range(no_of_rows):
        for j in range(len(matrix[i])):
            matrix[i][j] *= (i+j)


def foo(matrix: list) -> int:
    total = 0
    bar(matrix)
    print(matrix)
    for row in matrix:
        for element in row:
            total += element
    return total

print(foo([[1,2],[3,4,5]]))

def foob(n:str) -> str:
    if n == "":
        return n
    return (n + "#"*len(n) + foob(n[1:-1]))

print(foob("Hello"))