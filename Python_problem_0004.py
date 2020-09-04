# =============================================================================
# A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.
# 
# Find the largest palindrome made from the product of two 3-digit numbers.
# =============================================================================

# =============================================================================
# Solución:
# La función ispalindrome determina si un número (x) es palindrómico comparando los números en la primera posición mitad de x
# son iguales a sus posiciones invertidas en la segunda mitad (primero con último, segundo con penúltimo, etc)
# 
# La función maxpalindrome se vale de ispalindrome para hallar el máximo número palindrómico que puede formarse a partir de un número dado
# Nada elegante aquí, simplemente se le resta 1 al número hasta que la ispalindrome halle algo
# 
# ndigit se usa para generalizar la solución a más números que aquellos de 3 cifras (ndigit = 2 da el resultado de 9009)
# 
# se crea el máximo número de ndigit cifras dadas (nmax = 9*10^ndigit+9*10^(ndigit-1)+...+9*10^0)
# de igual forma se crea el número mínimo de ndigit cifras dadas (nmin = 100 para 3 cifras, 1000 para 4, etc)
# 
# se comienza a iterar con el máximo palíndromo que se puede formar con números de ndigit cifras (nmax*nmax)
# si el número i es múltiplo del máximo palíndromo considerado n entonces se revisa que j=n/i también tenga el número de cifras
# adecuado, es decir que esté entre nmin y nmax. Si j no tiene las cifras permitidas, se baja al siguiente n palindrómico máximo y se resetea i
# 
# Si ninguna i entre nmax y nmin divide perfectamente a n, se usa una nueva i = i-1, pero si esta i llega a ser =nmin, eso significa que
# n no tiene ningún divisor en el rango buscado de i y j, por lo que se resetea i a nmax y se busca otro n palindrómico menor
# para n = 5 se tarda bastante, pero funciona
# =============================================================================
def ispalindrome(x):
    plist = list(str(x))
    plen = len(plist)
    for i in range(plen//2):
        if plist[i] != plist[plen-1-i]:
            return False
    return True

def maxpalindrome(x):
    while not ispalindrome(x):
        x -= 1
    return x
    
ndigit = 3
nmax = 0
for i in range(ndigit):
    nmax += 9*10**i
nmin = 10**(ndigit-1)

i = nmax
n = nmax**2

while i >= nmin:
    n = maxpalindrome(n)
    if n%i == 0:
        j = n//i
        if (j >= nmin) and (j <= nmax):
            print('Maximo palindromo: {} ({} x {})'.format(n, i, j))
            break
        else:
            n -= 1
            i = nmax
    elif (i == nmin):
        i = nmax
        n -= 1
    else:
        i -= 1