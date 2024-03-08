from faker import Faker
import matplotlib.pyplot as plt
import numpy as np

fake = Faker('pt-BR')

# Gerando 20 nomes brasileiros aleatórios e número aleatório para cada nome
names = []
for i in range(20):
    names.append([fake.name(), str(fake.random_int(1,10))])

print(names, '\n')

# --------------------------------------------------------------------


# Criando ou abrindo arquivo.txt e escrevendo os 20 nomes e o número aleatório no arquivo.txt
with open('arquivo.txt', 'w') as arquivo:
    [arquivo.write(','.join(j) + '\n') for j in names]

# Recuperando os dados no arquivo.txt
nomes_arquivo = []
with open('arquivo.txt', 'r') as arquivo:
    [nomes_arquivo.append((linha.strip().split(','))) for linha in arquivo]
    print(nomes_arquivo)

pontuacao = []
for nome in nomes_arquivo:
    pontuacao.append(int(nome[1]))

print(pontuacao)

# total = 10

plt.hist(pontuacao, 10, density=True, facecolor='green', alpha=0.75)

plt.xlabel('Valores')
plt.ylabel('Probabilidade')
plt.title('Histograma dos valores')
plt.grid(True)
plt.show()