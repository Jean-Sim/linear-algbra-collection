def cross_product(vec):
    from content.modules_for_Web_app.web_app_tool import final_step
    vector_1, vector_2 = final_step(vec)

    new_vector = [1, 1, 1]

    new_vector[0] *= round(vector_1[1]*vector_2[2] - vector_1[2]*vector_2[1], 5)
    new_vector[1] *= round(vector_1[2]*vector_2[0] - vector_1[0]*vector_2[2], 5)
    new_vector[2] *= round(vector_1[0]*vector_2[1] - vector_1[1]*vector_2[0], 5)

    return new_vector