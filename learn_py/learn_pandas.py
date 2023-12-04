import pandas as pd

# Criando uma série com valores inteiros
series_objeto = pd.Series([1, 3, 5, 7, 8, 9, 11, 12, 30, 32, 35])

# Exibindo a série na tela usando print
print(series_objeto)

# Criando uma série com valores inteiros e índices personalizados
series_objeto2 = pd.Series([4, 7, 8, -2], index=['alfa', 'beta', 'teta', 'gama'])

# Imprimindo as séries na tela usando print e inserindo linhas em branco para melhorar a legibilidade
print(series_objeto2)
