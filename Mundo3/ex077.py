# Contagem de vogais em Tuplas
palavras = ['Aprender', 'Programar', 'em', 'Python', 'é', 'muito', 'legal',
            'é', 'também', 'divertido', 'e', 'desafiador', 'para', 'quem', 'gosta',
            'de', 'resolver', 'problemas', 'com', 'lógica', 'e', 'criatividade']

# Definindo as vogais (incluindo as acentuadas que aparecem na sua lista)
vogais = 'aeiouáéíóúAEIOUÁÉÍÓÚ'

# Mantive sua lógica de processamento por palavra
for palavra in palavras:
    # Criamos uma lista temporária para as vogais desta palavra específica
    vogais_da_palavra = []
    
    for letra in palavra:
        if letra in vogais:
            vogais_da_palavra.append(letra.lower())
    
    # Exibição conforme o seu modelo, mas automatizada para cada palavra
    if vogais_da_palavra:
        print(f'Na palavra {palavra:.<15} temos as vogais: {" ".join(vogais_da_palavra)}')

print('-'*40)
print('Fim da contagem de vogais.')

#OUTRA FORMA DE RESOLVER O EXERCÍCIO

# Lista de palavras
palavras = ('Aprender', 'Programar', 'em', 'Python', 'e', 'muito', 'legal',
            'e', 'tambem', 'divertido', 'e', 'desafiador', 'para', 'quem', 'gosta',
            'de', 'resolver', 'problemas', 'com', 'logica', 'e', 'criatividade')

# Loop para analisar cada palavra da tupla/lista
for p in palavras:
    print(f'\nNa palavra {p.upper()} temos as vogais: ', end='')
    
    # Loop para analisar cada letra da palavra atual
    for letra in p:
        if letra.lower() in 'aeiouáéíóúâêîôûãõ': # Verifica se a letra é uma vogal (incluindo acentos)
            print(letra.lower(), end=' ')

print('\n' + '-'*40)
print('Fim da listagem de vogais.')
