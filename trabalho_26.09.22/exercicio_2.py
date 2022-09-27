import datetime

readWeight = float(input('Digite o peso (em gramas) do produto radioativo: '))
timeElapsed = 0
storedWeight = readWeight

while storedWeight > 0.5:
    storedWeight = storedWeight / 2
    timeElapsed = timeElapsed + 50

print('Para chegar em %.2fg, se passaram %s segundos' % (storedWeight, datetime.timedelta(seconds = timeElapsed)))
