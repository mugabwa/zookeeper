import math


def round_down(number: float, decimals: int = 2):
    """
    Returns a value rounded down to a specific number of decimal places.
    """
    if number < 0:
        return round(number, 2)
    if not isinstance(decimals, int):
        raise TypeError("decimal places must be an integer")
    elif decimals < 0:
        raise ValueError("decimal places has to be 0 or more")
    elif decimals == 0:
        return math.floor(number)

    factor = 10 ** decimals
    return math.floor(number * factor) / factor


def scalarMultiplication(matrix1=None, scal=None):
    if matrix1 is None:
        size2 = list(map(int, input("Enter size of matrix: ").split()))
        a = size2[0]
        b = size2[1]
        print("Enter matrix:")
        matrix1 = [list(map(float, input().split())) for x in range(a)]
        const = int(input("Enter constant: "))
        matrix2 = [[round(matrix1[x][y] * const, 2) for y in range(b)] for x in range(a)]

    else:
        a = len(matrix1)
        b = len(matrix1[0])
        matrix2 = [[matrix1[x][y] * float(scal) for y in range(b)] for x in range(a)]
    for x in range(len(matrix2)):
        for y in range(len(matrix2[0])):
            if matrix2[x][y] == -0:
                matrix2[x][y] = 0
    return matrix2


def addition():
    size2 = list(map(int, input("Enter size of first matrix: ").split()))
    a = size2[0]
    b = size2[1]
    print("Enter first matrix:")
    matrix1 = [list(map(float, input().split())) for x in range(a)]

    size1 = list(map(int, input("Enter size of second matrix: ").split()))
    c = size1[0]
    d = size1[1]
    print("Enter second matrix:")
    matrix2 = [list(map(float, input().split())) for x in range(c)]
    if a == c and b == d:
        matrix3 = [[matrix1[x][y] + matrix2[x][y] for y in range(b)] for x in range(a)]
        print("The result is:")
        for val in matrix3:
            print(" ".join(str(z) for z in val))
    else:
        print("Error")
    print()


def matrixMultiplication():
    size2 = list(map(int, input("Enter size of first matrix: ").split()))
    a = size2[0]
    b = size2[1]
    print("Enter first matrix:")
    matrix1 = [list(map(float, input().split())) for x in range(a)]

    size1 = list(map(int, input("Enter size of second matrix: ").split()))
    c = size1[0]
    d = size1[1]
    print("Enter second matrix:")
    matrix2 = [list(map(float, input().split())) for x in range(c)]
    if b == c:
        result = list()
        for x in range(a):
            mat = matrix1[x]
            mat1 = list()
            length = len(mat)
            for y in range(d):
                temp = 0
                for z in range(length):
                    temp += (mat[z] * matrix2[z][y])
                mat1.append(temp)
            result.append(mat1)
        print("The result is:")
        for val in result:
            print(" ".join(str(val1) for val1 in val))
    else:
        print("Error")
    print()


def transpose(matrix=None):
    if matrix is None:
        print()
        print("""1. Main diagonal
    2. Side diagonal
    3. Vertical line
    4. Horizontal line""")
        choice = int(input("Your choice: "))
        size = list(map(int, input("Enter size of first matrix: ").split()))
        a = size[0]
        b = size[1]
        print("Enter first matrix:")
        matrix = [list(map(float, input().split())) for x in range(a)]
    else:
        choice = 1
        a = len(matrix)
        b = len(matrix[0])
    result1 = [[0 for x in range(a)] for y in range(b)]
    if choice == 1:
        for x in range(a):
            for y in range(b):
                result1[y][x] = matrix[x][y]
    elif choice == 2:
        ## For side diagonal: you can reversed(range(rows)) and reversed(range(columns)) in loops
        # and perform a main diagonal transpose.
        for x in reversed(range(a)):
            x1 = a - x
            for y in reversed(range(b)):
                y1 = b - y
                result1[y1 - 1][x1 - 1] = matrix[x][y]
    elif choice == 3:
        ## For vertical line: you can use your every row reversed by matrix[i].reverse() in loop.
        for x in range(a):
            for y in reversed(range(b)):
                y1 = b - y
                result1[x][y1 - 1] = matrix[x][y]
    elif choice == 4:
        ## For vertical line: you can use your every column reversed by matrix[i].reverse() in loop.
        for x in reversed(range(a)):
            x1 = a - x
            for y in range(b):
                result1[x1 - 1][y] = matrix[x][y]
    else:
        pass
    return result1


def minor(matrix, i, j):
    return [row[:j] + row[j + 1:] for row in (matrix[:i] + matrix[i + 1:])]


def getDeterminant(matrix):
    if len(matrix) == 2:
        return (matrix[0][0] * matrix[1][1]) - (matrix[0][1] * matrix[1][0])
    if len(matrix) == 1:
        return matrix[0][0]
    determ = 0
    for x in range(len(matrix)):
        determ += ((-1) ** x) * matrix[0][x] * getDeterminant(minor(matrix, 0, x))
    return determ


def cofactor(matrix):
    matrix1 = [[matrix[x][y] for y in range(len(matrix[0]))] for x in range(len(matrix))]
    for x in range(len(matrix)):
        for y in range(len(matrix[0])):
            matrix1[x][y] = ((pow(-1, x + y)) * getDeterminant(minor(matrix, x, y)))
    return matrix1


def determinant(matrix=None):
    if matrix is None:
        r, c = map(int, input("Enter matrix size: ").split())
        matrix = [list(map(float, input().split())) for x in range(r)]
    return getDeterminant(matrix)


def inverse():
    r, c = map(int, input("Enter matrix size: ").split())
    matrix = [list(map(float, input().split())) for x in range(r)]
    det = determinant(matrix)
    if det == 0:
        return 'error'
    co_trans = transpose(cofactor(matrix))
    return scalarMultiplication(co_trans, 1 / det)


while True:
    print("""1. Add matrices
2. Multiply matrix by a constant
3. Multiply matrices
4. Transpose matrix
5. Calculate a determinant
6. Inverse matrix
0. Exit""")
    response = int(input("Your choice: "))
    if response == 0:
        break
    elif response == 1:
        addition()
    elif response == 2:
        sresult = scalarMultiplication()
        print("The result is:")
        for val in sresult:
            print(" ".join(str(z) for z in val))
        print()
    elif response == 3:
        matrixMultiplication()
    elif response == 4:
        tresult = transpose()
        print("The result is:")
        for val in tresult:
            print(" ".join(str(val1) for val1 in val))
        print()
    elif response == 5:
        dresult = determinant()
        print("The result is:")
        print(dresult)
        print()
    elif response == 6:
        result = inverse()
        if result == 'error':
            print("The matrix has no inverse")
        else:
            print("The result is:")
            for val in result:
                print(" ".join(str(round_down(val1, 2)) for val1 in val))
        print()
    else:
        pass
