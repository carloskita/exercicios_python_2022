from datetime import datetime

def convertTime(readedTime):
    convertedTime = datetime.strptime(readedTime, "%H:%M")
    
    return convertedTime

def printConvertedTime(readedTime):
    print('O tempo convertido vai ser: %s' % (readedTime.strftime("%r")))
    
    return

temp = 0

while temp != 1:
    readTime = str(input('Digite o horario no padrao imperial (exemplo: 22:30 ou 05:00), digite -1 para terminar o loop: '))
    
    if readTime == "-1":
        break

    convertedTime = convertTime(readTime)
    printConvertedTime(convertedTime)