#DESAFIO 79 DO CURSO EM VÍDEO
#Valores unicos em uma lista

valores = []
while True:
    n = int(input('Digite um valor: '))
    if n not in valores:
        valores.append(n)
        print('Valor adicionado com sucesso...')
    else:
        print('Valor duplicado! Não vou adicionar...')

    r = str(input('Quer continuar? [S/N]').strip().upper())
    if r == 'N':
        break
print('-='*30)
print(f'Você digitou os valores {valores}')



