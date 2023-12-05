import pandas as pd

# Criando uma série com valores inteiros
series_objeto = pd.Series([1, 3, 5, 7, 8, 9, 11, 12, 30, 32, 35])

# Criando uma série com valores inteiros e índices personalizados
series_objeto2 = pd.Series([4, 7, 8, -2], index=['alfa', 'beta', 'teta', 'gama'])

# Exibindo a série na tela usando print
print(series_objeto)
print()
print(series_objeto2)

# Dicionário com informações sobre disciplinas
disciplinas = {
    'cursos': ['Estatistica', 'Economia', 'Calculo', 'Geometria'],  # Lista de nomes de cursos
    'créditos': [90, 60, 90, 40],  # Lista de créditos associados aos cursos
    'requisitos': [True, False, True, False]  # Lista de requisitos para cada curso (Verdadeiro ou Falso)
}
# Criando um DataFrame a partir do dicionário de disciplinas
data = pd.DataFrame(disciplinas)
# Exibindo o DataFrame na tela
print()
print(data)

# Criando uma série com nomes de cidades
nome_cidade = pd.Series(['São Paulo', 'Diadema', 'Campinas'])
# Criando uma série com dados de população para cada cidade
populacao = pd.Series([11.451245, 393.237, 1.138309])

# Criando um DataFrame combinando as séries de cidades e populações
# As séries são combinadas em um dicionário onde as chaves representam os nomes das colunas
dataframe_cidades = pd.DataFrame({"Cidade": nome_cidade, "População": populacao})

# Exibindo o DataFrame na tela
print()
print(dataframe_cidades)

# Lista de materiais e seus respectivos preços
materiais = ['Caderno', 'Caneta', 'Estojo']
precos = [12.99, 0.50, 4.99]

# Criação de um dicionário combinando os materiais com seus preços usando zip() e dict()
preco_materiais = dict(zip(materiais, precos))
# Verifica o tipo de dado de preco_materiais (será dict)
type(preco_materiais)

# Imprime o dicionário com os materiais e preços
print()
print(preco_materiais)

# Imprime o preço do material 'Caderno'
print()
print(preco_materiais['Caderno'])

# Verifica se 'Caneta' está presente como chave no dicionário e imprime o resultado (True ou False)
print('Caneta' in preco_materiais)

# Adiciona a chave 'Lapis' com o valor 0.25 ao dicionário
preco_materiais['Lapis'] = 0.25
# Imprime o dicionário atualizado após a adição da chave 'Lapis'
print()
print(preco_materiais)

# Remove a chave 'Estojo' do dicionário
del preco_materiais['Estojo']
# Imprime o dicionário após a remoção da chave 'Estojo'
print()
print(preco_materiais)

