import os
import time
from PIL import Image

start_time = time.time()
# Définissez le répertoire contenant les images
dossier_images = "Parallel_Programming/Image_reader/images/7k"

# Obtenez la liste de tous les fichiers d'image dans le dossier
fichiers_images = [f for f in os.listdir(dossier_images) if f.lower().endswith((".jpg", ".jpeg"))]

# Triez les fichiers d'image par ordre alphabétique
fichiers_images.sort()
start_time2 = time.time()
# Lisez et traitez chaque image séquentiellement
for fichier_image in fichiers_images:
    chemin_image = os.path.join(dossier_images, fichier_image)
    image = Image.open(chemin_image)
    # Traitez l'image (par exemple, affichez sa taille)
    #print(f"Lecture de l'image : {fichier_image}, taille : {image.size}")
end_time2 = time.time()
end_time = time.time()
exe_time = end_time - start_time
exe_time2 = end_time2 - start_time2
vitesse = len(fichiers_images) / exe_time2
# Affichez un message de réussite
print(f"Lettura di {len(fichiers_images)} immagini sequenzialmente.")
print("Tempo di execuzione della funzione: ", exe_time2, "secondi")
print("Tempo di execuzione del programma: ", exe_time, "secondi")
print(f"Velocita' di lettura delle immagini: {vitesse} immagini/secondo")
del chemin_image
del image
del fichiers_images