# =============================================================================
# Each new term in the Fibonacci sequence is generated by adding the previous two terms. By starting with 1 and 2, the first 10 terms will be:
# 
# 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...
# 
# By considering the terms in the Fibonacci sequence whose values do not exceed four million, find the sum of the even-valued terms.
# =============================================================================

# =============================================================================
# Solución:
# 
# Se inicializa el resultado de la sumatoria en 0, y los 2 primeros números de la secuencia en 1 y 2
# El último número de la secuencia es el que importa a la hora de sumar (el anterior por definición ya es un valor evaluado)
# Si el último número de la secuencia es menor al límite de 4 millones y además es par, se suma al total.
# =============================================================================
a = 1
b = 2
total = 0

while b < 4000000:
    if b%2 == 0:
        total += b
    b = b + a
    a = b - a
    
print("El resultado es {}".format(total))