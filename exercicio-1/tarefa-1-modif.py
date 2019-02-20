contador = 0
soma = 0
maior = 0
menor = 0
while contador < 10:
    valor = int(input("entre com o valor"))
    soma = soma + valor
    contador = contador + 1
    if valor > maior:
            maior = valor
    elif valor < menor:
            menor = valor
media = soma / 10
print(media, "é a media dos valores")
print(soma, "é a soma dos valores")
print(maior, "é o maior valor")
print(menor, "é o menor valor")