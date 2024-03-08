from faker import Faker
import matplotlib.pyplot as plt
from num2words import num2words
from wordcloud import WordCloud


fake = Faker('pt-BR')

# Gerando nomes brasileiros aleatórios e pontuação aleatória para cada nome de pessoa
nomes_e_pontuacao = []
quantidade_de_alunos = 20
for i in range(quantidade_de_alunos):
    nomes_e_pontuacao.append([fake.name(), str(fake.random_int(1,10))])
    print(f'Nome: {nomes_e_pontuacao[i][0]} / Pontuação: {nomes_e_pontuacao[i][1]}')

# Criando ou abrindo arquivo.txt, escrevendo os 20 nomes e o número aleatório no arquivo.txt
try:
    with open('arquivo.txt', 'w') as arquivo:
        [arquivo.write(','.join(j) + '\n') for j in nomes_e_pontuacao]
except OSError:
    print('Ocorreu um erro')
finally:
    print('O arquivo.txt foi criado ou modificado com sucesso!\n')

# Recuperando os dados no arquivo.txt
try:
    dados_arquivo = []
    with open('arquivo.txt', 'r') as arquivo:
        [dados_arquivo.append((linha.strip().split(','))) for linha in arquivo] # armazena cada linha em uma lista bidimensional
except FileNotFoundError as erro:
    print('O arquivo não foi encontrado, execute o bloco de código acima novamente para criar o arquivo')
except OSError:
    print('Ocorreu um erro')
finally:
    print('Dados recuperados com sucesso!\n')

# Separando a pontuação em uma única lista
pontuacao = []
for nome in dados_arquivo:
    pontuacao.append(int(nome[1]))

# Contando quantas vezes cada pontuação aparece
for numero in set(pontuacao):
    mensagem = "pessoa" if pontuacao.count(numero) == 1 else "pessoas"
    verbo = 'tirou' if pontuacao.count(numero) == 1 else "tiraram"
    print(f'{pontuacao.count(numero)} {mensagem} {verbo} a pontuação {numero}')

# Gerando gráfico de histograma
total_colunas = 10
plt.figure(figsize=(8,5))
plt.hist(pontuacao, total_colunas, density=True, facecolor='blue', alpha=0.75)
plt.xlabel('Pontuações')
plt.ylabel('Probabilidade')
plt.title('Histograma das Pontuações')
plt.grid(True)
plt.show()

#Transformando os números em palavras
pontuacao_strings = list(map(lambda x: num2words(x, lang='pt_BR'),pontuacao))

# Gerando nuvem de palavras
nuvem_palavras = WordCloud(background_color='black', width=800, height=400).generate(','.join(pontuacao_strings))
plt.figure(figsize=(8,5))
plt.imshow(nuvem_palavras, interpolation='bilinear')
plt.axis("off")
nuvem_palavras.to_file("Nuvem de palavras.png")