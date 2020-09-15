def cross_product(vector_1, vector_2):
    new_vector = []
    # defines empty list that will be contain the future end vectore 
    
    new_vector.append(vector_1[1]*vector_2[2] - vector_1[2]*vector_2[1])
    new_vector.append(vector_1[2]*vector_2[0] - vector_1[0]*vector_2[2])
    new_vector.append(vector_1[0]*vector_2[1] - vector_1[1]*vector_2[0])
    # does the correct multiplications and subtractions 

    return new_vector
