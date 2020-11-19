def angle(vector_1, vector_2):
    #uses dotproduct = |vector_1|*|vector_2|*cos(a)
    from math import sqrt
    def dot_product(vector_1, vector_2):
        dot_product = 0
        for index in range(len(vector_1)):
            # interrates through both vectore at the same time
            try:
                dot_product += vector_1[index] * vector_2[index]
                # multiplies both vectore elements and adds them to dot_product
            except IndexError:
                "ERROR"

        return dot_product

    def absolute_value(vector):
        val = 0
        for element in vector:
            val += element ** 2
            # takes each value form vectore square a´nd adds them

        return sqrt(val)
    # uses fromula from line 2 | result in arch length turned to degrees 
    return math.degrees(math.acos(dot_product(vector_2,vector_1)/absolute_value(vector_2)*absolute_value(vector_1)))
