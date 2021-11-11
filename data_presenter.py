open_file = open('CupcakeInvoices.csv')

# for row in open_file:
#     print(row)


# for line in open_file:
#     line = line.rstrip('\n').split(',')
#     print(line[2])

# invoices = []

# for line in open_file:
#     line = line.rstrip('\n').split(',')
#     invoice = float(line[-1]) * float(line[3])
#     invoices.append(invoice)

# print(invoices)


# total = 0

# for line in open_file:
#     line = line.rstrip('\n').split(',')
#     cost = float(line[-1]) * float(line[3])
#     total += cost

# print(total)

# Dictionary == Object in JS
cupcake_flavors = {
    "Chocolate": 0,
    "Vanilla": 0,
    "Strawberry": 0
}

for line in open_file:
    line = line.rstrip('\n').split(',')
    flavor = line[2]
    cupcake_flavors[f'{line[2]}'] += 1

    # if flavor == "Strawberry":
    #     straw.append(flavor)
    # elif flavor == "Chocolate":
    #     choc.append(flavor)
    # else: 
    #     nilla.append(flavor)

print(f'There are {cupcake_flavors["Chocolate"]} Chocolate cupcakes, {cupcake_flavors["Strawberry"]} Strawberry cupcakes and {cupcake_flavors["Vanilla"]} Vanilla cupcakes')

# print(f'There are {len(straw)} Strawberry cupcakes, {len(choc)} Chocolate cupcakes and {len(nilla)} Vanilla cupcakes')

open_file.close()