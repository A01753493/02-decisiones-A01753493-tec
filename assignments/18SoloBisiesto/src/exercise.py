"""
Convertidor;
escribe el año;
if(año <=0) {
    Dato incorrecto
} else {
    if(año % 4 == 0) {
        if(año % 100 == 0){
            if(año % 400 == 0) {
                True
            } else {
                False
            }
        } else {
            True
        }
    } else {
        False
    }
}
"""

def main():
    #escribe tu código abajo de esta línea
    year_1 = int(input("Año:"))

    if year_1 <= 0:
        print('Dato incorrecto')
    else:
        if year_1 % 4 == 0:
            if year_1 % 100 ==0:
                if year_1 % 400 == 0:
                    print(True)
                else:
                    print(False)
            else:
                print(True)
        else:
            print(False)
            
    


if __name__=='__main__':
    main()
