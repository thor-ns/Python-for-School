#The temp converters as a function
def convert_to_celsius(F):
    C = (F-32) * 5 / 9
    print(C)

def convert_to_fahrenheit(Cel):
    Fah = (float(Cel) * 9 / 5) + 32
    print(Fah)