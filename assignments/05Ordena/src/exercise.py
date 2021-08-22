"""
Edades;
a = Ingresa el primer numero;
b = Ingresa el segundo numero;
c = Ingresa el tercer numero;
if(a<b) {
    if(b<c) {
        a, b, c
    } else {
        if(a<c) {
            a, c, b
        } else {
            c, a, b
        }
    }
} else {
    if(c<b) {
        c, b, a
    } else {
        b, a, c
    }
}
"""

def main():
    # Escribe el código adecuado para completar el programa
    x = int(input("Ingresa el primer número:"))
    y = int(input("Ingresa el segundo número:"))
    z = int(input("Ingresa el tercer número:"))

    if (x<y and x<z):
        print(x)
        if (y<z):
            print(y)
            print(z)
        else:
            print(z)
            print(y)
    else:
        if (y<x and y<z):
            print(y)
            if(x<z):
                print(x)
                print(z)
            else:
                print(z)
                print(x)
        else:
            print(z)
            if (x<y):
                print(x)
                print(y)
            else:
                print(y)
                print(x)
 
if __name__=='__main__':
    main()
