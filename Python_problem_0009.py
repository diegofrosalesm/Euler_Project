# =============================================================================
# A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,
# a^2 + b^2 = c^2
# 
# For example, 3^2 + 4^2 = 9 + 16 = 25 = 5^2.
# 
# There exists exactly one Pythagorean triplet for which a + b + c = 1000.
# Find the product abc.
# =============================================================================

# =============================================================================
# Solución:
#     Ya que a y b deben ser números naturales, esto limita la búsqueda a cada par (a,b) tal que
#     tanto a como b estén entre cero y la mitad del objetivo (target) (0, target/2)
#     por cada número a en este rango, se prueban los valores posibles de b (desde 0 hasta n/2)
#     hasta encontrar (a,b) enteros que hagan que a+b+(a**2 + b**2)**0.5 = target y a*b*c no sea 0
# 
# =============================================================================
target = 1000

a = target//2
while a > 0:
    b = target//2 - a
    while b < target//2:
        c = (a**2 + b**2)**0.5
        total = a + b + c
        prod = a*b*c
        if total == target and prod != 0:
            break
        else:
            b += 1
    if total == target and prod != 0:
        print("El resultado es: {}, a: {}, b: {}, c: {}".format(prod, a, b, c))
        break
    else:
        a -= 1