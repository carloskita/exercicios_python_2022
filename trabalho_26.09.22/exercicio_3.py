cityPopsA = 5000000
cityPopsB = 7000000
yearsElapsed = 0

while cityPopsA < cityPopsB:
    cityPopsA += (cityPopsA * 0.03)
    cityPopsB += (cityPopsB * 0.02)
    yearsElapsed += 1
    
print('Serao necessarios %d anos para a cidade A passar a cidade B em população' % (yearsElapsed))
    