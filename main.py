#MENU#
menu = ['Burger - ₹120.50','Pizza - ₹250.45','Coffee - ₹70.62',
        'Sandwich - ₹100.12','Cold Drink - ₹90.254']

#MENU DISPlAY#
print('')
print('------- MENU -------')
for numbering,items in enumerate(menu, 1):
    print(numbering, items)

#ORDERING#
print('')
print('Welcome START ORDERING or N to stop ')
print('')
quantities = []
prices = []
item_names = []
while True:
    item_code = input('Enter item code: ')
    if item_code == 'N' or item_code == 'n':
        break

    item_code = int(item_code) - 1
    selected_items = menu[item_code]

    #PRICES#
    p = float(selected_items.split('-')[1].replace('₹',''))
    prices.append(p)

    #ITEM-NAMES#
    i = str(selected_items.split('-')[0])
    item_names.append(i)

    #QUANTITIES#
    q = int(input('Quantity: '))
    quantities.append(q)

print('')    

#SUB-TOTAL#
sub_total = 0
for x, y in zip(quantities, prices):
    sub_total = sub_total + (x*y)

#TIP#
while True:
    Tip = int(input('Enter Tip Percentage: '))
    if Tip >= 0:
        break
    print('Tip can not be negative')
    
tip = round(sub_total*Tip/100, 2)
print('')

#RUNNING-TOTAL#
running_total = sub_total + tip

#DISCOUNT CONDITION#
Discount = 0
if running_total >= 1000:
    Discount = round(sub_total * 0.05, 2)
elif running_total >= 500 or running_total < 1000:
    Discount = round(sub_total * 0.02, 2)
else:
    Discount = 0

#TOTAL-BILL#
total_bill = round(running_total - Discount, 2)

#FINAL-BILL-FORMAT#
bill_per_person = 0
def final_bill():
    print('\n' + '=' * 48)
    print('Beso Dulce café'.center(48))
    print('=' * 48)
    print('')
    print(f"{'ITEM':<20}{'QTY':<10}{'PRICE':<10}{'Total':<10}")
    print('-' * 45)
    for m,n,o in zip(item_names,quantities,prices):
        total = round(n * o , 2)
        print(f"{m:<20}{n:<10}{o:<10}{total:<10}")
    print('-' * 45)
    print(f'Tip: ₹{str(tip).ljust(45)}')
    print(f'Sub Total: ₹{str(running_total).ljust(45)}')
    print(f'Discount: ₹{str(Discount).ljust(45)}')
    print('-' * 45)
    print(f'GRAND TOTAL: ₹{str(total_bill).ljust(45)}')
    print(f'Bill per person: {str(bill_per_person).ljust(45)}')
    print('=' * 48)
    print('THANKS FOR ORDERING!'.center(48))
    print('=' * 48)
    

#SPLIT-CONDITIONS#
split = str(input('Do you want to split bill? Y/N '))
print('')
if split == 'Y':
    number_of_persons = int(input('Enter number of person: '))
    bill_per_person = round(total_bill/number_of_persons, 2)
    final_bill()
elif split == 'y':
    number_of_persons = int(input('Enter number of person: '))
    bill_per_person = round(total_bill/number_of_persons, 2)
    final_bill()
else:
    final_bill()
    
    













