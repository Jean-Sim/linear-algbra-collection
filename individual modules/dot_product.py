def dot_product(vector_1, vector_2):
    dot_product = 0
    # defines end variable  
    for index in range(len(vector_1)):
        try:
            dot_product += vector_1[index] * vector_2[index]
        except IndexError:
            "incorrect dimensions please check input"

    return dot_product
