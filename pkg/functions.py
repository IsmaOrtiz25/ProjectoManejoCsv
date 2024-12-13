"""Funciones propias"""
def validar_opcion():
    """Verifica que la opcion ingresada para el menu de opciones sea valida"""
    opcion = int(input('Selecciona la opcion: '))
    while opcion < 0 or opcion > 8:
        print('Opcion incorrecta.')
        opcion = int(input('Selecciona la opcion: '))

    return opcion

def mostrar_lineas(data):
    """Muesta las primeras y ultimas 10 lineas del conjunto de diccionario"""
    print('Primeras 10 lineas')
    for row in data[:10]:
        print(row)

    print('Ultimas 10 lineas')
    for row in data[-10:]:
        print(row)

def mostrar_rating(data, rating):
    """Muestra aquellas series que tengan un rating superior o igual
    al pasado por el usuario"""
    print(f'Mostrando series con un rating {rating} o mayor...')
    for row in data:
        if float(row['rating']) >= rating:
            print(row)

    print('Ya se mostraron todas las series.')

def promedio_tipo(data):
    """agrupa la serie por tipo (movie, tv, ova) y calcula el promedio del rating"""
    tipo = [0, 0, 0, 0] #indice: 0 movie, 1 tv, 2 ova, 3 Special
    acum = [0, 0, 0, 0] #indice: 0 movie, 1 tv, 2 ova, 3 Special
    for row in data:
        if row['type'] == 'Movie':
            tipo[0] += float(row['rating'])
            acum[0] += 1
        elif row['type'] == 'TV':
            tipo[1] += float(row['rating'])
            acum[1] += 1
        elif row['type'] == 'OVA':
            tipo[2] += float(row['rating'])
            acum[2] += 1
        else:
            tipo[3] += float(row['rating'])
            acum[3] += 1

    return tipo, acum

def anime_genero(data):
    """Obtiene la cantidad de generos que aparece en un anime"""
    dict_generos = {}
    for row in data:
        generos = row['genre'].split(', ') # Divide la cadena en una lista
        for genre in generos:
            if genre in dict_generos:
                dict_generos[genre] += 1
            else:
                dict_generos[genre] = 1

    return dict_generos


def obtener_prom_tipo(tipo, acum):
    """Muestra el promedio de cantidad de series por tipo"""
    if acum[0] > 0:
        print(f'Rating promedio de peliculas: {round(tipo[0]/acum[0],2)}')
    if acum[1] > 0:
        print(f'Rating promedio de series por TV: {round(tipo[1]/acum[1],2)}')
    if acum[2] > 0:
        print(f'Rating promedio de OVAs: {round(tipo[2]/acum[2],2)}')
    if acum[3] > 0:
        print(f'Rating promedio de Especiales: {round(tipo[3]/acum[3],2)}')

def mostrar_por_id(data, id_serie):
    """Busca el ID de una serie y muestra sus datos"""
    for row in data:
        if row['anime_id'] == id_serie:
            print(row)
            break
