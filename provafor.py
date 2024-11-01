inicio = int(input('Digite o primeiro número do intervalo: '))

fim = int(input('Digite o último número do intervalo: '))

soma = 0

for numero_pares in range (inicio, fim + 1):
    if numero_pares % 2 == 0:
        soma += numero_pares
if soma > 0:
    print (f'A soma dos números pares nos intervalos de {inicio} a {fim} é: {soma}')
else:
    print (f'Não há números pares no intervalo entre {inicio} a {fim}.')









