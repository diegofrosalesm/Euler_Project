# =============================================================================
# 2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.
# 
# What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?
# =============================================================================

# =============================================================================
# Solución:
#     
# El número más pequeño que es múltiplo de un conjunto de números dados (r) es aquel que se puede formar con los factores primos
# comunes y no comunes de los números en r, elevados a su mayor exponente cada uno. Por lo tanto el problema se divide en 2 partes:
#     
# El el primer bucle for se hallan todos los números primos (primes) dentro de r por simple criterio de divisibilidad (esto ya se hizo en el problema 3)
# El tercer bucle toma cada número en r, y lo divide por todos y cada uno de los números primos hallados. Si resulta que algún número primo divide a un
# número en r, se cuentan (counter) cuantas veces lo puede dividir perfectamente, es decir se calcula el exponente de ese factor primo en ese número
# el mayor exponente contado de cada número primo se asigna a un índice en powers igual al índice que tiene ese número primo en primes
# y luego simplemente se hace una productoria entre cada número primo elevado a su exponente mayor
# =============================================================================
n = 20
r = list(range(n+1)[1:])
primes = []
powers = []
for i in r:
    flag = True
    for j in primes:
        if i%j == 0 and (j!= 1):
            flag = False
    if flag:
        primes.append(i)
        
nprimes = range(len(primes))

for i in nprimes:
    powers.append(0)

for i in r:
    for j in primes:
        counter = 0
        if i%j == 0:
             n = i
             while n%j == 0 and (j != 1):
                 n = n//j
                 counter += 1
             if counter > powers[primes.index(j)]:
                powers[primes.index(j)] = counter

total = 1            
for i in nprimes:
    total = total*primes[i]**powers[i]

print("El resultado es {}".format(total))