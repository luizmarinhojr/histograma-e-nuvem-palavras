from faker import Faker

fake = Faker('pt-BR')
names = []

for i in range(20):
    names.append([fake.name(), str(fake.random_int(1,10))])

print(names)

with open('arquivo.txt', 'w') as arquivo:
    for j in names:
        arquivo.write(','.join(j))
        arquivo.write('\n')

