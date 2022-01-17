# agrega los enteros impares del 0 al 500,000, e imprime la suma final.

sum=0
for i in range (0,500001):
    if i%2 != 0:
        sum+=i
print(sum)