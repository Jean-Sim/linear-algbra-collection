def finde_position_vector(vec):
    from content.modules_for_Web_app.web_app_tool import final_step
    point_1, point_2 = final_step(vec)

    for element in range(len(point_1)):
        point_2[element] = round(point_2[element] - point_1[element], 5)

    return point_2
