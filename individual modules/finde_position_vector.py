def finde_position_vector(point_1, point_2):
    for element in range(len(point_1)):
        # goes through each element between those points and subtracts them 
        point_2[element] = point_2[element] - point_1[element]

    return point_2
