"""Proyecto data base"""
import pkg
import pkg.charts
import pkg.functions

def menu():
    """Muestra el menu de opciones"""
    print('-' * 50)
    print('Menu de opciones')
    print('1- Cargar archivo.')
    print('2- Mostrar primeras y ultimas lineas.')
    print('3- Mostrar series con mayor rating.')
    print('4- Promedio por tipo')
    print('5- Cantidad de veces por cada genero.')
    print('6- Grafica de cantidad por tipo.')
    print('7- Grafica de cantidad por genero.')
    print('8- Mostrar serie por ID de serie.')
    print('0- Exit')
    print('-' * 50)

def main():
    """Programa principal"""
    carga = False
    opcion = -1
    while opcion != 0:
        menu()
        opcion = pkg.functions.validar_opcion()
        if opcion == 1:
            ruta = './proyecto/anime.csv'
            data = pkg.read_csv.read_csv(ruta)
            carga = True
            print('El archivo se ha cargado con exito.')
        elif opcion == 0:
            print('Saliendo del programa.')
        elif carga:
            if opcion == 2:
                pkg.functions.mostrar_lineas(data)
            elif opcion == 3:
                rating = float(input('Ingrese el rating minimo para mostrar: '))
                pkg.functions.mostrar_rating(data, rating)
            elif opcion == 4:
                tipos, acum = pkg.functions.promedio_tipo(data)
                pkg.functions.obtener_prom_tipo(tipos, acum)
            elif opcion == 5:
                por_generos = pkg.functions.anime_genero(data)
                print('Cantidad de veces que aparecio el genero en algun anime.')
                print(por_generos)
            elif opcion == 6:
                tipos, acum = pkg.functions.promedio_tipo(data)
                pkg.charts.grafico_tipo(acum)
            elif opcion == 7:
                por_generos = pkg.functions.anime_genero(data)
                pkg.charts.grafica_generos(por_generos)
            elif opcion == 8:
                id_serie = input('Ingresa el id de la serie a buscar: ')
                pkg.functions.mostrar_por_id(data, id_serie)
        else:
            print('Primero debes cargar el archivo.')

if __name__ == '__main__':
    main()
