readNum = float(input("Digite uma nota, para fechar o programa, digite -1: "))
grades = []
addplus = 0
while readNum != -1:
   grades.append(readNum)
   addplus += readNum
   media = addplus/len(grades)
   Menor = 0
   Maior = 0
   for maior in grades:
       if maior > media:
           Maior += 1
       if maior < 7:
           Menor += 1
   print("%d\n%s\n%s\n%.2f\n%.1f\n%d\n%d" % (len(grades), format(grades), format(grades[::-1]), addplus, media, Maior, Menor))
   readNum = float(input("Digite uma nota, para fechar o programa, digite -1: "))