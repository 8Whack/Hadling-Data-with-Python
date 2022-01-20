cupcakes = open('CupcakeInvoices.csv')
for line in cupcakes:
    print (line)

cupcakes.seek(0)

for line in cupcakes:
    line = line.strip()
    values = line.split(',')
    print(values[2])

cupcakes.seek(0)

for line in cupcakes:
    line = line.strip()
    line = line.split(',')
    quantity = float(line[3])
    price = float(line[4])
    total = quantity * price
    print(total)

cupcakes.seek(0)
    
grand_total = 0
for line in cupcakes:
    line = line.strip()
    line = line.split(',')
    quantity = float(line[3])
    price = float(line[4])
    total = quantity * price
    grand_total += total

#just use round(number, x) where x is the number of decimal places to round.
print(round(grand_total, 2))

cupcakes.close