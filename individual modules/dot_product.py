def dot_product(vector_1, vector_2):
    dot_product = 0
    # defines end variable  
    for index in range(len(vector_1)):
        # goes through each element in the two vectors 
        try:
            dot_product += vector_1[index] * vector_2[index]
            #multiplies them then adds them to dot_product
            
        except IndexError:
            "incorrect dimensions please check input"

    return dot_product
