import turtle
t = turtle.Turtle()
t.fd(150)
t.bk(300)
t.fd(150)
t.penup()
t.rt(90)
t.fd(100)
t.lt(90)
t.pendown()
t.fd(150)
t.bk(300)
t.fd(200)
t.lt(90)
t.fd(200)
t.bk(300)
t.fd(100)
t.lt(90)
t.fd(100)
t.rt(90)
t.fd(200)
t.bk(300)
t.fd(100)
t.rt(90)

def x_top(t):
    t.penup()
    t.home()
    t.fd(50)
    t.lt(135)
    t.fd(25)
    t.pendown()
    t.fd(100)
    t.bk(50)
    t.lt(90)
    t.fd(50)
    t.bk(100)
    t.penup()
    t.home()

#x_top(t)

def x_right(t):
    t.penup()
    t.home()
    t.fd(50)
    t.lt(315)
    t.fd(25)
    t.pendown()
    t.fd(100)
    t.bk(50)
    t.lt(90)
    t.fd(50)
    t.bk(100)
    t.penup()
    t.home()
#x_right(t)
def x_top_left(t):
    t.penup()
    t.home()
    t.bk(50)
    t.lt(135)
    t.fd(25)
    t.pendown()
    t.fd(100)
    t.bk(50)
    t.lt(90)
    t.fd(50)
    t.bk(100)
    t.penup()
    t.home()

#x_top_left(t)

def x_top_right(t):
    t.penup()
    t.home()
    t.fd(150)
    t.lt(135)
    t.fd(25)
    t.pendown()
    t.fd(100)
    t.bk(50)
    t.lt(90)
    t.fd(50)
    t.bk(100)
    t.penup()
    t.home()
#x_top_right(t)
def x_left(t):
    t.penup()
    t.home()
    t.bk(50)
    t.rt(135)
    t.fd(25)
    t.pendown()
    t.fd(100)
    t.bk(50)
    t.lt(90)
    t.fd(50)
    t.bk(100)
    t.penup()
    t.home()
#x_left(t)
def x(t):
    t.penup()
    t.home()
    t.fd(50)
    t.rt(135)
    t.fd(25)
    t.pendown()
    t.fd(100)
    t.bk(50)
    t.lt(90)
    t.fd(50)
    t.bk(100)
    t.penup()
    t.home()
#x(t)

def x_bottom(t):
    t.penup()
    t.home()
    t.fd(50)
    t.rt(90)
    t.fd(100)
    t.lt(90)
    t.rt(135)
    t.fd(25)
    t.pendown()
    t.fd(100)
    t.bk(50)
    t.lt(90)
    t.fd(50)
    t.bk(100)
    t.penup()
    t.home()

#x_bottom(t)
def x_bottom_right(t):
    t.penup()
    t.home()
    t.fd(50)
    t.rt(90)
    t.fd(100)
    t.lt(90)
    t.fd(100)
    t.rt(135)
    t.fd(25)
    t.pendown()
    t.fd(100)
    t.bk(50)
    t.lt(90)
    t.fd(50)
    t.bk(100)
    t.penup()
    t.home()

#x_bottom_right(t)
def x_bottom_left(t):
    t.penup()
    t.home()
    t.fd(50)
    t.rt(90)
    t.fd(100)
    t.lt(90)
    t.bk(100)
    t.rt(135)
    t.fd(25)
    t.pendown()
    t.fd(100)
    t.bk(50)
    t.lt(90)
    t.fd(50)
    t.bk(100)
    t.penup()
    t.home()

#x_bottom_left(t)
def y_top(t):
    t.penup()
    t.home()
    t.fd(35)
    t.lt(90)
    t.fd(50)
    t.pendown()
    t.circle(40)
#y_top(t)
def y_top_right(t):
    t.penup()
    t.home()
    t.fd(135)
    t.lt(90)
    t.fd(50)
    t.pendown()
    t.circle(40)

#y_top_right(t)

def y(t):
    t.penup()
    t.home()
    t.bk(35)
    t.rt(90)
    t.fd(50)
    t.pendown()
    t.circle(40)

#y(t)

def y_bottom(t):
    t.penup()
    t.home()
    t.bk(35)
    t.rt(90)
    t.fd(150)
    t.pendown()
    t.circle(40)

#y_bottom(t)

def y_left(t):
    t.penup()
    t.home()
    t.bk(55)
    t.lt(90)
    t.bk(50)
    t.pendown()
    t.circle(40)

#y_left(t)

def y_top_left(t):
    t.penup()
    t.home()
    t.bk(55)
    t.lt(90)
    t.fd(50)
    t.pendown()
    t.circle(40)

#y_top_left(t)

def y_right(t):
    t.penup()
    t.home()
    t.fd(55)
    t.rt(90)
    t.fd(50)
    t.pendown()
    t.circle(40)
#y_right(t)

def y_bottom_right(t):
    t.penup()
    t.home()
    t.fd(55)
    t.rt(90)
    t.fd(150)
    t.pendown()
    t.circle(40)

#y_bottom_right(t)

def y_bottom_left(t):
    t.penup()
    t.home()
    t.bk(55)
    t.lt(90)
    t.bk(150)
    t.pendown()
    t.circle(40)
#y_bottom_left(t)


def tic_tac_toe(t):
    one = ''
    two = ''
    moves_one = []
    moves_two = []
    print('Welcome to multiplayer TIC TAC TOE')
    while one != 'winner' or two != 'winner':
        player_one = input('Player one, what is your move? (Either type top right, top left, top....'+'\n')
        moves_one.append(player_one)
        if player_one == 'top right':
            x_top_right(t)
        elif player_one == 'top left':
            x_top_left(t)
        elif player_one == 'top':
            x_top(t)
        elif player_one == 'center':
            x(t)
        elif player_one == 'right':
            x_right(t)
        elif player_one == 'left':
            x_left(t)
        elif player_one == 'bottom':
            x_bottom(t)
        elif player_one == 'bottom left':
            x_bottom_left(t)
        elif player_one == 'bottom right':
            x_bottom_right(t)
        if 'top left' in moves_one and 'left' in moves_one and 'bottom left' in moves_one:
            one = 'winner'
            t.penup()
            t.home()
            t.pendown()
            t.bk(100)
            t.lt(90)
            t.fd(100)
            t.bk(300)
            print('Congrats Player One, you won!!!')
            break
        if 'top' in moves_one and 'center' in moves_one and 'bottom' in moves_one:
            one = 'winner'
            t.penup()
            t.home()
            t.pendown()
            t.lt(90)
            t.fd(100)
            t.bk(300)
            print('Congrats Player One, you won!!!')
            break
        
        if 'top right' in moves_one and 'right' in moves_one and 'bottom right' in moves_one:
            one = 'winner'
            t.penup()
            t.home()
            t.pendown()
            t.fd(100)
            t.lt(90)
            t.fd(100)
            t.bk(300)
            print('Congrats Player One, you won!!!')
            break
        
        if 'top left' in moves_one and 'center' in moves_one and 'bottom right' in moves_one:
            one = 'winner'
            t.penup()
            t.home()
            t.pendown()
            t.lt(180)
            t.fd(50)
            t.rt(45)
            t.fd(70)
            t.bk(360)
            print('Congrats Player One, you won!!!')
            break
        
        if 'top right' in moves_one and 'center' in moves_one and 'bottom left' in moves_one:
            one = 'winner'
            t.penup()
            t.home()
            t.pendown()
            t.t.fd(50)
            t.lt(45)
            t.fd(70)
            t.bk(360)
            print('Congrats Player One, you won!!!')
            break
        
        if 'top left' in moves_one and 'top' in moves_one and 'top right' in moves_one:
            one = 'winner'
            t.penup()
            t.home()
            t.lt(90)
            t.fd(50)
            t.rt(90)
            t.pendown()
            t.fd(100)
            t.bk(300)
            print('Congrats Player One, you won!!!')
            break
        
        if 'left' in moves_one and 'center' in moves_one and 'right' in moves_one:
            one = 'winner'
            t.penup()
            t.home()
            t.penup()
            t.lt(90)
            t.bk(50)
            t.rt(90)
            t.pendown()
            t.fd(100)
            t.bk(300)
            print('Congrats Player One, you won!!!')
            break
        
        if 'bottom left' in moves_one and 'bottom' in moves_one and 'bottom right' in moves_one:
            one = 'winner'
            t.penup
            t.home()
            t.penup()
            t.lt(90)
            t.bk(150)
            t.rt(90)
            t.pendown()
            t.fd(100)
            t.bk(300)
            print('Congrats Player One, you won!!!')
            break
        if len(moves_one) > 4:
            print('DRAW')
            break

        player_two = input('Player two, what is your move? (Either type top right, top left, top....'+'\n')
        if player_two == 'top right':
            y_top_right(t)
        elif player_two == 'top left':
            y_top_left(t)
        elif player_two == 'top':
            y_top(t)
        elif player_two == 'center':
            y(t)
        elif player_two == 'right':
            y_right(t)
        elif player_two == 'left':
            y_left(t)
        elif player_two == 'bottom':
            y_bottom(t)
        elif player_two == 'bottom left':
            y_bottom_left(t)
        elif player_two == 'bottom right':
            y_bottom_right(t)
        moves_two.append(player_two)
        if 'top left' in moves_two and 'left' in moves_two and 'bottom left' in moves_two:
            two = 'winner'
            t.penup()
            t.home()
            t.pendown()
            t.bk(100)
            t.lt(90)
            t.fd(100)
            t.bk(300)
            print('Congrats Player Two, you won!!!')
            break
        if 'top' in moves_two and 'center' in moves_two and 'bottom' in moves_two:
            two = 'winner'
            t.penup()
            t.home()
            t.pendown()
            t.lt(90)
            t.fd(100)
            t.bk(300)
            print('Congrats Player Two, you won!!!')
            break
        if 'top right' in moves_two and 'right' in moves_two and 'bottom right' in moves_two:
            two = 'winner'
            t.penup()
            t.home()
            t.pendown()
            t.fd(100)
            t.lt(90)
            t.fd(100)
            t.bk(300)
            print('Congrats Player Two, you won!!!')
            break
        if 'top left' in moves_two and 'center' in moves_two and 'bottom right' in moves_two:
            two = 'winner'
            t.penup()
            t.home()
            t.pendown()
            t.lt(180)
            t.fd(50)
            t.rt(45)
            t.fd(70)
            t.bk(360)
            print('Congrats Player Two, you won!!!')
            break
        if 'top right' in moves_two and 'center' in moves_two and 'bottom left' in moves_two:
            two = 'winner'
            t.penup()
            t.home()
            t.pendown()
            t.t.fd(50)
            t.lt(45)
            t.fd(70)
            t.bk(360)
            print('Congrats Player Two, you won!!!')
            break
        if 'top left' in moves_two and 'top' in moves_two and 'top right' in moves_two:
            two = 'winner'
            t.penup()
            t.home()
            t.penup()
            t.lt(90)
            t.fd(50)
            t.rt(90)
            t.pendown()
            t.fd(100)
            t.bk(300)
            print('Congrats Player Two, you won!!!')
            break
        if 'left' in moves_two and 'center' in moves_two and 'right' in moves_two:
            two = 'winner'
            t.penup()
            t.home()
            t.penup()
            t.lt(90)
            t.bk(50)
            t.rt(90)
            t.pendown()
            t.fd(100)
            t.bk(300)
            print('Congrats Player Two, you won!!!')
            break
        if 'bottom left' in moves_two and 'bottom' in moves_two and 'bottom right' in moves_two:
            two = 'winner'
            t.penup()
            t.home()
            t.penup()
            t.lt(90)
            t.bk(150)
            t.rt(90)
            t.pendown()
            t.fd(100)
            t.bk(300)
            print('Congrats Player Two, you won!!!')
            break
        if len(moves_two) > 4:
            print('DRAW')
            break
        
        
    
    

tic_tac_toe(t)
