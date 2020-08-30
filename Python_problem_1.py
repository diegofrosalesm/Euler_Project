#Multiples of 3 and 5

#Problem 1

#If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.
#Find the sum of all the multiples of 3 or 5 below 1000.


#Solución:
    
#Se inicia el resultado de la sumatoria en cero
#Si i mod 3 y/o i mod 5 dan cero, i es múltiplo de alguno de esos números
#por tanto i se suma al resultado final

total = 0
for i in range(1000):
    if (i%3==0)or(i%5==0):
        total += i

print("El resultado es {}".format(total))