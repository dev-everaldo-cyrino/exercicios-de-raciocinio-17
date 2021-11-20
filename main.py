impares = 0
pares = 0
num = int(input('digite um numero: '))
for x in range(num):
    x +=1
    if x %2 ==1:
        impares +=1
    else:
        pares +=1
print('''
      numa lista de {} numeros
      {} são impares e {} são pares'''.format(num,impares,pares))