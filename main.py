import turtle
from datetime import datetime

# Create a Turtle screen
screen = turtle.Screen()
screen.bgcolor("black")  # Set background color

# Create a Turtle for drawing the clock
clock = turtle.Turtle()
clock.speed(0)  # Set the drawing speed to the maximum

# Function to draw the clock face
def draw_clock_face(radius):
    clock.penup()
    clock.goto(0, -radius)
    clock.pendown()
    clock.color("white")
    clock.begin_fill()
    clock.circle(radius)
    clock.end_fill()

# Function to draw clock hands (hour, minute, and second)
def draw_clock_hands(length, angle, width, color):
    clock.penup()
    clock.goto(0, 0)
    clock.setheading(90 - angle)
    clock.pendown()
    clock.color(color)
    clock.pensize(width)
    clock.forward(length)
    clock.penup()
    clock.goto(0, 0)
    clock.pendown()

# Function to update the clock hands
def update_clock_hands():
    now = datetime.now()
    second = now.second
    minute = now.minute
    hour = now.hour % 12  # Convert to 12-hour format

    # Draw the second hand
    draw_clock_hands(150, second * 6, 2, "red")

    # Draw the minute hand
    draw_clock_hands(120, minute * 6 + second * 0.1, 4, "white")

    # Draw the hour hand
    draw_clock_hands(90, hour * 30 + minute * 0.5, 6, "white")

# Draw the clock face
draw_clock_face(200)

# Update the clock hands
update_clock_hands()

# Close the Turtle graphics window when clicked
screen.exitonclick()
