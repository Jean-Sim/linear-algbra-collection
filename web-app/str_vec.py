def string_vector(lis):
    lis = lis.strip("[")
    lis = lis.strip("]")
    # removes all unnecessary brackets from string
    lis = lis.split(",")
    # splits the string into an array 
    for element in range(len(lis)):
        lis[element] = float(lis[element])
        # turns the number string in to numbers
    return lis
