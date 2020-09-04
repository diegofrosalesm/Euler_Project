# =============================================================================
# The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.
# 
# Find the sum of all the primes below two million.
# =============================================================================

# =============================================================================
# Solución
# 
# Para ahorrar tiempo en los problemas futuros se define una función que genera números primos por debajo de
# cierto límite x, por criterio de divisibilidad.
# 
# La lista generada de números primos se suma elemento a elemento.
# =============================================================================
def primegen(x):
    k = 0
    p = 1
    primes = [2]
    while p < x:
        k += 1
        p = 2*k + 1
        flag = True
        for i in primes:
            if p%i == 0:
                flag = False
                break
        if (flag )and (p < x):
            primes.append(p)
    return primes

n = sum(primegen(2000000))
print("El resultado es: {}".format(n))