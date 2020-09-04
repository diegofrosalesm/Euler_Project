# =============================================================================
# By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.
# 
# What is the 10 001st prime number?
# =============================================================================

# =============================================================================
# 
# Solución:
#     
#     Nada elegante aquí: simplemente se van chequeando números impares (p) hasta hallar uno en la posición (position) buscada
#     Se usa el criterio de divisibilidad de los primos (si el módulo de p con algún otro primo es cero, p no es primo y se termina el bucle)
# 
# =============================================================================

primes = [2]
position = 10001
k = 0
counter = 1
while counter != position:
    k += 1
    p = 2*k + 1
    flag = True
    for i in primes:
        if p%i == 0:
            flag = False
            break
    if flag:
        primes.append(p)
        counter += 1

print("El {}-esimo número primo es: {}".format(position, primes[counter-1]))