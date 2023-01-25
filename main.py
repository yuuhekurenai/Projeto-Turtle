import random
from turtle import Turtle, Screen

tela = Screen()
cores = ["purple", "yellow", "red", "blue", "pink", "orange"]
titulo_tela = tela.textinput(title="Correndo Devagar", prompt="Qual é a sua aposta?")
posicao_y = [-70, -40, -10, 20, 50, 80]
tartatugas = []

corrida_valendo = True

for turtle_index in range(0, 6):
    nova_tartaruga = Turtle(shape="turtle")
    tela.setup(width=500, height=400)
    nova_tartaruga.penup()
    nova_tartaruga.color(cores[turtle_index])
    nova_tartaruga.goto(x=-230, y=posicao_y[turtle_index])
    tartatugas.append(nova_tartaruga)

if titulo_tela:
    corrida = True

while corrida:
    for turtle in tartatugas:
        if turtle.xcor() > 230:
            corrida = False
            tartaruga_vencedora = turtle.pencolor()
            if tartaruga_vencedora == titulo_tela:
                print(f"A tartaruga {tartaruga_vencedora} venceu!")
            else:
                print(f"A tartaruga {tartaruga_vencedora} venceu! , Você perdeu!")

            distancia = random.randint(0, 10)
            turtle.forward(distancia)

tela.exitonclick()
