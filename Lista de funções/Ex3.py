""" 3. Faça uma função que recebe a idade de uma pessoa em anos, meses e dias e retorna essa idade
expressa em dias. Considere um ano = 365 dias e um mês = 30 dias."""

def idade():
    ano = int(input('Digite sua idade (em anos): '))
    mes = int(input('Digite quantos meses passaram do seu aniversário: '))
    dia = int(input('Digite quantos dias quebrados tem desde a data do seu aniversário desse mes: '))
    print((ano *365) + (mes * 30) + dia,'dias')
idade()