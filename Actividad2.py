import os

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
        self.res = self.num1 - self.num2

    def multiplicacion(self):
        self.res = self.num1 * self.num2

    def division(self):
        self.res = self.num1 / self.num2

def main():
    opcion = 1
    while (opcion != 0):
        print("""
        Menú
        1) Suma
        2) Resta
        3) Multiplicación
        4) División
        5) Salir
        """)

        opcion = int(input("Elige una opción: "))
        os.system('clear')
        if opcion == 1:
            print("Suma")
        elif opcion == 2:
            print("Resta")
        elif opcion == 3:
            print("Multiplicación")
        elif opcion == 4:
            print("División")
        elif opcion == 5:
            print("Bye")
        else:
            print("Ingresa una opción del menú")

        if opcion != 5:
            num1 = float(input("Primer número: ") )
            num2 = float(input("Segundo número: ") )
            obj = OperacionesBasicas(num1, num2)
        
        if opcion == 1:
            obj.suma()
            print("Suma: {0} + {1} = {2} ".format(num1, num2, obj.res))
        elif opcion == 2:
            obj.resta()
            print("Resta: {0} - {1} = {2} ".format(num1, num2, obj.res))
        elif opcion == 3:
            obj.multiplicacion()
            print("Multiplicación: {0} * {1} = {2} ".format(num1, num2, obj.res))
        elif opcion == 4:
            if num2 == 0:
                print("No se puede dividir entre 0")
            else:
                obj.division()
                print("División: {0} / {1} = {2} ".format(num1, num2, obj.res))
        elif opcion == 5:
            os.system('clear')
            opcion = 0
        else:
            print("Ingresa una opción del menú")

        

if __name__ == "__main__":
    main()