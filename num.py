import numpy as np

# Define matrices
A = np.array([[1, 2], [3, 4]])
B = np.array([[5, 6], [7, 8]])

# a) Add, subtract, multiply, and divide two matrices
add_result = A + B
subtract_result = A - B
multiply_result = A @ B  # Matrix multiplication
divide_result = A / B  # Element-wise division

# b) Find the determinant of matrices
det_A = np.linalg.det(A)
det_B = np.linalg.det(B)

# c) Check if matrices are symmetric
is_A_symmetric = np.allclose(A, A.T)
is_B_symmetric = np.allclose(B, B.T)

# d) Check if matrices are skew-symmetric
is_A_skew_symmetric = np.allclose(A, -A.T)
is_B_skew_symmetric = np.allclose(B, -B.T)

# e) Check if matrices are Hermitian
is_A_hermitian = np.allclose(A, np.conjugate(A.T))
is_B_hermitian = np.allclose(B, np.conjugate(B.T))

# f) Check if matrices are skew-Hermitian
is_A_skew_hermitian = np.allclose(A, -np.conjugate(A.T))
is_B_skew_hermitian = np.allclose(B, -np.conjugate(B.T))

# g) Check if matrices are orthogonal
is_A_orthogonal = np.allclose(A @ A.T, np.eye(A.shape[0]))
is_B_orthogonal = np.allclose(B @ B.T, np.eye(B.shape[0]))

# h) Check if matrices are upper or lower triangular
is_A_upper_triangular = np.allclose(A, np.triu(A))
is_A_lower_triangular = np.allclose(A, np.tril(A))
is_B_upper_triangular = np.allclose(B, np.triu(B))
is_B_lower_triangular = np.allclose(B, np.tril(B))

# i) Adjoint of the matrices (conjugate transpose)
adjoint_A = np.conjugate(A.T)
adjoint_B = np.conjugate(B.T)

# Print results
print("Addition:\n", add_result)
print("Subtraction:\n", subtract_result)
print("Multiplication:\n", multiply_result)
print("Division:\n", divide_result)
print("Determinant of A:", det_A)
print("Determinant of B:", det_B)
print("A is symmetric:", is_A_symmetric)
print("B is symmetric:", is_B_symmetric)
print("A is skew-symmetric:", is_A_skew_symmetric)
print("B is skew-symmetric:", is_B_skew_symmetric)
print("A is Hermitian:", is_A_hermitian)
print("B is Hermitian:", is_B_hermitian)
print("A is skew-Hermitian:", is_A_skew_hermitian)
print("B is skew-Hermitian:", is_B_skew_hermitian)
print("A is orthogonal:", is_A_orthogonal)
print("B is orthogonal:", is_B_orthogonal)
print("A is upper triangular:", is_A_upper_triangular)
print("A is lower triangular:", is_A_lower_triangular)
print("B is upper triangular:", is_B_upper_triangular)
print("B is lower triangular:", is_B_lower_triangular)
print("Adjoint of A:\n", adjoint_A)
print("Adjoint of B:\n", adjoint_B)
