

def transpose_matrix(matrix):
    rows = len(matrix)
    cols = len(matrix[0])


    transposed = [[0 for _ in range(rows)] for _ in range(cols)]

    # Transpose the matrix
    for i in range(rows):
        for j in range(cols):
            transposed[j][i] = matrix[i][j]

    return transposed

def input_matrix(rows, cols):
    matrix = []
    print(f"Enter the elements of a {rows}x{cols} matrix:")
    for i in range(rows):
        row = list(map(int, input().split()))
        matrix.append(row)
    return matrix



rows = int(input("Enter the number of rows: "))
cols = int(input("Enter the number of columns: "))

matrix = input_matrix(rows, cols)

transposed_matrix = transpose_matrix(matrix)

print("The transposed matrix is:")
for row in transposed_matrix:
    print(row)
