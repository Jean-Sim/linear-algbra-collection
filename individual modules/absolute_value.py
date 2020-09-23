def absolute_value(vector):
    import sqrt from math
    # impor the sqrt function from python standart math module
    val = 0
    # defines variable

    for element in vector:
        val += element**2
        # adds the squares of all vectore elements to the variable

    return math.sqrt(val)

