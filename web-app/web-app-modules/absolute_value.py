def absolute_value(vector):
    from content.modules_for_Web_app.web_app_tool import string_vector
    vector = string_vector(vector)
    import math

    val = 0

    for element in vector:
        val += element**2

    return round(math.sqrt(val), 5)

