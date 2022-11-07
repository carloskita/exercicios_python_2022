def positiveOrNegative(num):
    defineSit = 'N'
    
    if num >= 0:
        return 'P'
        
    return defineSit


readNum = int(input('Digite um numero, pois ira retornar P ou N: '))

numSituation = positiveOrNegative(readNum)

print('O retorno vai ser', (numSituation))