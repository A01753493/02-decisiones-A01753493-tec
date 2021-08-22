"""
ingresa tu edad;
if(>18) {
    if(¿Tienes identificación oficial?s/n) {
        Trámite de licencia concedido
    } else {
        No cumples requisitos
    }
}
"""

def main():
    edad = int(input("Ingresa tu edad:"))

    if  (edad<=0):
        print("Respuesta incorrecta")
    else:
        if (edad>=18):
            ine = input ("Tienes identificación oficial?(s/n):")
            if (ine == "s"):
                print("Trámite de licencia concedido")
            else:
                if (ine == "n"):
                    print("No cumples requisitos")
                else:
                    print("Respuesta incorrecta")
        else:
            print("No cumples requisitos")
   
if __name__ == '__main__':
    main()
