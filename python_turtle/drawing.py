import turtle



def draw_art():
    window = turtle.Screen() # window properties
    window.bgcolor("red")

    ggobugi = turtle.Turtle() # ggobugi properties
    ggobugi.shape("turtle")
    ggobugi.color("yellow")
    ggobugi.speed('slowest')

    #ggobugi = turtle.Turtle().shape("turtle") # ggobugi properties

    onibugi = turtle.Turtle() # onibugi properties
    onibugi.shape("turtle")
    onibugi.color("blue")
    onibugi.speed('normal')

    draw_square(ggobugi, 100)
    draw_circle(onibugi, 100)

    window.exitonclick() # click exits the program

def draw_square(pokemon, pixel):
    for _ in range(4): # temp variable not used can be replaced with _
        pokemon.forward(pixel)
        pokemon.right(90)

def draw_circle(pokemon, radius):
    pokemon.circle(radius)



draw_art()