def vector_addition(vec):
    from content.modules_for_Web_app.web_app_tool import final_step
    vector_1, vector_2 = final_step(vec)
    for element in range(len(vector_2)):
        try:
            vector_1[element] += vector_2[element]
        except IndexError:
            vector_1.append(vector_2[element])

    return vector_1

