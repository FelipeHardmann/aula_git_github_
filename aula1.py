nome = 'Felipe' # str
idade = 20 # int
altura = 1.90 # float

# print(type(nome))
# print(type(idade))

# nome.
# idade.

nomes = ['Felipe', 'Tiago', 'José', 1.90, 20, True, ['Felipe', 'Tiago', 'José', 1.90, 20, True]]
# print(nomes)

# nomes.

# print(type(nomes))

# print(nomes[6][0])

# valores = ['Felipe', 'Tiago', 'José', 1.90, 20, True]

# for valor in valores:
#     if valor == 'Felipe':
#         print(valor)
#     else:
#         continue

# Atividade 1

# lista_numeros = [1, 2, 3, 4, 5]

# for i in lista_numeros:
#     print(i)

#  função append

# for i in range(10):
#     nome = input('Digite seu nome: ')
#     lista_nomes.append(nome)

# print(lista_nomes)

# # insert
# lista_nomes = []
# for i in range(3):
#     nome = input('Digite seu nome: ')
#     lista_nomes.insert(0, nome)

# print(lista_nomes)

# Remove
# valores = ['Felipe', 'Tiago', 'José', 1.90, 20, True, 'Felipe']

# valores.remove('felipe')

# print(valores)

# pop

# valores = ['Felipe', 'Tiago', 'José', 1.90, 20, True, 'Felipe']

# # valores.pop()

# valor_removido = input('Digite o valor que você quer remover: ')

# valores.remove(valor_removido)

# print(valores)

# lista_nomes = ['Felipe', 'Adriano', 'Tiago', 'Felipe', 'Tiago', 'Taina']

# lista_filtradas = []

# lista_filtradas = [i for i in lista_nomes if i not in ]

# for i in lista_nomes:
#     if i not in lista_filtradas:
#         lista_filtradas.append(i)

# print(lista_filtradas)

# lista_filtradas = [i for i in range(100) if i % 2 == 0]

# lista = []

# for i in range(100):
#     if i % 2 == 0:
#         lista.append(i)

# print(lista_filtradas)

# Tuplas
# lista.append('Teste')

# lista = ('Felipe', 'Adriano', 'Teste', 1, 2, 3, 4)

# lista = list(lista)

# Atividade tuplas

# tupla = (
#     ('Python', 'Infinity', 'Felipe'),
#     ('Java', 'USP', 'Prof.Teste'),
#     ('C', 'PUC', 'Murilo')
# )

# print(f'Palestrante: {tupla[2][2]}, Instituição: {tupla[2][1]}, Palestra: {tupla[2][0]}')

# Desafio prático

# times = [
#     ('Brasil', [9, 7.8, 10]),
#     ('Argentina', [1, 2, 0]),
#     ('Uruguai', [5, 7.8, 1])
# ]

# lista = []

# for time, valor in times:
#     media = sum(valor)/len(valor)
#     tupla = (time, media)
#     lista.append(tupla)

# for time, media in lista:
#     print(f'O time é {time} e a média: {media:.2f}')
