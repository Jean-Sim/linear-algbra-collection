def string_vector(lis):
    lis = lis.strip("[")
    lis = lis.strip("]")
    # removes all unnecessary brackets from string vector
    lis = lis.split(",")
    # splits the vector in string form into an array 
    for element in range(len(lis)):
        lis[element] = float(lis[element])
        # turns the number string in to numbers
    return lis
