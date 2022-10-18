#Usar de separacoes de decimais com numeros de 1 a 9 e 10 a 90

decimalRead = {1: 'dez', 2: 'vinte', 3: 'trinta', 4: 'quarenta', 5: 'cinquenta', 6: 'sessenta', 7: 'setenta', 8: 'oitenta', 9: 'noventa'} #Typando as variaveis
singleRead = {1: 'um', 2: 'dois', 3: 'tres', 4: 'quatro', 5: 'cinco', 6: 'seis', 7: 'sete', 8: 'oito', 9: 'nove'}

readNum = int(input('Digite um numero de 1 a 99 para ler por extenso: '))

numStrings = [int(a) for a in str(readNum)] #Separar os numeros

# print('Decimal: %d Singular: %d' % (numStrings[0], numStrings[1])) #exemplo para testar as separacoes

if readNum > 9 and numStrings[1] == 0:
    print('Numero por extenso: %s' % (decimalRead.get(numStrings[0])))
    
elif readNum > 9:
    print('Numero por extenso: %s e %s' % (decimalRead.get(numStrings[0]), singleRead.get(numStrings[1])))
    
else:
    print('Numero por extenso: %s' % (singleRead.get(numStrings[0])))