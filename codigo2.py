#* «Copyright 2022 Roberto Reinosa»
#*
#* This program is free software: you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation, either version 3 of the License, or
#  (at your option) any later version.
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#  You should have received a copy of the GNU General Public License
#  along with this program.  If not, see <http://www.gnu.org/licenses/>.
#*

import matplotlib.pyplot as plt
import random

valor_A = int(input("Cantidad de A: \n"))
probabilidad_reaccion = int(input("Probabilidad de la Reacción 1: \n"))
probabilidad_reaccion2 = int(input("Probabilidad de la Reacción 2: \n"))

vector_principal = []
vector_secundario = []

for i in range(0, 100):

    vector_principal.append(0)

contador_2 = 0

while 1:

    valor_aleatorio = random.randint(0, 99)

    if vector_principal[valor_aleatorio] == 0:

        contador_2 += 1
        vector_principal[valor_aleatorio] = 1

    if contador_2 == valor_A:

        break

vector_iteracion1 = []
vector_iteracion2 = []
vector_iteracion3 = []

for i in range(0, 100):

    vector_iteracion1.append(0)
    vector_iteracion2.append(0)
    vector_iteracion3.append(0)

for iteraciones in range(0, 200):

    for i in range(0, 100):

        vector_principal[i] = 0

    contador_1 = 0

    while 1:

        valor_aleatorio = random.randint(0, 99)

        if vector_principal[valor_aleatorio] == 0:

            contador_1 += 1
            vector_principal[valor_aleatorio] = 1

        if contador_1 == valor_A:

            break

    for tiempo in range(0, 100):

        vector_secundario = vector_principal

        for i in range(0, 100):

            if(vector_principal[i] == 1) & (random.randint(0, 99) < probabilidad_reaccion):

                vector_secundario[i] = 2

            elif (vector_principal[i] == 2) & (random.randint(0, 99) < probabilidad_reaccion2):

                vector_secundario[i] = 3

        vector_principal = vector_secundario

        contador1 = 0
        contador2 = 0
        contador3 = 0

        for i in range(0, 100):

            if vector_principal[i] == 1:

                contador1 += 1

            elif vector_principal[i] == 2:

                contador2 += 1

            elif vector_principal[i] == 3:

                contador3 += 1

        vector_iteracion1[tiempo] += contador1
        vector_iteracion2[tiempo] += contador2
        vector_iteracion3[tiempo] += contador3

for i in range(0, 100):

    vector_iteracion1[i] /= 200
    vector_iteracion2[i] /= 200
    vector_iteracion3[i] /= 200

vector_iteracion1.insert(0, valor_A)
vector_iteracion2.insert(0, 0)
vector_iteracion3.insert(0, 0)

plt.xlabel("Iteraciones")
plt.ylabel("Cantidad")

plt.plot(vector_iteracion1)
plt.plot(vector_iteracion2)
plt.plot(vector_iteracion3)

plt.show()

