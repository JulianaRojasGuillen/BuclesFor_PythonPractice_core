#Imprime números enteros del 1 al 100. Si es divisible por 5, imprime "Coding” en su lugar.
#Si es divisible por 10, imprime "Coding Dojo".

for i in range(1,101):
    if i%10==0:
        print ("Coding Dojo")
    elif i%5==0:
        print ("Coding")
    else: 
        print (i)