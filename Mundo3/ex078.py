#DESAFIO 078 DO CURSO EM VÍDEO PYTHON

lista = []

# Usamos um laço para não precisar repetir o input 5 vezes
for i in range(0, 5):
    lista.append(int(input(f'Digite um valor para a Posição {i}: ')))

print('=-=' * 20)

# Corrigido: Adicionado o 'f' antes das aspas para a lista aparecer
print(f'Você digitou os números {lista}')

# Exibição dos resultados com f-strings
print(f'O maior valor digitado foi {max(lista)} na posição {lista.index(max(lista))}')
print(f'O menor valor digitado foi {min(lista)} na posição {lista.index(min(lista))}')
