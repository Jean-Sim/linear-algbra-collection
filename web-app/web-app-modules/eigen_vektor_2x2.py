def eigen_vectore_2x2(matrix):
    from content.modules_for_Web_app.eigenvalue_for_2x2 import eigenvalue_2x2
    from content.modules_for_Web_app.web_app_tool import string_matrix
    from content.modules_for_Web_app.solve_eq import solve_eq
    matrix = string_matrix(matrix)

    matrix[0,0] -= eigenvalue_2x2(matrix)
    matrix[1,1] -= eigenvalue_2x2(matrix)


    return solve_eq(matrix, [0,0])

