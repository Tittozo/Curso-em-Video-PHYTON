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
