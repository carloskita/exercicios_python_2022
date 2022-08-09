readGain = float(input('Digite quanto voce ganha por hora: '))
readHour = int(input('Digite quantas horas voce trabalhou nesse mes: '))

print('Voce ganhou R$%.2f nesse mes' % (readGain * readHour))