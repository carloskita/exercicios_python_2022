readHeight = float(input('Digite sua altura em metros: '))
readWeight = float(input('Digite seu peso em Kg: '))

print('Seu IMC vai ser: %.2f' % (readWeight / (readHeight ** 2)))