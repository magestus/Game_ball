import chargrid
resize(14, 50)
chargrid.add_rectangle(0, 0, *get_size())
add_vertical_line(5, 10, 13)
add_vertical_line(2, 9, 12, "!")
add_horizontal_line(3, 10, 20, "+")
add_rectangle(0, 0, 5, 5, "%")
add_rectangle(5, 7, 12, 40, "#", True)
add_rectangle(7, 9, 10, 38, " ")
add_text(8, 10, "This is the CharGrid module")
add_text(1, 32, "Pleasantville", "@")
add_rectangle(6, 42, 11, 46, fill=True)
render(False)

print