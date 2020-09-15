def solve_eq(inp):
    from content.modules_for_Web_app.web_app_tool import final_step
    result, matrix = final_step(inp)
    def abs(lis):
        if lis < 0:
            lis = lis*-1
        return lis

    for k in range(len(result)):
        if abs(matrix[k][k]) < 0:
            for i in range(k+1, len(result)):
                if abs(matrix[i][k]) > abs(matrix[k][k]):
                    for j in range(k,len(result)):
                        matrix[k][j], matrix[i][j] = matrix[i][j], matrix[k][j]
                    result[k], result[i] = result[i], result[k]
                    break
        pivot = matrix[k][k]
        for j in range(k, len(result)):
            matrix[k][j] /= pivot
        result[k] /= pivot

        for i in range(len(result)):
            if i == k or matrix[i][k] == 0:
                continue
            factore = matrix[i][k]
            for j in range(k, len(result)):
                matrix[i][j] -= factore * matrix[k][j]
            result[i] -= factore*result[k]
    return matrix, result



