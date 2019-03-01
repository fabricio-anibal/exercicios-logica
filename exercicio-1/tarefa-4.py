n = 0
soma = 0
while n <= 0:
    n = int(input("Entre com o valor inteiro positivo"))
for i in range (2, n+1 , 2):
    soma = i + soma
print(soma)