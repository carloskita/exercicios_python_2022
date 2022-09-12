List_readMonth = int(input("Digite um mes entre 1 e 12: "))

if List_readMonth in (1,3,5,7,8,10,12):
    monthLength = 31
elif List_readMonth == 2:
    monthLength = 30
    
List_readDay = int(input("Digite um dia entre 1 e 31: "))

if List_readDay < monthLength:
    List_readDay += 1
else:
    List_readDay = 1
    if List_readMonth == 12:
        List_readMonth = 1
    else:
        List_readMonth += 1
        
print("O proximo dia vai ser: %d/%d" % (List_readDay, List_readMonth))