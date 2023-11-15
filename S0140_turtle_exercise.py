"""
Opgave "Tom the Turtle":

Som altid skal du læse hele opgavebeskrivelsen omhyggeligt, før du begynder at løse opgaven.

Kopier denne fil til din egen løsningsmappe. Skriv din løsning ind i kopien.

Funktionen "demo" introducerer dig til alle de kommandoer, du skal bruge for at interagere med Tom i de følgende øvelser.

Kun hvis du er nysgerrig og elsker detaljer:
    Her er den fulde dokumentation for turtle graphics:
    https://docs.python.org/3.3/library/turtle.html

Del 1:
    Skriv en funktion "square", som accepterer en parameter "length".
    Hvis denne funktion kaldes, får skildpadden til at tegne en firkant med en sidelængde på "længde" pixels.

Del 2:
     Færdiggør funktionen "visible", som skal returnere en boolsk værdi,
     der angiver, om skildpadden befinder sig i det synlige område af skærmen.
     Brug denne funktion i de følgende dele af denne øvelse
     til at få skildpadden tilbage til skærmen, når den er vandret væk.

Del 3:
    Skriv en funktion "many_squares" med en for-loop, som kalder square gentagne gange.
    Brug denne funktion til at tegne flere firkanter af forskellig størrelse i forskellige positioner.
    Funktionen skal have nogle parametre. F.eks:
        antal: hvor mange firkanter skal der tegnes?
        størrelse: hvor store er firkanterne?
        afstand: hvor langt væk fra den sidste firkant er den næste firkant placeret?

Del 4:
    Skriv en funktion, der producerer mønstre, der ligner dette:
    https://pixabay.com/vectors/spiral-square-pattern-black-white-154465/

Del 5:
    Skriv en funktion, der producerer mønstre svarende til dette:
    https://www.101computing.net/2d-shapes-using-python-turtle/star-polygons/
    Funktionen skal have en parameter, som påvirker mønsterets form.

Del 6:
    Opret din egen funktion, der producerer et sejt mønster.
    Senere, hvis du har lyst, kan du præsentere dit mønster på storskærmen for de andre.

Når dit program er færdigt, skal du skubbe det til dit github-repository.
Send derefter denne Teams-meddelelse til din lærer: <filename> færdig
Fortsæt derefter med den næste fil.
"""

import turtle  # this imports a library called "turtle". A library is (someone else's) python code, that you can use in your own program.


# def visible(turtle_name):  # returns true if both the x- and y-value of the turtle's position are between -480 and 480
# you will need this: x-value: turtle_name.position()[0]
# and this:           y-value: turtle_name.position()[1]
# if turtle_name.position()[0] and turtle_name.position(480)[0] and turtle_name.position()[1] and turtle_name.position(480)[1]:
# return True

# Del 3: Visible funktion:
def visible(my_turtle):
    x, y = my_turtle.position()
    # x_inside_left = -my_turtle.window_width() / 2 < x
    # x_inside_right = x < my_turtle.window_width() / 2

    x_inside = (-my_turtle.window_width() / 2 < x < my_turtle.window_width() / 2)
    y_inside = (-my_turtle.window_height() / 2 < y < my_turtle.window_height() / 2)

    return x_inside and y_inside


def demo():  # demonstration of basic turtle commands
    tom = turtle.Turtle()  # create an object named tom of type Turtle
    print(type(tom))
    tom.speed(1)  # fastest: 10, slowest: 1
    for x in range(8):  # do the following for x = 0, 1, 2, 3, 4, 5, 6, 7
        tom.forward(50)  # move 50 pixels
        tom.left(45)  # turn 45 degrees left
        print(f'Tom is now at {tom.position()}, x-value: {tom.position()[0]=:.2f}, y-value: {tom.position()[1]=:.2f}')
    tom.penup()  # do not draw while moving from now on
    tom.forward(100)
    tom.pendown()  # draw while moving from now on
    tom.pencolor("red")  # draw in red
    tom.right(90)  # turn 90 degrees right
    tom.forward(120)
    tom.right(-90)  # turning -90 degrees right is the same as turning +90 degrees left
    tom.forward(120)
    tom.home()  # return to the original position in the middle of the window

    turtle.done()  # keeps the turtle window open after the program is done


# Del 1: Square funktion:
def square(my_turtle, length):
    for x in range(4):
        my_turtle.forward(length)
        my_turtle.right(90)


# Del 3: "Many squares" funktion:
def many_squares(my_turtle, amount, size, distance):
    for x in range(amount):
        square(my_turtle, size)
        my_turtle.penup()
        my_turtle.forward(distance)
        my_turtle.pendown()


# Del 4: lav spiral mønster
def spiral_pattern(my_turtle, sides, length_incre, length_start, angle):
    length = length_start
    for x in range(sides):
        my_turtle.left(angle)
        my_turtle.backward(length)
        length += length_incre


# Del 6:
def own_pattern(my_turtle, sides, length_start, angle):
    length = length_start
    for x in range(length):
        my_turtle.forward(length)
        my_turtle.left(angle)
        my_turtle.forward(length)
        my_turtle.left(angle)


def tegn_stjerne(my_turtle, points, size, angle):
    # Opret en Turtle-skærm
    skærm = turtle.Screen()

    # Tegn stjernen
    for _ in range(points):
        my_turtle.forward(size)
        my_turtle.right(angle)

    # Luk Turtle-vinduet ved at klikke på det
    skærm.exitonclick()


def tegn_sejt_mønster(my_turtle, points, size, angle):
    # Opret en Turtle-skærm
    # skærm = turtle.Screen()

    # Opret en Turtle
    # mønster_turtle = turtle.Turtle()

    # Tegn det seje mønster
    for _ in range(points):
        my_turtle.forward(size)
        my_turtle.right(angle)

    # Luk Turtle-vinduet ved at klikke på det
    # skærm.exitonclick()


tom = turtle.Turtle()  # create an object named tom of type Turtle

# square function test
square(tom, 50)
# many_squares(tom, 3, 50, 60)
# spiral_pattern(my_turtle=tom, sides=10, length_incre=10, length_start=10, angle=90)
# own_pattern(my_turtle=tom, sides=10, length_start=20, angle=90)
# Kald funktionen med ønsket størrelse
# tegn_stjerne(my_turtle=tom, points=5, size=50, angle=144)
# Kald funktionen for at tegne mønsteret
# tegn_sejt_mønster(my_turtle=tom, points=59, size=150, angle=118)
# Test visible function
print(visible(my_turtle=tom))
turtle.done()  # keeps the turtle window open after the program is done

#demo()
