import unittest
def ultimo_numero(x):
    return x % 10
def remove(x):
    return x // 10
def soma(x):
    suma = 0
    while x!=0:
        var = ultimo_numero(x)
        x = remove(x)
        suma= var + suma
def dobra_numero(x):
    i=1
    while x != 0:
        digito = ultimo_numero(x)
        x = remove(x)
        pot = w = 0
        if i % 2 == 0:
            novo = digito * 2
            if novo > 9:
                y = ultimo_numero(x)
                z = remove(x)
                novo = y + z
            novo = novo * 10 ** (pot)
            if novo > 99:
                auxiliar = auxiliar * 10 ** (pot - 1)
            w = novo + auxiliar + w
        else:
            auxiliar = digito
        i = i + 1
        pot = pot + 1
    return w
def luhn(x):
    b = dobra_numero(x)
    n = soma(b)
    if n % 10 == 0:
        return True
    else:
        return False


