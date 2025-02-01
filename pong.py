import turtle
janela = turtle.Screen()
janela.title("Pong - Prova")
janela.bgcolor("black")
janela.setup(width=800, height=600)
janela.tracer(0)

pontos_a = 0
pontos_b = 0

parede_a = turtle.Turtle()
parede_a.speed(0)
parede_a.shape("square")
parede_a.color("white")
parede_a.shapesize(stretch_wid=5, stretch_len=1)
parede_a.penup()
parede_a.goto(-350, 0)

parede_b = turtle.Turtle()
parede_b.speed(0)
parede_b.shape("square")
parede_b.color("white")
parede_b.shapesize(stretch_wid=5, stretch_len=1)
parede_b.penup()
parede_b.goto(350, 0)

bola = turtle.Turtle()
bola.speed(0)
bola.shape("square")
bola.color("white")
bola.penup()
bola.goto(0, 0)
bola.mx = 0.2
bola.my = -0.2

placar = turtle.Turtle()
placar.speed(0)
placar.color("white")
placar.penup()
placar.hideturtle()
placar.goto(0, 260)
placar.write("Jogador A: 0  Jogador B: 0", align="center", font=("Courier", 15, "normal"))

def parede_a_up():
    y = parede_a.ycor()
    y += 20
    parede_a.sety(y)

def parede_a_down():
    y = parede_a.ycor()
    y -= 20
    parede_a.sety(y)

def parede_b_up():
    y = parede_b.ycor()
    y += 20
    parede_b.sety(y)

def parede_b_down():
    y = parede_b.ycor()
    y -= 20
    parede_b.sety(y)

janela.listen()
janela.onkeypress(parede_a_up, "Right")
janela.onkeypress(parede_a_down, "Left")
janela.onkeypress(parede_b_up, "Up")
janela.onkeypress(parede_b_down, "Down")

while True:
    janela.update()

    bola.setx(bola.xcor() + bola.mx)
    bola.sety(bola.ycor() + bola.my)

    if bola.ycor() > 290:
        bola.sety(290)
        bola.my *= -1

    if bola.ycor() < -290:
        bola.sety(-290)
        bola.my *= -1

    if bola.xcor() > 390:
        bola.goto(0, 0)
        bola.mx *= -1
        pontos_a += 1
        placar.clear()
        placar.write("Jogador A: {}  Jogador B: {}".format(pontos_a, pontos_b), align="center", font=("Courier", 15, "normal"))

    if bola.xcor() < -390:
        bola.goto(0, 0)
        bola.mx *= -1
        pontos_b += 1
        placar.clear()
        placar.write("Jogador A: {}  Jogador B: {}".format(pontos_a, pontos_b), align="center", font=("Courier", 15, "normal"))

    if (bola.xcor() > 340 and bola.xcor() < 350) and (bola.ycor() < parede_b.ycor() + 50 and bola.ycor() > parede_b.ycor() - 50):
        bola.setx(340)
        bola.mx *= -1

    if (bola.xcor() < -340 and bola.xcor() > -350) and (bola.ycor() < parede_a.ycor() + 50 and bola.ycor() > parede_a.ycor() - 50):
        bola.setx(-340)
        bola.mx *= -1
