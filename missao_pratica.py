from faker import Faker


fake = Faker('pt-BR')
names = []

# Gerando 20 nomes brasileiros aleatórios e número aleatório para cada nome
for i in range(20):
    names.append([fake.name(), str(fake.random_int(1,10))])

print(names, '\n')

# Criando ou abrindo arquivo.txt e escrevendo os 20 nomes e o número aleatório no arquivo.txt
with open('arquivo.txt', 'w') as arquivo:
    [arquivo.write(','.join(j) + '\n') for j in names]

# Recuperando os dados no arquivo.txt
names_graph = []
with open('arquivo.txt', 'r') as arquivo:
    [names_graph.append((linha.strip().split(','))) for linha in arquivo]
    
    for elemento in names_graph:
        elemento[1] = int(elemento[1])

print(names_graph)