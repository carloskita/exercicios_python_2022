def sumCalc(a, b, c):
    sum = a + b + c
    return sum

readNum = []

readNum.append(float(input('Digite um numero para fazer a soma(1): ')))
readNum.append(float(input('Digite um numero para fazer a soma(2): ')))
readNum.append(float(input('Digite um numero para fazer a soma(3): ')))

print('A soma dos numeros vai ser: %.1f' % (sumCalc(readNum[0], readNum[1], readNum[2])))