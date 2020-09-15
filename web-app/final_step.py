def final_step(st):
    st = st.split("|")
    new_st = []
    # defines new_list and splits the input into two 

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
    # checks weather it is scalar, matrix, or vector then inserts it into the correct position  
    else:
        new_st.insert(0, float(st[0]))
    # checks whether it is matrix, vector or num
    # and inserts them in the correct position so that num , vector , matrix
    return new_st[0], new_st[1]
