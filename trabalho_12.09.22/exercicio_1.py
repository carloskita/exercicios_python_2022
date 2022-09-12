List_readNum = [0]*3

for i in range(3):
    List_readNum[i] = input("Digite 3 numeros para ver em ordem descrescente e ordem crescente: ")

print("Ordem crescente: ", sorted(List_readNum))
print("Ordem decrescente: ", sorted(List_readNum, reverse=True))