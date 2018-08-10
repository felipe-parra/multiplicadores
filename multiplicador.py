# -*- coding:utf-8 -*-
import cleaner
billetes = [1000, 500, 200, 100, 50, 20]

cleaner.main()

def decorador():
    print('*' * 80)

def main():
    decorador()
    decorador()
    print('\t\t\tMultiplicador')
    decorador()

    mil = 0
    qui = 0
    dos = 0
    cie = 0
    cin = 0
    vei = 0

    m_mil = 0
    m_qui = 0
    m_dos = 0
    m_cie = 0
    m_cin = 0
    m_vei = 0

    cantidades = [mil,qui,dos,cie,cin,vei]
    multiplicados = [m_mil,m_qui,m_dos,m_cie,m_cin,m_vei]
    
    for i in range(0,6):
        cantidades[i] = input('\nCantidad de Billetes de {}:\t'.format(billetes[i]))
        multiplicados[i] = int(cantidades[i]) * int(billetes[i])

    cleaner.main()
    decorador()
    print('\tBillete\t\tCantidad\tImporte')
    decorador()
    for i in range(0,6):
        print('\t{:,} \tx \t{}\t:\t{:,}'.format(billetes[i], cantidades[i], multiplicados[i]))

    decorador()
    suma = 0
    for i in range(0,6):
        suma += multiplicados[i]

    print('********\tSuma Total:\t$\t{:,}\t\t\t\t********'.format(suma))
    decorador()

if __name__ == '__main__':
    main()
