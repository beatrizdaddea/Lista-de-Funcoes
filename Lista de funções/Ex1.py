"""1. Faça uma função que recebe por parâmetro o raio de uma esfera e calcula o seu volume
v = 4/3 x PI x R³, com PI = 3,14 """

def volume():
    raio_esfera = float(input('Digite o valor do raio da esfera:'))
    print(((4/3)*3.14) *(raio_esfera**3))
volume()