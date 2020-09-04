# =============================================================================
# The prime factors of 13195 are 5, 7, 13 and 29.
# 
# What is the largest prime factor of the number 600851475143 ?
# =============================================================================

# =============================================================================
# Solución:
# 
# Se comienza asumiendo que el número dado (n) es primo por lo que su único y mayor divisor p es 1
# Si el único número primo par (2) divide a n, entonces su mayor factor primo p = 2,
# se sigue diviendo n por p hasta que el residuo deje de 0 y n no sea 1, luego se van probando números impares de la forma p=2*k+1 donde k pertence a los naturales
# estos números impares p sólo puede ser factores primos de n si p<sqrt(n) por definición.
# Así mientras n no se haya dividido completamente hasta 1 y p siga siendo menor que la raíz cuadrada de n,
# se repite el proceso de dividir n hasta que su residuo deje de ser 0.
# 
# El mayor factor primo es el máximo entre p y el resultado de todas las divisiones realizadas
# (Lo de p < n**0.5 y p=2*k+1 se hace para optimizar el código)
# =============================================================================
    
n = 600851475143
lim = int(n**0.5)
p = 1
if n%2 == 0:
    p = 2
    while n%2 == 0:
        n = n//2 
k = 0

while (p < lim) and (n > 1):
    k += 1
    p = 2*k + 1
    if n%p == 0:
        while n%p == 0:
            n = n//p

print("Mayor factor primo es {}".format(max(n, p)))