import turtle as t

def draw_rectangle(width, height, line_color, fill_color):
    t.begin_fill()
    t.color(line_color, fill_color)
    for _ in range(2):
        t.forward(width)
        t.left(90)
        t.forward(height)
        t.left(90)
    t.end_fill()

def draw_square(size, line_color, fill_color):
    t.begin_fill()
    t.color(line_color, fill_color)
    for _ in range(4):
        t.forward(size)
        t.left(90)
    t.end_fill()

def draw_shape(x, y, width, height, line_color, fill_color):
    t.penup()
    t.goto(x - width / 2, y - height / 2)
    t.pendown()
    draw_rectangle(width, height, line_color, fill_color)

t.speed(0)
t.bgcolor("white")

house_width, house_height, roof_height, door_width, door_height, window_size, chimney_height = 200, 150, 80, 40, 80, 30, 50
line_color, fill_color = "black", "white"

draw_shape(0, 0, house_width, house_height, line_color, fill_color)
draw_shape(0, -house_height / 2, house_width, roof_height, line_color, fill_color)
draw_shape(0, -house_height / 2, door_width, door_height, line_color, fill_color)

window_positions = [(-60, -20), (60, -20), (-30, 30), (30, 30)]
for position in window_positions:
    draw_shape(position[0], position[1], window_size, window_size, line_color, fill_color)

draw_shape(20, roof_height + chimney_height, 40, chimney_height, line_color, fill_color)

t.exitonclick()