def eigenvalue_2x2(matrix):
    from content.modules_for_Web_app.web_app_tool import string_matrix
    matrix = string_matrix(matrix)

    import math

    result1 = (matrix[0][0] + matrix[1][1]) / 2 + math.sqrt(
        ((matrix[0][0] + matrix[1][1]) / 2) ** 2 - matrix[0][0] * matrix[1][1])

    result2 = (matrix[0][0] + matrix[1][1]) / 2 - math.sqrt(
        ((matrix[0][0] + matrix[1][1]) / 2) ** 2 - matrix[0][0] * matrix[1][1])

    return round(result1, 5), round(result2, 5)

