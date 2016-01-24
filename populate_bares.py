# -*- encoding: utf-8 -*-

import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'proyectoDAI.settings')

import django
django.setup()

from bares.models import Bares, Tapas

def populate():

    la_pinta = add_bar(nombre="La Pinta",direccion="C/ Socrates, 31")
    ecu = add_bar(nombre="Ecu",direccion="C/ Paseo del Emperador Carlos V, 7")
    los_diamantes = add_bar(nombre="Los Diamantes",direccion="Plaza Nueva, 13")
    castaneda = add_bar(nombre="Bodegas Castañeda",direccion="C/ de Almireceros, 1")

    add_tapa(nombre="Serranito",bar=la_pinta)
    add_tapa(nombre="Queso a la plancha",bar=la_pinta)
    add_tapa(nombre="Hamburguesa",bar=la_pinta)
    add_tapa(nombre="Perrito",bar=la_pinta)

    add_tapa(nombre="Pinchito",bar=ecu)
    add_tapa(nombre="Patatas bravas",bar=ecu)
    add_tapa(nombre="Lomo con roquefort",bar=ecu)
    add_tapa(nombre="Lomo con ali oli",bar=ecu)

    add_tapa(nombre="Pulpo",bar=los_diamantes)
    add_tapa(nombre="Migas",bar=los_diamantes)
    add_tapa(nombre="Salmorejo",bar=los_diamantes)
    add_tapa(nombre="Jamón ibérico",bar=los_diamantes)

    add_tapa(nombre="Jamón",bar=castaneda)
    add_tapa(nombre="Queso",bar=castaneda)
    add_tapa(nombre="Chorizo",bar=castaneda)
    add_tapa(nombre="Morcilla",bar=castaneda)

    # Print out what we have added to the user.
    for b in Bares.objects.all():
        print "+{0}:".format(str(b))
        for t in Tapas.objects.filter(bar=b):
            print "-{0}".format(str(t))
        print "\n"

def add_bar(nombre,direccion,visitas=0):
    b = Bares.objects.get_or_create(nombre_bar=nombre, direccion=direccion)[0]
    b.visitas=visitas
    b.save()
    return b

def add_tapa(nombre,bar,votos=0):
    t = Tapas.objects.get_or_create(nombre_tapa=nombre,bar = bar)[0]
    t.votos=votos
    t.save()
    return t

# Start execution here!
if __name__ == '__main__':
    print "Incluyendo bares y tapas...\n"
    populate()
