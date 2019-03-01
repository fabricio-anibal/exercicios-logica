################################################################################

# author: Fabricio Anibal Pinheiro Alves
# GitHub: https://github.com/fabricio-anibal

################################################################################

# Desenvolva um algoritmo que solicite um número inteiro positivo N ao usuário e imprima a soma dos N primeiros números pares maiores do que zero.

################################################################################

n = 0
soma = 0
while n <= 0:
    n = int(input("Entre com o valor inteiro positivo"))
for i in range (2, (n*2)+1 , 2):
    soma = i + soma
print(soma)