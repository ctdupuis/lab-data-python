open_file = open('CupcakeInvoices.csv')

for row in open_file:
    print(row)


for line in open_file:
    line = line.rstrip('\n').split(',')
    print(line[2])

invoices = []

for line in open_file:
    line = line.rstrip('\n').split(',')
    invoice = float(line[-1]) * float(line[3])
    invoices.append(invoice)

print(invoices)


total = 0

for line in open_file:
    line = line.rstrip('\n').split(',')
    cost = float(line[-1]) * float(line[3])
    total += cost

print(total)

open_file.close()