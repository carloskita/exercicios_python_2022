def counNum(a):
    counted = len(a)
    return counted

readNum = str(input('Digite um numero para ver quantos elementos tem nele: '))

print('A quantidade de elementos sao: %s' % (counNum(readNum)))