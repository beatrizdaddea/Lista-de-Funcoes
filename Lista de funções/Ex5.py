""" 5. Escreva um programa para calcular a soma dos números que aparecem em uma determinada
string. Se não houver números, gere uma exceção dizendo que a string não contém números.
A string fornecida é: 15 é 25 uma 20 string
A soma dos números na string é: 60 """

import re
def result():
    frase = input('Digite uma frase: ')
    try:
        if (any(chr.isdigit() for chr in frase) == True):
            i = 0
            soma = 0
            n = [float(temp) for temp in re.findall(r'-?\d+\.?\d*', frase)]
            qtdn = len(n)
            while i < qtdn:
                soma = soma + n[i]
                i= i + 1
            print(soma)
        else:
            next()
    except:
        print('A String nao contem numeros!!!')
result()