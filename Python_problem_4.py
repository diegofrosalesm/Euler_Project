# =============================================================================
# A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.
# 
# Find the largest palindrome made from the product of two 3-digit numbers.
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
        if (i*j == n) and (j >= nmin) and (j <= nmax):
            print('Maximo palindromo: {} ({} x {})'.format(n, i, j))
            break
        else:
            n -= 1
            i = nmax
    elif (i == nmin) and (n == maxpalindrome(n+1)):
        i = nmax
        n -= 1
    else:
        i -= 1