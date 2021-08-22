"""
Edades;
ingresa tu peso;
ingresa tu altura;
if(peso y altura >1) {
    imc= peso/altura**2;
    if(imc < 20) {
        Peso bajo
    } else {
        if(imc >= 20 y < 25) {
            Normal
        } else {
            if(imc >=25 y < 30) {
                Sobrepeso
            } else {
                if(imc >= 30 y < 40){
                    Obesidad
                } else {
                  Obesidad morbida
                }
            }
        }
    }
} else{
    Revisa tus datos, alguno de ellos es erróneo
}
"""

def main():
    #escribe tu código abajo de esta línea
    peso = float(input("Peso en kg:"))
    altura = float(input("Altura en m:"))

    imc = peso / (altura**2)

    if (altura<=0 or peso<=0):
        print("Revisa tus datos, alguno de ellos es erróneo.")
    else:
        if(altura != 0 and peso != 0):
            if(imc<20):
                print("Peso bajo")
            else:
                if(20<=imc<25):
                    print("Normal")
                else:
                    if (25<=imc<30):
                        print("Sobrepeso")
                    else:
                        if (30<=imc<40):
                            print("Obesidad")
                        else:
                            print("Obesidad morbida")
        else:
            print("Revisa tus datos, alguno de ellos es erróneo.")
            

if __name__=='__main__':
    main()