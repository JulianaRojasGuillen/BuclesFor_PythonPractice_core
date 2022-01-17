# establece tres variables: lowNum, highNum, mult. Comenzando en lowNum 
# y pasando por highNum, imprime solo los enteros que sean múltiplos de mult.
#  Por ejemplo, si lowNum=2, highNum=9 y mult=3. El bucle debe imprimir 3, 6, 9 (en líneas sucesivas). 

def contadorFlexible(lowNum, highNum, mult):
    linea=[]
    for i in range(lowNum,highNum+1):
        if i%mult==0:
            linea.append(i)
    print(linea)
    

resultado = contadorFlexible(2,9,3)
print(resultado)