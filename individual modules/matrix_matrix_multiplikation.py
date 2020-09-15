def MM_multiplication(matrix_1, matrix_2):
    end_matrix = []
    for element in range(len(matrix_1)):
        end_matrix.append([])
        for none in matrix_1:
            end_matrix[element].append(0)
    # creates endmatrix

    for i in range(len(matrix_1)):
        for j in range(len(matrix_1)):
            for k in range(len(matrix_1)):
                end_matrix[i][j] += matrix_1[i][k] * matrix_2[k][j]
    # goes through each amtrix and adds there product to end matrix

    return end_matrix

