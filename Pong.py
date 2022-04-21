
import turtle as t
import os



player1 = 0
player2 = 0

win = t.Screen()    
win.title("Pong Game")
win.bgcolor('black')    
win.setup(width=800,height=600) 
win.tracer(0)  



paddle1 = t.Turtle()
paddle1.speed(0)
paddle1.shape('square')
paddle1.color('white')
paddle1.shapesize(stretch_wid=5,stretch_len=1)
paddle1.penup()
paddle1.goto(-350,0)



paddle2 = t.Turtle()
paddle2.speed(0)
paddle2.shape('square')
paddle2.shapesize(stretch_wid=5,stretch_len=1)
paddle2.color('blue')
paddle2.penup()
paddle2.goto(350,0)



ball = t.Turtle()
ball.speed(0)
ball.shape('circle')
ball.color('red')
ball.penup()
ball.goto(0,0)
ball_dx = 0.2   
ball_dy = 0.2



pen = t.Turtle()
pen.speed(0)
pen.color('skyblue')
pen.penup()
pen.hideturtle()
pen.goto(0,260)
pen.write("{}                 -                    {} ".format(player1,player2),align="center",font=('Monaco',24,"normal"))




def pad1_yukari():
    
    if paddle1.ycor()<=240:
        y = paddle1.ycor()
        y = y + 10
        paddle1.sety(y)



def pad1_asagi():
    if paddle1.ycor()>=-240:
        y = paddle1.ycor()
        y = y - 10
        paddle1.sety(y)



def pad2_yukari():
    if paddle2.ycor()<=240:
        y = paddle2.ycor()
        y = y + 10
        paddle2.sety(y)



def pad2_assagi():
    if paddle2.ycor()>=-240:
        y = paddle2.ycor()
        y = y - 10
        paddle2.sety(y)


win.listen()
win.onkeypress(pad1_yukari,"w")
win.onkeypress(pad1_asagi,"s")
win.onkeypress(pad2_yukari,"Up")
win.onkeypress(pad2_assagi,"Down")




def start_game(ball_dx,ball_dy,player1,player2):

    while True:
        win.update() 
       
        ball.setx(ball.xcor() + ball_dx)
        ball.sety(ball.ycor() + ball_dy)

        

        if ball.ycor() > 290:   
            ball.sety(290)
            ball_dy = ball_dy * -1
            
        
        if ball.ycor() < -290:  
            ball.sety(-290)
            ball_dy = ball_dy * -1
            

        if ball.xcor() > 390:   
            ball.goto(0,0)
            ball_dx = ball_dx * -1
            player1 = player1 + 1
            pen.clear()
            pen.write("{}                 -                    {} ".format(player1,player2),align="center",font=('Monaco',24,"normal"))
            os.system("afplay wallhit.wav&")



        if(ball.xcor()) < -390: 
            ball.goto(0,0)
            ball_dx = ball_dx * -1
            player2 = player2 + 1
            pen.clear()
            pen.write("{}                 -                    {} ".format(player1,player2),align="center",font=('Monaco',24,"normal"))
            os.system("afplay wallhit.wav&")


        

        if(ball.xcor() > 330) and (ball.xcor() < 350) and (ball.ycor() < paddle2.ycor() + 40 and ball.ycor() > paddle2.ycor() - 40):
        
            ball.setx(329)
            ball_dx = ball_dx * -1
            os.system("afplay paddle.wav&")

        if(ball.xcor() < -330) and (ball.xcor() > -350) and (ball.ycor() < paddle1.ycor() + 40 and ball.ycor() > paddle1.ycor() - 40):
            ball.setx(-329)
            ball_dx = ball_dx * -1
            os.system("afplay paddle.wav&")

start_game(ball_dx,ball_dy,player1,player2)
