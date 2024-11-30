"""Graficas"""
import matplotlib.pyplot as plt

def grafico_tipo(cantidad):
    """Devuelve un grafico de cantidad de animes por tipo"""
    keys = ['Movie', 'TV', 'OVA', 'Special']
    fig, ax = plt.subplots()
    ax.bar(keys, cantidad)
    plt.show()

def grafica_generos(generos):
    """Obtiene la grafica por cantidad de veces que aparece un genero"""
    keys = generos.keys()
    values = generos.values()
    fig, ax = plt.subplots()
    ax.bar(keys, values)
    plt.show()
