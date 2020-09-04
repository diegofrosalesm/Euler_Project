# =============================================================================
# The sum of the squares of the first ten natural numbers is,
# 1^2 + 2^2 + ... + 10^2 = 385
# The square of the sum of the first ten natural numbers is,
# (1 + 2 + ... + 10)^2 = 55^2 = 3025
# Hence the difference between the sum of the squares of the first ten natural numbers and the square of the sum is
# 
# 3025 - 385 = 2640
# 
# Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.
# =============================================================================

# =============================================================================
# Solución:
# 
# Este problema es muy sencillo sabiendo sobre series: siendo n el n-simo número natural se tiene que 
#     1 + 2 +...+ n = n(n + 1)/2
#     1^2+ 2^2 +...+ n^2 = n(n+1)(2n+1)/6
#     
# Entonces, la diferencia entre el cuadrado de la primera ecuación y la segunda es:
#     (n(n+1)/2)^2 - n(n+1)(2n+1)/6
#     n^2*(n+1)^2/4 - n(n+1)(2n+1)/6
#     [3n^2*(n+1)^2 - 2n(n+1)(2n+1)]/12
#     n(n+1)[3n(n+1) - 2(2n+1)]/12
#     n(n+1)[3n^2 +3n -4n -2]/12
#     n(n+1)(3n^2 -n -2)/12
# =============================================================================
    
n = 100
dif = n*(n+1)*(3*n**2-n-2)//12
print(dif)