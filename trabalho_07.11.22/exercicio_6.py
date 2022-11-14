def intercalar(a, b):
    listinterleaved = a + b
    listinterleaved[::2] = a
    listinterleaved[1::2] = b
    
    return listinterleaved

readList1 = []
readList2 = []

for i in range(10):
    readList1.append(int(input('Digite numero para a primeira lista, posicao do elemento [%d]: ' % (i+1))))
    
for i in range(10):
    readList2.append(int(input('Digite numero para a segunda lista, posicao do elemento [%d]: ' % (i+1))))

print('A lista intercalada vai ser: %s' % (str(intercalar(readList1, readList2))))