#input rules 
"""
1 to declare a matrix use those () ... a element inside the matrix must be separated by ; ... please input each matrix column as a vector as shown in rule 2
2 to declare vector use those [] ... numbers inside must be separated by ,
3 if the module you are using take multiple inputs use | to separate them
"""
# Note the order of output is as follows: Skalar<-Vector<-Matrix   

def string_vector(lis):
    lis = lis.strip("[")
    lis = lis.strip("]")
    # removes unnecessary elements from string
    lis = lis.split(",")
    # split in to individual numbers
    for element in range(len(lis)):
        lis[element] = float(lis[element])
        # turns each string out of the list 
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
    # defines new_st and splits the two inputs
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
    # checks whether it is a matrix, vector or num
    # and then inserts them in the correct position so that the return order is |num , vector , matrix|

    return new_st[0], new_st[1]
