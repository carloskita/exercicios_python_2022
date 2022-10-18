# def changeLetter(wantToChange, changeFor,phrase):
#     phrase = phrase.replace(wantToChange, changeFor, len(phrase))
#     return phrase

# print('A frase substituida vai ser: %s' % (phraseRead.replace(letter1Read, 'temp').replace(letter2Read, letter1Read).replace('temp', letter2Read)))

phraseRead = str(input('Digite uma frase: '))

letter1Read = input('Digite uma letra para trocar na frase: ')
letter2Read = input('Digite outra letra para trocar na frase: ')

sizeString = len(phraseRead)
phraseList = list(phraseRead)

for i in range(sizeString):
    if phraseList[i] in letter1Read:
        phraseList[i] = letter2Read
    elif phraseList[i] in letter2Read:
        phraseList[i] = letter1Read
    
print('A frase substituida vai ser: %s' % (''.join(phraseList)))