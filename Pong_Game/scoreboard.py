from turtle import Turtle

FONT = ("Germania One", 80, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.right_score = 0
        self.left_score = 0
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.goto(-100, 200)
        self.write(self.left_score, align="center", font=FONT)
        self.goto(100, 200)
        self.write(self.right_score, align="center", font=FONT)

    def left_point(self):
        self.left_score += 1
        self.update_scoreboard()

    def right_point(self):
        self.right_score += 1
        self.update_scoreboard()

    def draw_dashed_line(self):
        dash_line = Turtle()
        dash_line.color("white")
        dash_line.penup()
        dash_line.goto(0, 300)
        dash_line.setheading(270)
        dash_line.pendown()
        dash_line.pensize(2)

        for _ in range(30):
            dash_line.forward(10)  # Move forward by 10 units
            dash_line.penup()
            dash_line.forward(10)  # Skip 10 units (create a gap)
            dash_line.pendown()

        dash_line.hideturtle()
