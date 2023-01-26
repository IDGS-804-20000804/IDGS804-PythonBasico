
num1 = 10
num2 = 0

try:
    res = num1 / num2
    pass
except ZeroDivisionError:
    res = 0
    print("Error en el programa")
finally:
    print( "res: {0}".format(res) )