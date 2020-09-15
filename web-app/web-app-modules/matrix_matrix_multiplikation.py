def MM_multiplication(vec):
    #needs square matrix
    from content.modules_for_Web_app.web_app_tool import final_step
    matrix_1, matrix_2 = final_step(vec)

    end_matrix = []
    for element in range(len(matrix_1)):
        end_matrix.append([])
        for none in matrix_1:
            end_matrix[element].append(0)

    for i in range(len(matrix_1)):
        for j in range(len(matrix_1)):
            for k in range(len(matrix_1)):
                end_matrix[i][j] += matrix_1[i][k] * matrix_2[k][j]

    return end_matrix
