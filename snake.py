from turtle import Turtle
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0
STARTING_POSITIONS = [(0,0), (-20,0), (-40,0)]
class Snake:

    def __init__(self):
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]

    def create_snake(self):
        for position in STARTING_POSITIONS:
            self.add_segment(position)


    def add_segment(self, position):
        tim = Turtle()
        tim.shape('square')
        tim.color('white')
        tim.penup()
        tim.goto(position)
        tim.shapesize(stretch_wid=0.95, stretch_len=0.95, outline=None)
        self.segments.append(tim)

    def extend(self):
        #add a new function to the snake
        self.add_segment(self.segments[-1].position())



    def move(self):
        for seg_num in range(len(self.segments) - 1, 0, -1):
            nex_x = self.segments[seg_num - 1].xcor()
            nex_y = self.segments[seg_num - 1].ycor()
            self.segments[seg_num].goto(nex_x, nex_y)
        self.head.forward(MOVE_DISTANCE)

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
