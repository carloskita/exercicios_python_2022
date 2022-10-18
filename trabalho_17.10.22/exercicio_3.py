def cesar(data, key):
    alphabetString = 'abcdefghijklmnopqrstuvwyz'
    newData = ''
    
    for c in data:
        index = alphabetString.find(c)
        if index == -1:
            newData += c
        else:
            newIndex = index + key
            newIndex = newIndex % len(alphabetString)
            newData += alphabetString[newIndex:newIndex + 1]
    
    return newData

key = 3 #Chave para codificar, pula as posicoes que foram colocadas na variavel

originalRead = input('Digite sua frase para codificar (nao utilize acento e apenas em letra minuscula): ')

encryptDef = cesar(originalRead, key)

print('Codificada: %s' % (encryptDef))