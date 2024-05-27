import matplotlib.pyplot as plt
import numpy as np

#Aplicar o estilo dark_background
plt.style.use('dark_background')

#Dados
y = [5.6, 5, 7.4, 6.3, 7.5, 7.1, 5.3, 6, 4.4, 1.1, 0.4, 7.5, 5.6, 6.7, 2.8, 0.1, 5.2, 5.2, 5.5, 5.3, 5.6, 5.4, 4.9, 5.8, 4.6, 7.2, 0.1, 7.8, 8.7, 4.3, 6.3, 4.3, 6, 5.2, 3.5, 1, 7.6, 0.1, 5.3, 6.9, 5, 7.9, 5.4, 8.7]
x = np.arange(len(y))
y3 = [7] * len(x)

#Calcular a média da turma
media = np.mean(y)

#Criar um array de médias com o mesmo comprimento de x
y_media = [media] * len(x)

#Criar a figura e os eixos
fig, ax = plt.subplots()

#Definir os labels e o título
ax.set_xlabel('ALUNOS')
ax.set_ylabel('NOTAS')
ax.set_title('NOTAS GRAFOS')

#Definir os limites do eixo y
ax.set_ylim(0, 10)

#Definindo o intervalo entre os valores de y
ax.set_yticks(np.arange(0, 11, 1))

#Remover os valores do eixo x
ax.set_xticks([])

cores = ['blue', 'white'] * 22

#Adicionar o scatter plot e a linha horizontal
ax.scatter(x, y, color=cores)
ax.plot(x, y_media, label="MÉDIA DA TURMA", linewidth=1.5, color='red', linestyle='-')
ax.plot(x, y3, label="MÉDIA PADRÃO", linewidth=1.5, color='gray', linestyle='-')

#Adicionar a legenda
ax.legend()

#Mostrar o gráfico
plt.show()
