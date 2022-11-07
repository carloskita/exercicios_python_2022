readList1 = []
readList2 = []

for i in range(10):
    readList1.append(int(input('Digite numero para a primeira lista, posicao do elemento [%d]: ' % (i+1))))
    
for i in range(10):
    readList2.append(int(input('Digite numero para a segunda lista, posicao do elemento [%d]: ' % (i+1))))
    
listinterleaved = readList1 + readList2
listinterleaved[::2] = readList1
listinterleaved[1::2] = readList2

print('A lista intercalada vai ser: %s' % (str(listinterleaved)))