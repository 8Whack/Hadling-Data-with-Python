import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np



cupcakes = open('CupcakeInvoices.csv')
for line in cupcakes:
    print (line)


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

cupcakes.seek(0)

total_vanilla = 0
total_chocolate = 0
total_strawberry = 0
for line in cupcakes:
    line = line.strip()
    line = line.split(',')
    if line[2] == 'Vanilla':
        total_vanilla += float(line[3])
    elif line[2] == 'Chocolate':
        total_chocolate += float(line[3])
    elif line[2] == 'Strawberry':
        total_strawberry += float(line[3])
    
cupcakes.seek(0)

revenue_vanilla = 0
revenue_chocolate = 0
revenue_strawberry = 0
for line in cupcakes:
    line = line.strip()
    line = line.split(',')
    if line[2] == 'Vanilla':
        revenue_vanilla += float(line[4]) * float(line[3])
    elif line[2] == 'Chocolate':
        revenue_chocolate += float(line[4]) * float(line[3])
    elif line[2] == 'Strawberry':
        revenue_strawberry += float(line[4]) * float(line[3])
#print(revenue_chocolate, revenue_vanilla, revenue_strawberry)

cupcakes.seek(0)

quantity = []
purchases = []
visits = 0

for line in cupcakes:
    line = line.strip()
    line = line.split(',')
    quantity.append(float(line[3]))
    purchases.append(visits+1)
    visits += 1

# print(quantity)
# print(purchases)

cupcakes.close

flavors = ['Vanilla', 'Chocolate', 'Strawberry']
amt_sold = [total_vanilla, total_chocolate, total_strawberry]
revenue = [revenue_vanilla, revenue_chocolate, revenue_strawberry]

# uncomment these out one at a time to see the different graphs.

# plt.bar(flavors, amt_sold, color = 'green')
# plt.title('Cupcake Sales', color = 'purple')
# plt.xlabel('Type of Cupcake', color = 'purple')
# plt.ylabel('Quantity Sold', color = 'purple')

# plt.bar(flavors, revenue, color = 'blue')
# plt.title('Cupcake Revenue', color = 'purple')
# plt.xlabel('Type of Cupcake', color = 'purple')
# plt.ylabel('Total Sold', color = 'purple')

# plt.scatter(purchases, quantity, color = 'brown')
# plt.title('Orders over the day', color = 'purple')
# plt.xlabel('Orders', color = 'purple')
# plt.ylabel('Amount purchased', color = 'purple')

plt.show()