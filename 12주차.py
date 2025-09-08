##ex.1
##from turtle import *
##
##t1= Turtle() 
##t1.shape("circle")
##
##t2= Turtle() 
##t2.shape("turtle")
##
##t3= Turtle() 
##t3.shape("square")
##
##t1.penup()
##t2.penup()
##t1.goto(0, 100)
##t2.goto(0,50)
##t1.pendown()
##t2.pendown()
##
##while True:
##    t1.circle(100)
##    t2.circle(150)
##    t3.circle(200)


##ex.2
##from turtle import*
##class Ball:
##    def __init__(self,c,s,speed):
##
##        self.x=0
##        self.y=0
##
##        self.xspeed=speed
##        self.yspeed=speed
##
##        self.size=s
##
##        self.color=c
##
##        self.t=Turtle()
##        self.t.shape("circle")
##        self.t.color(c,c)
##        self.t.resizemode("user")
##        self.t.shapesize(s,s,10)
##        
##    def move(self):
##        self.x += self.xspeed
##        self.y += self.yspeed
##        self.t.goto(self.x,self.y)
##
##ball=Ball("red",2,4)
##for i in range(100):
##    ball.move()



##ex.3
class Circle:
    def __init__(self,radius):
        self.radius=radius

    def calcPerimeter(self):
        self.radius*2*3.14
    def calcArea(self):
        self.radius**2*3.14
circle=Circle(4)
print("반지름:",circle.radius,"둘레:",circle.calcPerimeter,
      "면적:",circle.calcArea)
