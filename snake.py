from turtle import Turtle

# starting positions for turtle objects
STARTING_POSITIONS = [(20, 0), (0, 0), (-20, 0)]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snake:

    def __init__(self):
        self.snake = []
        self.create_snake()
        self.head = self.snake[0]

    # generate 3 starting snake segments in the middle of the screen
    def create_snake(self):
        for position in STARTING_POSITIONS:
            new_segment = Turtle("square")
            new_segment.penup()
            new_segment.goto(position)
            new_segment.color("LimeGreen")
            self.snake.append(new_segment)

    # moves the snake
    def move_snake(self):
        # moves the snake segments starting with the last one, to the position of the one before it
        for segment in range(len(self.snake) - 1, 0, -1):
            self.snake[segment].goto(self.snake[segment - 1].xcor(), self.snake[segment - 1].ycor())
        self.head.forward(MOVE_DISTANCE)

    # directional methods for turning, cannot turn back on itself
    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)

    # adds a segment to the snake
    def add_snake_segment(self):
        new_segment = Turtle("square")
        new_segment.penup()
        new_segment.color("LimeGreen")
        self.snake.append(new_segment)

    def collide_with_wall(self):
        if self.head.xcor() <= -290 or self.head.xcor() >= 290:
            return True
        if self.head.ycor() <= -290 or self.head.ycor() >= 290:
            return True

    def collide_with_tail(self):
        for segment in self.snake[1:]:
            if self.head.distance(segment) < 10:
                return True

    def reset_snake(self):
        for segment in self.snake:
            segment.hideturtle()
        self.snake.clear()
        self.create_snake()
        self.head = self.snake[0]
