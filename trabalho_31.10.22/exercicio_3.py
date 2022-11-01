listRealNum = []
print ('Informe os 10 numeros reais')
for i in range(10):
    listRealNum.append(float(input('Numero '+ str(i+1) + ':\n')))
listRealNum.reverse()
print (listRealNum)