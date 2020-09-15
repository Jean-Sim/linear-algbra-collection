def angle(vec):
    import math
    from content.modules_for_Web_app.web_app_tool import final_step
    vector_1, vector_2 = final_step(vec)

    def dot_product(vector_1, vector_2):
        dot_product = 0
        for index in range(len(vector_1)):
            try:
                dot_product += vector_1[index] * vector_2[index]
            except IndexError:
                ""
        return dot_product

    def absolute_value(vector):
        import math
        val = 0

        for element in vector:
            val += element ** 2

        return math.sqrt(val)

    result = math.acos(dot_product(vector_2, vector_1)/(absolute_value(vector_2)*absolute_value(vector_1)))

    return round(math.degrees(result), 5)