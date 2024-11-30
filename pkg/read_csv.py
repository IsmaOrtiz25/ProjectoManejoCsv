"""Lectura del archivo csv"""
import csv

def read_csv(ruta):
    """Realiza la lectura del archivo csv y devuelve la informacion del mismo
    en formato de lsita de diccionarios"""
    data = []
    with open(ruta, 'r', encoding='utf-8') as csvfile:
        reader = csv.reader(csvfile)
        header = next(reader)
        for row in reader:
            iterable = zip(header, row)
            anime_dict = {key: item for key, item in iterable}
            data.append(anime_dict)

    return data

if __name__ == '__main__':
    ruta = './proyecto/anime.csv'
    data = read_csv(ruta)
    print(data)
