# diga si cada una de las desigualdades es verdadera o falsa
# A) -3 < -15 
import numpy as np 
resultado= np.array(-3) < np.array(-15)
print(resultado )
# por que en la recta numerica el -3 esta mas serca del 0 y portanto es mayor que -15

# B) 2**0.5 > 1.41
import numpy as np 
resultado= 2**0.5 > 1.41 
print(resultado)
# es verdadero por que al momento de hacer la operacion de raiz de dos, da como resultado 1.41... y al tener mas desimales es mayor que 1.41
# C) 11/12 < 13/14
import numpy as np 
resultado= 11/12 < 13/14
print( resultado)
# por que al momento de hacer los calculos de 11/12 y 13/14  los resultados fueron 0,91 y 0,92, por tanto, como 0, tiene una sentecima menos que 0,92 es correcto decir que  11/12 < 13/14 
# D) e < 3
import numpy as np 
import math
resultado= math.e < 3
print(resultado)
#esto es verdadero ya que "e" es una costante matematica que es aproximadamente a 2,71828 lo cual es menor que 3
# E) -1/2 <= 0.4 
import numpy as np
resultado= -1/2 <= 0.4 
print(resultado)
# esto es verdadero ya que -1/2 es negativo y 0,4 es positivo por lo tanto es verdadero
# F) π >= 4
import numpy as np 
import math
math.pi
resultado= math.pi >= 4 
print( resultado)
#esto es falso ya que π es una costante matematica que equivale aproximadamente a 3,1416 y esto es menor que 4


# escriba cada uno de los enunciados en terminos de desigualdades 
#A) x es positivo 
import numpy as np

x = 5  
print("Para que x sea positivo, se debe cumplir la siguiente desigualdad:")
print("x > 0")
print("resultado de la evaluacion")
print(x > 0)

# B) y es mayo que 6
import numpy as np 
y=6.001
print("y es mayor que 6 si cumple con la siguiente desigualdad")
print("y > 6")
print("resultado de la evaluacion")
print(y > 6)

# C) Z es mayor que 3/2 y menor que  que 1 
import numpy as np 
z= 1.49
print("para que z sea mayor que 3/2 y menos que 1, de debe cumplir la siguiente expresion:")
print("3/2 < z < 1")
print("resultado de la evaluacion:")
print(3/2 <z < 1)

# D) la distacia de r a 5 es 4
import numpy as np 
r=9
print("para que la distacia de r a 5 sea 4, de debe cumplir la siguiente expresion")
print("| r - 5 | = 4")
print("resultado de la evaluacion:")
print(abs(r - 5) == 4)


## FUNCIONES Y SU APLICACION A LA ECONOMIA

# 1)
# Un restaurante de comidas rápidas calcula que la demanda mensual de hamburguesas es:
# 𝑃= 60000/20000 − 𝑥
# También sabe que el costo total de producción es:
# 𝐶= 2000 + 0.56𝑥
# Obtenga una expresión para los ingresos totales y para el beneficio total, y el punto de equilibrio. 

def ingresos_totales(x):
    return (60000 * x - x ** 2) / 20000

def costo_total(x):
    return 5000 + 0.56 * x

def beneficio_total(x):
    return ingresos_totales(x) - costo_total(x)

# Para resolver la ecuación cuadrática y encontrar el punto de equilibrio
import sympy as sp

# Definir la variable simbólica x
x = sp.symbols('x')

# Definir la ecuación B(x) = 0
ecuacion = (60000 * x - x ** 2) / 20000 - (5000 + 0.56 * x)

# Resolver la ecuación cuadrática
puntos_equilibrio = sp.solve(ecuacion, x)
print("Los puntos de equilibrio son:", puntos_equilibrio)


#2) Una compañía reembolsa a su representante de ventas US$ 150 diarios por alojamiento y comidas más 30 centavos por milla recorrida. Escriba una función lineal que exprese el costo diario 𝑐𝑐𝑐𝑐 para la compañía en términos de 𝑥𝑥𝑥𝑥, el número de millas recorridas.

def costo_diario(millas_recorridas):
    
    pendiente = 0.3
    termino_constante = 150
    # Calcular el costo diario usando la función lineal
    costo = pendiente * millas_recorridas + termino_constante
    return costo

millas = 100
costo_total = costo_diario(millas)
print("El costo diario para", millas, "millas recorridas es:", costo_total)



## 3) Un empleado dispone de dos opciones a puesto en una gran corporación. En un puesto le pagan $US 12.5 por hora más un suplemento de US$ 0,75 por unidad producida. En el otro, le pagan US$ 9,2 por hora más un suplemento de US$ 1,3 por unidad producida. Encuentre funciones lineales que expresen los salarios por hora 𝑊 en términos de 𝑥, el número de unidades producidas por hora, para cada una de las opciones. Matemáticas I para las Ciencias Económicas 209 Represente gráficamente las funciones de los salarios y encuentre el punto de intersección de las dos funciones de salarios.
#Interprete el significado del punto de intersección de las gráficas. ¿Cómo usaría esta información para seleccionar la opción correcta si su objetivo fuera obtener el mayor sueldo por hora 

import numpy as np
import matplotlib.pyplot as plt

# Función para el salario por hora en la opción 1
def salario_opcion_1(x):
    return 12.5 + 0.75 * x

# Función para el salario por hora en la opción 2
def salario_opcion_2(x):
    return 9.2 + 1.3 * x

# Encontrar el punto de intersección de las dos funciones
def punto_interseccion():
    # Igualar las dos funciones y resolver para x
    # 12.5 + 0.75x = 9.2 + 1.3x
    # 0.75x - 1.3x = 9.2 - 12.5
    # -0.55x = -3.3
    # x = -3.3 / -0.55
    x_interseccion = -3.3 / -0.55
    return x_interseccion

# Calcular el punto de intersección
x_interseccion = punto_interseccion()
y_interseccion = salario_opcion_1(x_interseccion)

# Graficar las funciones
x_values = np.linspace(0, 10, 100)
y_values_opcion_1 = salario_opcion_1(x_values)
y_values_opcion_2 = salario_opcion_2(x_values)

plt.plot(x_values, y_values_opcion_1, label='Opción 1')
plt.plot(x_values, y_values_opcion_2, label='Opción 2')
plt.scatter(x_interseccion, y_interseccion, color='red', label='Intersección')

plt.xlabel('Unidades producidas por hora')
plt.ylabel('Salario por hora (USD)')
plt.title('Funciones de salario por hora para opciones 1 y 2')
plt.legend()
plt.grid(True)
plt.show()

print("El punto de intersección es:", x_interseccion)


## 4) Un fabricante puede producir grabadoras a un costo de US$ 40 la unidad. Se estima que si las grabadores se venden a un precio de 𝑥 dólares cada una, los consumidores comprarán 120 − 𝑥 de estas al mes. Exprese el beneficio de la compañía como una función del precio unitario, dibuje la gráfica de esta función y utilícela para estimar el precio óptimo de venta, el beneficio óptimo, y determine el dominio y recorrido de esta función. 

# Definir la función de beneficio
def beneficio(x):
    return 160*x - x**2 - 4800

# Encontrar el vértice de la parábola (punto máximo)
# Como la parábola se abre hacia abajo, el vértice es el máximo
x_max = 80
y_max = beneficio(x_max)

# Calcular las intersecciones con el eje x (donde el beneficio es cero)
interseccion_1 = 40
interseccion_2 = 120

# Imprimir los resultados
print("Vértice (precio óptimo de venta, beneficio máximo): ({}, {})".format(x_max, y_max))
print("Intersecciones con el eje x:")
print("Intersección 1:", interseccion_1)
print("Intersección 2:", interseccion_2)


import numpy as np
import matplotlib.pyplot as plt

# Definir la función de beneficio
def beneficio(x):
    return 160*x - x**2 - 4800

# Crear un rango de valores de precio unitario (x)
x_values = np.linspace(0, 120, 100)

# Calcular el beneficio para cada precio unitario (x)
y_values = beneficio(x_values)

# Encontrar el vértice de la parábola (punto máximo)
x_max = 80
y_max = beneficio(x_max)

# Calcular las intersecciones con el eje x (donde el beneficio es cero)
interseccion_1 = 40
interseccion_2 = 120

# Graficar la función de beneficio
plt.plot(x_values, y_values, label='Beneficio')
plt.scatter(x_max, y_max, color='red', label='Vértice (precio óptimo de venta, beneficio máximo)')
plt.scatter(interseccion_1, 0, color='green', label='Intersección 1')
plt.scatter(interseccion_2, 0, color='blue', label='Intersección 2')

# Etiquetas y título del gráfico
plt.xlabel('Precio unitario ($)')
plt.ylabel('Beneficio ($)')
plt.title('Función de beneficio de la compañía')
plt.legend()

# Mostrar el gráfico
plt.grid(True)
plt.show()



## 5) Una compañía de maquinaria tiene un plan de incentivos para sus agentes de ventas. Por cada máquina que un agente venda la comisión es $40 , y esta se incrementa en $0,04 por cada máquina vendida por arriba de 600 unidades. Exprese la comisión como una función del número de unidades vendidas

def comision(unidades_vendidas):
    if unidades_vendidas <= 600:
        return 40 * unidades_vendidas
    else:
        return 40 + 0.04 * (unidades_vendidas - 600)

# Ejemplo de uso
unidades_vendidas = 700
comision_total = comision(unidades_vendidas)
print("La comisión total por {} unidades vendidas es de ${:.2f}".format(unidades_vendidas, comision_total))
