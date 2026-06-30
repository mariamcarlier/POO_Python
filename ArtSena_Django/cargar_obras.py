# cargar_obras.py
import os
import django

# Configurar Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'ArtSena_Django.settings')
django.setup()

from usuarios.models import ObraArte, Artista

def cargar_obras():
    # Obtener los artistas usando id_usuario (clave primaria)
    leonardo = Artista.objects.get(id_usuario=1)
    monet = Artista.objects.get(id_usuario=2)
    cassatt = Artista.objects.get(id_usuario=3)
    picasso = Artista.objects.get(id_usuario=4)
    dali = Artista.objects.get(id_usuario=5)
    magritte = Artista.objects.get(id_usuario=6)

    # ----- OBRAS DE LEONARDO DA VINCI -----
    ObraArte.objects.create(
        titulo="La Gioconda (Mona Lisa)",
        tecnica="Óleo sobre tabla",
        anio=1503,
        dimensiones="77 x 53 cm",
        precio=850000.00,
        disponibilidad="Disponible",
        artista=leonardo
    )
    ObraArte.objects.create(
        titulo="La Última Cena",
        tecnica="Temple y óleo sobre yeso",
        anio=1498,
        dimensiones="460 x 880 cm",
        precio=1200000.00,
        disponibilidad="Reservada",
        artista=leonardo
    )

    # ----- OBRAS DE CLAUDE MONET -----
    ObraArte.objects.create(
        titulo="Impresión, sol naciente",
        tecnica="Óleo sobre lienzo",
        anio=1872,
        dimensiones="48 x 63 cm",
        precio=350000.00,
        disponibilidad="Disponible",
        artista=monet
    )
    ObraArte.objects.create(
        titulo="Nenúfares",
        tecnica="Óleo sobre lienzo",
        anio=1916,
        dimensiones="200 x 300 cm",
        precio=450000.00,
        disponibilidad="Vendida",
        artista=monet
    )

    # ----- OBRAS DE MARY CASSATT -----
    ObraArte.objects.create(
        titulo="Niña en un sillón azul",
        tecnica="Óleo sobre lienzo",
        anio=1878,
        dimensiones="89.5 x 129.8 cm",
        precio=280000.00,
        disponibilidad="Disponible",
        artista=cassatt
    )
    ObraArte.objects.create(
        titulo="La taza de té",
        tecnica="Óleo sobre lienzo",
        anio=1881,
        dimensiones="64.8 x 81.3 cm",
        precio=310000.00,
        disponibilidad="Reservada",
        artista=cassatt
    )

    # ----- OBRAS DE PABLO PICASSO -----
    ObraArte.objects.create(
        titulo="Guernica",
        tecnica="Óleo sobre lienzo",
        anio=1937,
        dimensiones="349 x 776 cm",
        precio=2000000.00,
        disponibilidad="Disponible",
        artista=picasso
    )
    ObraArte.objects.create(
        titulo="Las señoritas de Avignon",
        tecnica="Óleo sobre lienzo",
        anio=1907,
        dimensiones="244 x 234 cm",
        precio=1500000.00,
        disponibilidad="Vendida",
        artista=picasso
    )

    # ----- OBRAS DE SALVADOR DALÍ -----
    ObraArte.objects.create(
        titulo="La persistencia de la memoria",
        tecnica="Óleo sobre lienzo",
        anio=1931,
        dimensiones="24 x 33 cm",
        precio=750000.00,
        disponibilidad="Disponible",
        artista=dali
    )
    ObraArte.objects.create(
        titulo="El gran masturbador",
        tecnica="Óleo sobre lienzo",
        anio=1929,
        dimensiones="110 x 150 cm",
        precio=620000.00,
        disponibilidad="Reservada",
        artista=dali
    )

    # ----- OBRAS DE RENÉ MAGRITTE -----
    ObraArte.objects.create(
        titulo="La traición de las imágenes (Esto no es una pipa)",
        tecnica="Óleo sobre lienzo",
        anio=1929,
        dimensiones="63.5 x 93.98 cm",
        precio=550000.00,
        disponibilidad="Disponible",
        artista=magritte
    )
    ObraArte.objects.create(
        titulo="El hijo del hombre",
        tecnica="Óleo sobre lienzo",
        anio=1964,
        dimensiones="116 x 89 cm",
        precio=680000.00,
        disponibilidad="Disponible",
        artista=magritte
    )

    print("✅ ¡Todas las obras se han creado con éxito!")

if __name__ == "__main__":
    cargar_obras()