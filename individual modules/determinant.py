
def determinant(M):
    def normalise(M):
        new_M = []
        # creats a new Matrix
        for element in range(len(M)):
            new_M.append([])
            # appand new sub vectore 
            for element2 in range(len(M)):
                # inserts the element in correct position 
                new_M[element].append(M[element2][element])
        return new_M
    # changes Matrix in to the right shape 

    def rowMod(M, i, j, x):
        M[i] = [a + x * b for a, b in zip(M[i], M[j])]
    # modefies matrix element   

    def rowEchelon(M):
        M = normalise(M)
        # uses noramlise to make matrix fit the algorithem 
        row, col = 0, 0
        rows, cols = len(M), len(M[0])
        # defines size of matrix 
        while row < rows and col < cols:
            # starts while loop witch continues until matrix in echelon form 
            if M[row][col] == 0:
                for r in range(row + 1, rows):
                    if M[r][col] != 0:
                        rowMod(M, row, r, 1)
                        break

            if M[row][col] == 0:
                col += 1
                continue
            pivot = M[row][col]

            for r in range(row + 1, rows):
                if M[r][col] != 0:
                    rowMod(M, r, row, -M[r][col] / pivot)

            row += 1
            col += 1

        return normalise(M)
    #to compute the determinant we just bring the matrix in to echelon form and then multiply all diagunal values 

    num = 1
    new_M = rowEchelon(M)
    for element in range(len(M)):
        num = num*new_M[element][element]
    # multiplies elements diagonally
    return num

