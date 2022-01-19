#  https://faker.readthedocs.io/en/master/#
from faker import Faker
fake = Faker(['pt_BR'])
fake.name()
fake.address()
fake.cpf()
fake.country()
for c in range(3):
    print(f'Nome: {fake.name()}')
    print(f'Endereço: {fake.address()}')
    print(f'CPF: {fake.cpf()}')
    print(f'País: {fake.country()}')
    print('='*50)

