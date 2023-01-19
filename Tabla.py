
def multiplicar(a):
    for x in range(0, 10):
        h = x+1
        j = (x+1)*a
        print((" {0} * {1} = {2}"). format(h, a, j))



multiplicar(int(input('Dame el primer número ')))

