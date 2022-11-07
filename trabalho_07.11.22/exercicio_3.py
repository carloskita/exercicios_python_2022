def somaImposto(taxaImposto, custo):
    convertPercentage = 1 + (taxaImposto / 100)
    
    newCusto = float(custo * convertPercentage)
    
    return newCusto
    

readPrice = float(input('Digite o preco do produto: '))
readTax = float(input('Digite (em porcentagem) o imposto: '))

taxedPrice = somaImposto(readTax, readPrice)

print('O preco do produto R$%.2f vai ser, com as taxas, R$%.2f' % (readPrice, taxedPrice))