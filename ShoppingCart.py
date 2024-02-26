import time as t
import random as ran
#_______________________________________________
#all of the special errors that get raised throughtout the program
class InsufficientStockError(Exception):
    pass
class ProductNotFoundError(Exception):
    pass
class ProductExists(Exception):
    pass
class EmptyCart(Exception):
    pass
class InvalidInput(Exception):
    pass
#_______________________________________________
#All of my classes 
class Department(): #This class has all the methods that get passed on to the other classes, making it easier to change/add any functions
    def __init__(self):
        pass
    def List(self):
        try:
            print("This department has the following items available: ")
            for x in self.stock:
                if(self.stock[x] == self.stock["NAN"]):
                    continue
                else:
                    print(f"  ◦ {x}")
        except Exception as e:
            print(str(e))
    def Stock(self, product="NAN"):
        try:
            if(product not in self.stock):
                raise ProductNotFoundError("This product doesn't exist")
            elif(self.stock.setdefault(product) > 0):
                print(f"There are %s units of %s"%(self.stock.setdefault(product), product))
            else:
                raise InsufficientStockError(f"There is are no more %s in stock. Sorry for the inconvenience"%(product))
        except InsufficientStockError as e:
            print(str(e))
        except ProductNotFoundError as e:
            print(str(e))
        except Exception as e:
            print(str(e))
    def Price(self, product="NAN"):
        try:
            if(product not in self.stock):
                raise ProductNotFoundError("This product doesn't exist")
            else:
                print(f"%s cost %s"%(product, self.price.setdefault(product)))
                return self.price.setdefault(product)
        except ProductNotFoundError as e:
            print(str(e))
        except Exception as e:
            print(str(e))
    def Restock(self, product, quantity):
        try: 
            if(product not in self.stock):
                raise ProductNotFoundError("This product doesn't exist")
            elif(product == "NAN"):
                raise ProductNotFoundError("This product doesn't exist")
            else:
                self.stock[product] += quantity
        except ProductNotFoundError as e:
            print(str(e))
        except Exception as e:
            print(str(e))
        else:
            print(f"{quantity} {product} have been restocked")
            print(f"There are now %s in stock"%self.stock.setdefault(product))
    def RemoveStock(self, product, quantity):
        try:
            if(product not in self.stock):
                raise ProductNotFoundError("This product doesn't exist")
            elif(product == "NAN"):
                raise ProductNotFoundError("This product doesn't exist")
            elif(self.stock[product] <= 0):
                raise InsufficientStockError("Unable to remove any more stock")
            else:
                self.stock[product] -= quantity
        except ProductNotFoundError as e:
            print(str(e))
        except InsufficientStockError as e:
            print(str(e))
        except Exception as e:
            print(str(e))
        else:
            print(f"{quantity} {product} have been unstocked")
            print(f"There are now %s in stock"%self.stock.setdefault(product))
    def AddItem(self, newProduct, newStock, newPrice):
        try:
            if(newProduct in self.stock):
                raise ProductExists("Product already exists")
            else:
                self.stock[newProduct] = newStock
                self.price[newProduct] = newPrice
        except ProductExists as e:
            print(str(e))
        except Exception as e:
            print(str(e))
        else:
            print(f"New product: {newProduct} has been added")
    def RemoveItem(self, product):
        try:
            if(product == "NAN"):
                raise ProductExists("This item already exists")
            else:
                del self.stock[product]
                del self.price[product]
        except KeyError:
            print(f"error: {product} item doesn't exist")
        except Exception as e:
            print(str(e))
        else:
            print(f"{product} item has been deleted")

class Frozen(Department):
    def __init__(self):
        self.price = {
            "NAN": "N/A",
            "vanilla ice cream": 4.50,
            "chocolate ice cream": 5.50,
            "strawberry ice cream": 4.75,
        }   
        self.stock = { 
            "NAN": 0, 
            "vanilla ice cream": 30,
            "chocolate ice cream": 30,
            "strawberry ice cream": 30,
        }
        super().__init__()

class Bakery(Department):
    def __init__(self):
        self.price = {
            "NAN": "N/A",
            "blueberry muffin": 2.75,
            "chocolate chip muffin": 2.75,
            "cinnamon bun": 5.00,
            "bagel": 3.50,
        }
        self.stock = {
            "NAN": 0,
            "blueberry muffin": 25,
            "chocolate chip muffin": 30,
            "cinnamon bun": 20,
            "bagel": 40,
        }
        super().__init__()

class Deli(Department):
    def __init__(self):
        self.price = {
            "NAN": "N/A",
            "ground beef": 39.00,
            "chicken thighs": 35.00,
            "cow liver": 40.00,
        }
        self.stock = {
            "NAN": 0,
            "ground beef": 50,
            "chicken thighs": 35,
            "cow liver": 20,
        }
        super().__init__()

class Canned(Department):
    def __init__(self):
        self.price = {
            "NAN": "N/A",
        }
        self.stock = {
            "NAN": 0,
        }
        super().__init__()

class Dairy(Department):
    def __init__(self):
        self.price = {
            "NAN": "N/A",
            "milk": 5.50,
            "butter": 3.00
        }
        self.stock = {
            "NAN": 0,
            "milk": 60,
            "butter": 40,
        }
        super().__init__()

class Fresh(Department):
    def __init__(self):
        self.price = {
            "NAN": "N/A",
            "apples": 2.55,
            "bananas": 3.00,
            "pears": 1.55,
            "blackberries": 2.99,
            "raspberries": 3.99,
            "blueberries": 5.69,
            "dragonfruit": 20.54,
            "kiwi": 13.25,
        }
        self.stock = {
            "NAN": 0,
            "apples": 45,
            "bananas": 50,
            "pears": 35,
            "blackberries": 40,
            "raspberries": 45,
            "blueberries": 35,
            "dragonfruit": 20,
            "kiwi": 15,
        }
        super().__init__()

class Health(Department):
    def __init__(self):
        self.price = {
            "NAN": "N/A",
            "human liver": 5000000.00,
            "full human body": 45000000.00,
            "tylonel": 30.00,
            "advil": 35.00, 
        }
        self.stock = {
            "NAN": 0,
            "human liver": 4,
            "full human body": 2,
            "tylonel": 20,
            "advil": 15
        }
        super().__init__()

class Alchohol(Department):
    def __init__(self):
        self.price = {
            "NAN": "N/A",
            "whiskey": 35.00,
            "rum": 40.00,
            "red wine": 50.00,
            "white wine": 55.00,
        }
        self.stock = {
            "NAN": 0,
            "whiskey": 20,
            "rum": 40,
            "red wine": 25,
            "white wine": 30
        }
        super().__init__()

def Barcode():
    x = ran.randint(100, 100)
    barcode = ""
    while(x > 0):
        barcode = barcode + str(ran.randint(0, 9))
        x -= 1
    return barcode
#__________________________________________________________

class Item():
    def __init__(self, quantity, product, store, choice):
        self.quantity = quantity
        self.product = product
        self.barcode = Barcode()
        self.department = choice
        self.stringDepartment = choice
        self.price = store.Price(product)
    def TotalCost(self):
        total = int(self.quantity) * self.price
        return total
    def Description(self):
        print(f"{self.product} item: Quantity - {self.quantity}, Price - {self.TotalCost()}, Department - {self.department}, Barcode - {self.barcode}")

class Cart():
    def __init__(self):
        self.cart = []
        self.tax = 0.15
    def InCart(self):
        print("You have: ")
        for x in self.cart:
            x.Description()
        print("in your cart")
        main()
    def AddItemToCart(self, amount, product, store, choice):
        try:
            newItem = Item(amount, product, store, choice)
            self.cart.append(newItem)
            self.InCart()
        except Exception as e:
            print(str(e))
            main()
    def RemoveLastItem(self):
        try:
            if(len(self.cart) == 0):
                raise EmptyCart("Your cart is empty")
            else:
                self.cart.pop()
                self.InCart()
                main()
        except EmptyCart as e:
            print(str(e))
        except Exception as e:
            print(str(e))
    def Checkout(self):
        try:
            if(len(self.cart) == 0):
                raise EmptyCart("Your cart is empty")
            else:
                for x in self.cart:
                    total = (x.TotalCost() * self.tax) + x.TotalCost()
                else:
                    print(f"Your total is {total:0.2f} with tax. Thanks for shopping with us!")
        except EmptyCart as e:
            print(str(e))
            t.sleep(2)
            main()
        except Exception as e:
            print(str(e))
#_____________________________________________
#This is the what shows when the program gets executed, the "user interface" per say
cart = Cart() #this just initializes the cart so the items actually affect the cart property; also so you can access the methods
def main():
    dept = {
        "Frozen": Frozen(),
        "Bakery": Bakery(),
        "Deli": Deli(),
        "Canned": Canned(),
        "Dairy": Dairy(),
        "Fresh": Fresh(),
        "Health": Health(),
        "Alchohol": Alchohol(),
    }
    print("Welcome to my online store, we have many departments to choose from: ")
    for x in dept:
        print(f"  ◦ {x}")
    print("Choose a department to see what items are available or checkout!")
    choice = input()
    if(choice=="Frozen" or choice=="frozen"):
        store = Frozen()
        options(store, cart, choice)
    elif(choice=="Bakery" or choice=="bakery"):
        store = Bakery()
        options(store, cart, choice)
    elif(choice=="Deli" or choice=="deli"):
        store = Deli()
        options(store, cart, choice)
    elif(choice=="Canned" or choice=="canned"):
        store = Canned()
        options(store, cart, choice)
    elif(choice=="Dairy" or choice=="dairy"):
        store = Dairy()
        options(store, cart, choice)
    elif(choice=="Fresh" or choice=="fresh"):
        store = Fresh()
        options(store, cart, choice)
    elif(choice=="Health" or choice=="health"):
        store = Health()
        options(store, cart, choice)
    elif(choice=="Alchohol" or choice=="alchohol"):
        store = Alchohol()
        options(store, cart, choice)
    elif(choice=="Checkout" or choice=="checkout"):
        print("""What do you want to do with your cart?
    1. Remove
    2. View
    3. Checkout""")
        checkoutOption = input()
        if(checkoutOption == "remove" or checkoutOption == "Remove" or checkoutOption == "1"):
            cart.RemoveLastItem()
        elif(checkoutOption == "view" or checkoutOption == "View" or checkoutOption == "2"):
            cart.InCart()
        elif(checkoutOption == "checkout" or checkoutOption == "Checkout" or checkoutOption == "3"):
            cart.Checkout()
        else:
            print("Invalid option")
            main()
    else:
        print("Invalid option")
        main()
        
def options(store, cart, choice): #options for each department: list, stock, price, buy, and back
    print("""Would you like to: 
    1: list available items
    2: view the stock for an item
    3: view the price of an item
    4: buy an item
    5: go back to department selection""")
    answer = input()
    if(answer == "1"):
        store.List() #this method gets called after store is created
        t.sleep(3.5)
        options(store, cart, choice)
    elif(answer == "2"):
        print("Which item would you like to see the stock of?")
        product = input() #gets the input for item, error handling is handled inside the function
        store.Stock(product) #same for this one
        t.sleep(3.5)
        options(store, cart, choice)
    elif(answer == "3"):
        print("Which item would you like to see the price of?")
        product = input() #also gets the input for which item, errors also handled through the function
        store.Price(product) #and this one
        t.sleep(3.5)
        options(store, cart, choice)
    elif(answer == "4"):
        try:
            print("Which item would you like to buy?")
            option = input()
            print("How many? (max 10)")
            num = input()
            if(num not in ("1", "2", "3", "4", "5", "6", "7", "8", "9", "10")):
                raise InvalidInput("Not a valid input")
            else:
                print(f"{option} added to cart")
        except InvalidInput as e:
            print(str(e))
            options(store, cart, choice)
        except Exception as e:
            print(str(e))
        else:
            cart.AddItemToCart(num, option, store, choice)
    elif(answer == "5"):
        main()
    else:
        try:
            raise InvalidInput("Not a valid input")
        except InvalidInput as e:
            print(str(e))
            main()
        except Exception as e:
            print(str(e))
#_____________________________________________
main()#Lets the program run