

#
def multiply_matrices(matrix1, matrix2):
    result = [[0 for _ in range(len(matrix2[0]))] for _ in range(len(matrix1))]
    for i in range(len(matrix1)):

        for j in range(len(matrix2[0])):

            for k in range(len(matrix2)):
                result[i][j] += matrix1[i][k] * matrix2[k][j]

    return result


def input_matrix(rows, cols):
    matrix = []
    print(f"Enter the elements of a {rows}x{cols} matrix:")
    for i in range(rows):
        row = list(map(int, input().split()))
        matrix.append(row)
    return matrix


rows1 = int(input("Enter the number of rows in matrix 1: "))
cols1 = int(input("Enter the number of columns in matrix 1: "))

rows2 = int(input("Enter the number of rows in matrix 2: "))
cols2 = int(input("Enter the number of columns in matrix 2: "))


if cols1 != rows2:
    print("Matrix multiplication is not possible. The number of columns in matrix 1 must be equal to the number of rows in matrix 2.")
else:
    print("Matrix 1:")
    matrix1 = input_matrix(rows1, cols1)

    print("Matrix 2:")
    matrix2 = input_matrix(rows2, cols2)
    result_matrix = multiply_matrices(matrix1, matrix2)
    print("The result of matrix multiplication is:")
    for row in result_matrix:
        print(row)
