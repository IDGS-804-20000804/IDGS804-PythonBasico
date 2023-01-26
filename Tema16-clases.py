
# class OperacionesBasicas(herencia):
class OperacionesBasicas():
    # Propiedades
    num1 = 0
    num2 = 0
    res = 0
    
    # Constructor
    def __init__(self, a, b):
        self.num1 = a
        self.num2 = b
    
    # Metodos
    def suma(self):
        self.res = self.num1 + self.num2

    def resta(self):
        return (self.res = self.num1 - self.num2)


def main():
    obj = OperacionesBasicas(3,4)
    obj.suma()
    print("La suma es {0} ".format(obj.res))
    obj.resta()
    print("La resta es {0} ".format(obj.res))


if __name__ == "__main__":
    main()