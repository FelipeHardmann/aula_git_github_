# lista = []
# tupla = ()

# conjunto = set()

# idade = '20'

# idade = int(idade)

# lista = ['Felipe', 'Tiago', 'Camila', 'André', 'Luis', 'Carlos', 'Thalita', 'Felipe', 'Felipe', 'Thalita']

# lista = set(lista)

# lista = list(lista)

# print(lista[0])

# conjunto = {'Felipe', 1.90, True, 20, 'Felipe', 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2}

# conjunto2 = {'Felipe', 'Tiago', 'André', 'Thalita'}

# conjunto3 = conjunto.intersection(conjunto2)

# conjunto4 = conjunto.union(conjunto2)

# print(conjunto4)

# conjunto = {'Felipe', 1.90, True, 20, 'Felipe', 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2}

# conjunto2 = {'Felipe', 'Tiago', 'André', 'Thalita'}

# conjunto.update(conjunto2)

# print(conjunto)

# for i in conjunto:
#     print(type(i))

# for i in conjunto:
#     print(i)

# conjunto.remove('Felipe')

# print(conjunto)

# print(conjunto | conjunto2)

# Atividade 1
# conjunto = set()

# conjunto.add('Maça')
# conjunto.add('Banana')
# conjunto.add('Uva')
# conjunto.add('Laranja')
# conjunto.add('Morango')

# for i in range(5):
#     fruta = input('Digite uma fruta: ')
#     conjunto.add(fruta)

# print(conjunto)

# Atividade 2

# print('Banana' in conjunto)

# lista = ['Felipe', 'Fernanda', 'Tiago']
# lista2 = ['Felipe', 'Chico', 'João']

# lista = set(lista)
# lista2 = set(lista2)

# valor_final = lista | lista2

# valor_final = list(valor_final)

# print(valor_final)

# Exemplo do dia a dia

# lista_emails_acesso = ['felipe@email.com', 'chico@email.com', 'joao@email.com',
#                        'thalita@email.com', 'carlos@email.com']

# lista_clientes = ['thalita@email.com', 'carlos@email.com']

# lista_emails_acesso = set(lista_emails_acesso)
# lista_clientes = set(lista_clientes)

# lista_email_enviar = lista_emails_acesso - lista_clientes

# print(lista_email_enviar)

# hashmap

# social_name = input('Digite seu nome: ')
# username = input('Digite o nome do seu usuário: ')

usuarios = {
    'username': 'fehardmann',
    'social_name': 'felipe',
    'city': 'Salvador'
}

# dicionario = {

# }

# print(usuarios['bairro'])
# print(usuarios.get('bairro', 'Não se aplica'))

# print(usuarios.items())

# for chave, valor in usuarios.items():
#     print(chave, valor)

# bairro = {'bairro': 'Stella Mares'}

# usuarios.update(bairro)

# lista_dados = list(usuarios.values())

# print(lista_dados)

# print(usuarios.values())

# for i in usuarios.values():
#     print(i)

# print(usuarios)


dicinario = {}

nome = input('Digite seu nome: ')
idade = int(input('Digite sua idade: '))

dicinario['nome'] = nome
dicinario['idade'] = idade

for chave, valor in dicinario.items():
    print(f'{chave}: {valor}')
