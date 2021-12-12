import re  # RegEx

endereco = 'Rua Jaguaré, 84, Jardim Laila, 06813170, Embu das Artes, SP'

# Ponto de interrogação depois do conjunto, indica que o conjunto pode aparecer ou não (?)
# Quantificadores, entre chaves indica o numero de repeticoes de um conjunto, pode ter limite ou não {0,2}
padrao = re.compile('[0-9]{5}[-]?[0-9]{3}')  # CEP Brasileiro
busca = padrao.search(endereco)  # Match
if busca:
    print(busca.group())
