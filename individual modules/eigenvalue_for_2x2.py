def eigenvalue_2x2(matrix):
    import math

    # solves quadratic eq
    result1 = (matrix[0][0] + matrix[1][1]) / 2 + math.sqrt(
        ((matrix[0][0] + matrix[1][1]) / 2) ** 2 - matrix[0][0] * matrix[1][1])

    result2 = (matrix[0][0] + matrix[1][1]) / 2 - math.sqrt(
        ((matrix[0][0] + matrix[1][1]) / 2) ** 2 - matrix[0][0] * matrix[1][1])

    # returns two eigenvalues 
    return result1, result2

