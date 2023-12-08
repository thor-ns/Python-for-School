items = input("How many items are in your cart? ")
items = int(items)
if items == 0:
    print("No items are in your cart")
    exit()

def shopping_list(items):
    price = 0
    items -= 1
    x = 0
    while x < items:
        price += 2.95
        x += 1
    price += 10.95
    print(price)


shopping_list(items)