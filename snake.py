import turtle as tur
from random import randrange
import copy

snake = [[0, 0]]
direct = [0, 10]
food = [-10, 0]

def make_square(x, y, size, color):
    tur.penup()
    tur.goto(x, y)
    tur.pendown()
    tur.begin_fill()
    tur.color(color)
    for i in range(4):
        tur.forward(size)
        tur.left(90)
    tur.end_fill()

def change_direction(x, y):
    direct[0] = x
    direct[1] = y


def in_range(head):
    return -250<head[0]<250 and -250 <head[1] <250

def move():
    #head = snake[-1][:]
    head = [snake[-1][0],snake[-1][1]]
    #head = copy.deepcopy(snake[-1])
    head = [head[0] + direct[0], head[1] + direct[1]]
    #print(head)
    if head in snake or not in_range(head):
        make_square(head[0],head[1],10,'red')
        tur.update()
        return
    if head == food:
        print("snake", len(snake))
        food[0] = randrange(-15, 15) * 10
        food[1] = randrange(-15, 15) * 10
    else:
        snake.pop(0)
    snake.append(head)
    tur.clear()
    make_square(food[0], food[1], 10, "orange")
    for body in snake:
        make_square(body[0], body[1], 10, "black")
    tur.update()
    tur.ontimer(move, 300)

tur.setup(500,500)
tur.hideturtle()
tur.listen()
tur.onkey(lambda: change_direction(0, 10), "Up")
tur.onkey(lambda: change_direction(0, -10), "Down")
tur.onkey(lambda: change_direction(-10, 0), "Left")
tur.onkey(lambda: change_direction(10, 0), "Right")
tur.tracer(False)
move()
tur.done()

