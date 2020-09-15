def rowEchelon(M):
    def normalise(M):
        # normalise is used to translate between deifrent way of inputing a matrix
        new_M = []
        for element in range(len(M)):
            new_M.append([])
            for element2 in range(len(M)):
                new_M[element].append(M[element2][element])
        return new_M

    def rowMod(M, i, j, x):
        M[i] = [a + x * b for a, b in zip(M[i], M[j])]
    # define row mod function

    M = normalise(M)
    row, col = 0, 0
    rows, cols = len(M), len(M[0])
    while row < rows and col < cols:
        if M[row][col] == 0:
            for r in range(row +1, rows):
                if M[r][col] != 0:
                    rowMod(M, row, r, 1)
                    break
    # uses while loop to go through matrix 
        if M[row][col] == 0:
            col += 1
            continue
        pivot = M[row][col]

        for r in range(row +1, rows):
            if M[r][col] != 0:
                rowMod(M, r, row, -M[r][col] / pivot)

        row += 1
        col += 1

    return normalise(M)
