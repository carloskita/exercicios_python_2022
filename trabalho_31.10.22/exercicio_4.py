ficha = list()
mediaGeral = 0

while True:
    nome = str(input('Nome: '))
    nota1 = float(input('Nota 1: '))
    nota2 = float(input('Nota 2: '))
    nota3 = float(input('Nota 3: '))
    media = (nota1 + nota2 + nota3) / 3
    result = ''
    if media >= 6:
        result = 'Aprovado'
    else:
        result = 'Reprovado'
    ficha.append([nome, [nota1, nota2, nota3], media, result])
    mediaGeral = mediaGeral + media
    readAwnswer = input('Quer continuar? [S/N]: ')
    if readAwnswer in 'Nn':
        break
    
print(f'{"No.":<4}{"NOME":<10}{"MEDIA":<8}{"STATUS":>8}')
    
for i, a in enumerate(ficha):
    print(f'{i:<4}{a[0]:<10}{a[2]:<8.1f}{a[3]:>8}')
    
# print('MediaGeral: %.2f\n i = %d' % (mediaGeral, i)) DEBUG, please ignore
print('A media geral da turma vai ser: %.2f' % (mediaGeral / (i+1)))