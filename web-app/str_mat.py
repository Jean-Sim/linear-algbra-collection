def string_matrix(mis):
    mis = mis.strip("(")
    mis = mis.strip(")")
    # removes the unnecessary elements from the string
    mis = mis.split(";")
    # splits it into individual vector parts
    for element in range(len(mis)):
        mis[element] = string_vector(mis[element])
        # turns the string in to a list
    return mis
