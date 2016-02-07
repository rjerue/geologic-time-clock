# @author Ryan Jerue
# @email rjerue@umass.edu
# @Since 02/06/2016
# @See http://github.com/rjerue
# @See http://jerue.org/
# Credit to DJ Oamen for walkthrough on creation of the clock

#This is an analog clock that has the ability to flash images at certain points
#It was originally made for a geology professor so that he could have certain 
#geological events appear on the screen at certain times.

from turtle import *
from datetime import *

def main():
    ti = datetime.now()
    
###############################
    #CONFIG OPTIONS
###############################

#GLOBAL VARIABLES
    global t, tickspeed, stop, slowtick, newtick, changetick, image1, image1name, image2, image2name, image3, image3name, image4, image4name,image5, image5name
#STOP
    #Will stop the clock at one minute, switch to false to let it keep going
    stop = True
#TICKSPEED
    tickspeed  = 500000 #This number determines the speed of the clock. IT MUST BE UNDER 1000000 (One Million)
    changetick = 40 #Put a number under 60 here where you want to change how fast the tick goes.
    newtick    = 50000 #What you want the new tickspeed to be
#IMAGES
    #Create an image variable and set an image name. Then, add it to the images() function (right below main)
    #All Images must be of gif format (library mandated). I've been useing the below converter.
    #http://image.online-convert.com/convert-to-gif
    image1 = Turtle()
    image1name = "meteor.gif"
    image2 = Turtle()
    image2name = "bacteria.gif"
    image3 = Turtle()
    image3name = "protozoa.gif"
    image4 = Turtle()
    image4name = "mesozoic.gif"
    image5 = Turtle()
    image5name = "human.gif"
###############################
    
    t = ti.replace(hour=0, minute=0, second=0, microsecond=0) #sets the time to midnight.
    tracer(False)
    settings()
    tracer(True)
    tick()
    return "DONE"

###############################
    #IMAGES
###############################
def images():
    if(t.hour <= 1):
        #Image 1
        if(t.second > 2 and t.second < 10): #Between 2 and 10 seconds
            addshape(image1name)
            image1.shape(image1name)
            image1.resizemode("user")
            image1.shapesize(1, 1, 1)
            image1.showturtle()
        else:
            image1.hideturtle()
        #Image 2
        if(t.second > 14 and t.second < 30):
            addshape(image2name)
            image2.shape(image2name)
            image2.resizemode("user")
            image2.shapesize(1, 1, 1)
            image2.showturtle()
        else:
            image2.hideturtle()
        #Image 3
        if(t.second > 37 and t.second < 46):
            addshape(image3name)
            image3.shape(image3name)
            image3.resizemode("user")
            image3.shapesize(1, 1, 1)
            image3.showturtle()
        else:
            image3.hideturtle()
        #Image 4
        if(t.second > 48 and t.second < 52):
            addshape(image4name)
            image4.shape(image4name)
            image4.resizemode("user")
            image4.shapesize(1, 1, 1)
            image4.showturtle()
        else:
            image4.hideturtle()
        #Image 5
        if(t.second > 58 and t.second < 60):
            addshape(image5name)
            image5.shape(image5name)
            image5.resizemode("user")
            image5.shapesize(1, 1, 1)
            image5.showturtle()
        else:
            image5.hideturtle()

def moving(distance, angle=0):
    penup()
    right(angle)
    forward(distance)
    pendown()

def layout(length, vast):
    fd(length * 1.15)
    rt(90)
    fd(vast/2.0)
    lt(120)
    fd(vast)
    lt(120)
    fd(vast)
    lt(120)
    fd(vast/2.0)

def timer_hands(name, length, vast):
        reset()
        moving(-length*0.15)
        begin_poly()
        layout(length, vast)
        end_poly
        clock_labellings = get_poly()
        register_shape(name, clock_labellings)

def clockface(radius) :
    reset()
    pensize(3)
    for i in range(60):
        moving(radius)
        if i % 5 == 0:
            fd(25)
            moving(-radius-25)
        else:
            dot(3)
            moving(-radius)
        rt(6)
        
def settings():
    global  second_hand, minute_hand, hour_hand
    timer_hands("second_hand", 125, 25)
    timer_hands("minute_hand", 130, 25)
    timer_hands("hour_hand", 0, 0)#90, 25) #Support for a third hand. It actually calculates, it is just invisible
    clockface(400)
    second_hand = Turtle()
    second_hand.shape("second_hand")
    second_hand.color("gray40", "black")
    minute_hand = Turtle()
    minute_hand.shape("minute_hand")
    minute_hand.color("red", "orange")
    hour_hand = Turtle()
    hour_hand.shape("hour_hand")
    hour_hand.color("red", "orange")
    for hand in second_hand, minute_hand,  hour_hand:
        hand.resizemode("user")
        hand.shapesize(1, 3, 4)
        hand.speed(0)
    ht()

def tick():
    global t, tickspeed
    microseconds = t.microsecond + tickspeed
    secondTimer = t.second + microseconds/1000000.0
    minutes = t.minute + secondTimer/60.0
    onTheHour = t.hour + minutes/60.0
    if(changetick != 0):
        if(secondTimer > changetick):
            tickspeed = newtick
    if(microseconds >= 1000000):
        microseconds = 0;
    if(secondTimer >= 60.0):
        secondTimer = 0
        if(stop == True):
            time.sleep(500)
    if(minutes >=60):
        minutes = 0
    if(onTheHour >=24):
        onTheHour = 0
    t = t.replace(hour=int(onTheHour), minute=int(minutes), second=int(secondTimer), microsecond=int(microseconds))
    images()
    try:
        tracer(False)
        second_hand.setheading(6*secondTimer)
        minute_hand.setheading(6*minutes)
        hour_hand.setheading(30*onTheHour)
        tracer(True)
        ontimer(tick, 100)
    except Terminator:
        pass

#Don't touch this, its required for Turtle to work properly...
if __name__ == "__main__":
    mode("logo")
    msg = main()
    print(msg)
    mainloop()
