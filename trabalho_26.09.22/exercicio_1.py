readNum = 0 #Definindo o tipo da variavel
resultPar = 0
resultImpar = 0

while readNum <= 1000:
    readNum = int(input('Digite alguns numeros para saber as somas dos numeros impares e pares (digite 1000 para parar o programa): '))
    
    if readNum >= 1000:
        print("A soma dos numeros pares sao: %d \nA soma dos numeros impares sao: %d" % (resultPar, resultImpar))
        break
    
    if readNum % 2 == 0:
        resultPar = resultPar + readNum
    else:
        resultImpar = resultImpar + readNum
        
    print("A soma dos numeros pares sao: %d \nA soma dos numeros impares sao: %d" % (resultPar, resultImpar))