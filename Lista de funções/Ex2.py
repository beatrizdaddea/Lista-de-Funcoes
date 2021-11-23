""" 2. Faça um procedimento que recebe a idade de um nadador e retorna, a categoria desse nadador
de acordo com a tabela abaixo:
Idade/ Categoria
5 a 7 /anos Infantil A
8 a 10 /anos Infantil B
11-13 /anos Juvenil A
14-17 /anos Juvenil B
Maiores de 18 anos /Adult"""

def categoria():
    idade = int(input('Qual a sua idade? '))
    if (idade >=5 and idade <=7):
        print('Infantil A')
    elif (idade >=8 and idade <=10):
        print('Infantil B')
    elif (idade >= 11 and idade <=13):
        print('Juvenil A')
    elif (idade >=14 and idade <= 17):
        print('Juvenil B')
    elif(idade >= 18):
        print('Adulto')
categoria()