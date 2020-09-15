# note we have decided that this module will not be included in the web app
def mid(lis_vec):
    # input must be list of vectors
    new_vec = []
    add = 0

    for vec_row in range(len(lis_vec[0])):
        for element in lis_vec:
            add += element[vec_row]
            # adds each element of vector
        new_vec.append(add / len(vec_row))
        # divides by number of vectors 
        add = 0

    return new_vec
