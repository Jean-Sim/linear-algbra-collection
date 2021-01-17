"""
to declear a matrix use those () element inside saparated by ;
to declear a vector use those [] saparated by ,
to declear a element in a vector use those , to seperate the numbers
to separate diffrint inputs use |
"""

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

def string_matrix(mis):
    mis = mis.strip("(")
    mis = mis.strip(")")
    # removes unnecessary elements from string
    mis = mis.split(";")
    # splits it into individual vector parts

    for element in range(len(mis)):
        mis[element] = string_vector(mis[element])
        # turns string in to list
    return mis


def final_step(st):
    st = st.split("|")
    new_st = []
    # defines new list and splits the two inputs

    if "([" in st[0]:
        new_st.append(string_matrix(st[0]))
    elif "[" in st[0]:
        new_st.append(string_vector(st[0]))
    else:
        new_st.append(float(st[0]))
    # checks whether it is matrix, vector or num

    if "([" in st[1]:
        new_st.append(string_matrix(st[1]))
    elif "[" in st[1]:
        if type(new_st[0]) == float:
             new_st.append(string_vector(st[1]))
        else:
            new_st.insert(0, string_vector(st[1]))
    else:
        new_st.insert(0, float(st[0]))
    # checks whether it is matrix, vector or num
    # and inserts them in the correct position so that num , vector , matrix

    return new_st[0], new_st[1]
















