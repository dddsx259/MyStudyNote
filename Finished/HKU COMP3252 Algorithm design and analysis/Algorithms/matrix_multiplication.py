A = [[1, 0, 0, 0], [0, 1, 0, 0], [0, 0, 1, 0], [0, 0, 0, 1]]
B = [[1, 1, 4, 5], [1, 4, 1, 9], [1, 9, 8, 1], [0, 1, 1, 4]]

def square_add(A, B):
    return [[A[i][j] + B[i][j] for j in range(len(A[0]))] for i in range(len(A))]

def square_sub(A, B):
    return [[A[i][j] - B[i][j] for j in range(len(A[0]))] for i in range(len(A))]

def square_mul(A, B):
    n = len(A)
    if n == 1:
        return [[A[0][0] * B[0][0]]]
    
    if n % 2 != 0:
        raise ValueError("Matrix size must be a power of 2 for Strassen's algorithm.")
    
    half = n // 2

    A11 = [row[:half] for row in A[:half]]
    A12 = [row[half:] for row in A[:half]]
    A21 = [row[:half] for row in A[half:]]
    A22 = [row[half:] for row in A[half:]]

    B11 = [row[:half] for row in B[:half]]
    B12 = [row[half:] for row in B[:half]]
    B21 = [row[:half] for row in B[half:]]
    B22 = [row[half:] for row in B[half:]]

    M1 = square_mul(square_add(A11, A22), square_add(B11, B22))
    M2 = square_mul(square_add(A21, A22), B11)
    M3 = square_mul(A11, square_sub(B12, B22))
    M4 = square_mul(A22, square_sub(B21, B11))  
    M5 = square_mul(square_add(A11, A12), B22)
    M6 = square_mul(square_sub(A21, A11), square_add(B11, B12))
    M7 = square_mul(square_sub(A12, A22), square_add(B21, B22))

    C11 = square_add(square_sub(square_add(M1, M4), M5), M7)
    C12 = square_add(M3, M5)
    C21 = square_add(M2, M4)
    C22 = square_add(square_add(M1, M3), square_sub(M6, M2))

    C = [[0] * n for _ in range(n)]
    for i in range(half):
        for j in range(half):
            C[i][j] = C11[i][j]
            C[i][j + half] = C12[i][j]
            C[i + half][j] = C21[i][j]
            C[i + half][j + half] = C22[i][j]
    
    return C

print(square_mul(A, B))