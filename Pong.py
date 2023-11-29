
import turtle

# set up game screen
game_window = turtle.Screen()
game_window.title("Doug-Pong")
game_window.bgcolor("#000")
game_window.setup(width=750, height=550, startx=None, starty=None)
game_window.tracer(0)


# Create the paddles, ball and score

# Left Paddle
lpaddle = turtle.Turtle()
lpaddle.shape('square')
lpaddle.color('#fff')
lpaddle.shapesize(5, 1)
lpaddle.penup()
lpaddle.speed(0)
lpaddle.goto(-360, 0)

# Right Paddle
rpaddle = turtle.Turtle()
rpaddle.shape('square')
rpaddle.color('#fff')
rpaddle.shapesize(5, 1)
rpaddle.penup()
rpaddle.speed(0)
rpaddle.goto(350, 0)

# Ball
ball = turtle.Turtle()
ball.shape('circle')
ball.color('#fff')
ball.penup()
ball.goto(0, 0)
ball.speed(0)
ball.dx, ball.dy = 1.5, -1.5

# Score and scoreboard
P1_score = 0
P2_score = 0

scoreboard = turtle.Turtle()
scoreboard.penup()
scoreboard.hideturtle()
scoreboard.color('#fff')
scoreboard.setpos(0, 250)
scoreboard.write('Player 1: 0 | Player 2: 0', align="center",
                 font=('Courier', 22, 'bold'))
scoreboard.speed(0)

# Create movement for paddles
# and keeping them from going off the screen

# Functions
y = 20


# Left movements
def lpaddle_moveup():
    lpaddle.sety(lpaddle.ycor() + y)
    if lpaddle.ycor() > 220:
        lpaddle.sety(220)


def lpaddle_movedown():
    lpaddle.sety(lpaddle.ycor() - y)
    if lpaddle.ycor() < -220:
        lpaddle.sety(-220)


# Right movements
def rpaddle_moveup():
    rpaddle.sety(rpaddle.ycor() + y)
    if rpaddle.ycor() > 220:
        rpaddle.sety(220)


def rpaddle_movedown():
    rpaddle.sety(rpaddle.ycor() - y)
    if rpaddle.ycor() < -220:
        rpaddle.sety(-220)


# Event listeners
game_window.listen()
game_window.onkeypress(lpaddle_moveup, 'w')
game_window.onkeypress(lpaddle_movedown, 's')
game_window.onkeypress(rpaddle_moveup, 'Up')
game_window.onkeypress(rpaddle_movedown, 'Down')


# restart game
def start_again():
    global player1_score, player2_score
    player1_score = 0
    player2_score = 0
    scoreboard.clear()
    ball.goto(0, 0)
    ball.dx *= -1
    rpaddle.goto(350, 0)
    lpaddle.goto(-360, 0)

    start_button = turtle.Turtle()
    start_button.penup()
    start_button.color("white")
    start_button.hideturtle()
    start_button.write("Game Over! Press Space to Start",
                       font=('Courier', 26), align="center")
    game_window.update()


# main game
while True:
    game_window.update()

    # Move the ball
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    # Bounce off walls
    if ball.ycor() > 265 or ball.ycor() < -265:
        ball.sety(ball.ycor())
        ball.dy *= -1

    # Reset and change score when outbounds
    if ball.xcor() > 365:
        ball.goto(0, 0)
        ball.dx *= -1
        P2_score += 1
        scoreboard.clear()
        scoreboard.write('Player 1: {} | Player 2: {}'.format(P1_score, P2_score), align="center",
                         font=('Courier', 22, 'bold'))
    elif ball.xcor() < -365:
        ball.goto(0, 0)
        ball.dx *= -1
        P1_score += 1
        scoreboard.clear()
        scoreboard.write('Player 1: {} | Player 2: {}'.format(P1_score, P2_score), align="center",
                         font=('Courier', 22, 'bold'))

    # Bounce off both paddles

    # Check for collision with right paddle
    if (ball.xcor() > 330 and ball.xcor() < 340) and \
        (ball.ycor() < rpaddle.ycor() + 60 and
         ball.ycor() > rpaddle.ycor() - 60):
        ball.setx(330)
        ball.dx *= -1

    # Check for collision with left paddle
    elif (ball.xcor() < -340 and ball.xcor() > -350) and \
        (ball.ycor() < lpaddle.ycor() + 60 and
         ball.ycor() > lpaddle.ycor() - 60):
        ball.setx(-340)
        ball.dx *= -1

    # Change speed
    if P1_score == 10 or P2_score == 10:
        ball.hideturtle()
        start_again()
