""" 4. O código de César é uma das mais simples e conhecidas técnicas de criptografia. É um tipo de
substituição na qual cada letra do texto e substituída por outra, que se apresenta no alfabeto abaixo
dela um número fixo de vezes. Por exemplo, com uma troca de três posições, ‘A’ seria substituído
por ‘D’, ‘B’ se tornaria ‘E’, e assim por diante. Implemente um programa que faça uso desse
Código de César, entre com uma string e retorne a string codificada. Exemplo:
String: a ligeira raposa marrom saltou sobre o cachorro cansado
Nova string: D OLJHLUD UDSRVD PDUURP VDOWRX VREUH R FDFKRUUR
FDQVDGR"""

alfabeto = 'abcdefghijklmnopqrstuvwxyz'
texto = str(input('Digite o texto: '))
criptografia = ''
mover_frente = 29

for letra in texto.lower():
    for i in range(len(alfabeto)):
        if letra == alfabeto[i]:
            if i + mover_frente < len(alfabeto):
                criptografia += alfabeto[i+ mover_frente]
            else:
                while i + mover_frente > len(alfabeto):
                    mover_frente -= 26
                    criptografia += alfabeto[i+ mover_frente]

print(criptografia)