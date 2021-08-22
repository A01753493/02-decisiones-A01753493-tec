"""
Convertidor;
introduce los cm;
km = c, // 100000;
m = cm % 100000 // 100;
rest = cm % 100;
if(km) {
    son km
}
if(m) {
    son m
}
if(cm == 0 o rest) {
    son cm
}
"""

def main():
    # Escribe tu código abajo de esta línea
    int_1= int(input("Introduce los cm:"))

    km_1 = int_1// 100000
    m_1 = int_1 % 100000 // 100
    rest_1 = int_1 % 100

    if km_1:
        print(f'{km_1} km')
    if m_1:
        print(f'{m_1}m')
    if int_1 == 0 or rest_1:
        print(rest_1,'cm')

    
if __name__ == '__main__':
    main()
