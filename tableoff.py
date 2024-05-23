'''import matplotlib.pyplot as plt
import numpy as np

x = [1, 2, 3]
y = [3.3, 0, 2.6]
y1 = [2.3] * len(x)
x2 = np.linspace(0, 1, 10)

fig, ax = plt.subplots()
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_title('Scatterplot')

ax.set_xticks([])
#ax.set_yticks([])

ax.scatter(x, y, color='green')
ax.plot(x, y1, label="Dados", color='purple', linestyle='-')

plt.show()'''

import matplotlib.pyplot as plt
import numpy as np

# Aplicar o estilo dark_background
plt.style.use('dark_background')
plt.get_cmap('plasma')

# Dados
x = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32]
y = [3.3, 0.1, 2.6, 3.5, 6.3, 1, 8.5, 2.5, 0.1, 2, 0.1, 0.1, 0.1, 0.1, 6, 0.5, 2, 1.5, 2, 1, 3, 9.5, 0.1, 1, 0.1, 0.1, 0.1, 3, 0.1, 0.1, 7, 6.5]
y1 = [2.3] * len(x)
y3 = [7] * len(x)
x2 = np.linspace(0, 1, 10)

# Criar a figura e os eixos
fig, ax = plt.subplots()

# Definir os labels e o título
ax.set_xlabel('ALUNOS')
ax.set_ylabel('NOTAS')
ax.set_title('NOTAS CÀLCULO')

# Definir os limites do eixo y
ax.set_ylim(0, 10)

# Definindo o intervalo entre os valores de y
ax.set_yticks(np.arange(0, 11, 1))

# Remover os valores do eixo x
ax.set_xticks([])

cores = ['magenta', 'lime'] * 16

# Adicionar o scatter plot e a linha horizontal
ax.scatter(x, y, color=cores)
ax.plot(x, y1, label="MÉDIA DA TURMA", linewidth=1.5, color='red', linestyle='-')
ax.plot(x, y3, label="MÉDIA PADRÃO", linewidth=1.5, color='gray', linestyle='-')

# Adicionar a legenda
ax.legend()

# Mostrar o gráfico
plt.show()