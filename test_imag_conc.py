import os
import time
from PIL import Image
import concurrent.futures

# Définir la fonction de traitement de chaque image
def process_image(chemin_image):
    # Ouvrir et traiter l'image
    with Image.open(chemin_image) as image:
        # Ici, vous pouvez ajouter votre logique de traitement de l'image
        # Par exemple, redimensionner, appliquer des filtres, etc.
        # Nous ne faisons rien de spécial ici pour l'exemple
        pass
    return chemin_image

if __name__ == "__main__":
    # Définir le répertoire contenant les images
    dossier_images = "Parallel_Programming/Image_reader/images/200k"

    # Obtenez la liste de tous les fichiers d'image dans le dossier
    fichiers_images = [os.path.join(dossier_images, f) for f in os.listdir(dossier_images) if f.lower().endswith((".jpg", ".jpeg"))]

    # Triez les fichiers d'image par ordre alphabétique
    fichiers_images.sort()

    # Nombre de threads à utiliser
    nombre_threads = os.cpu_count()

    start_time = time.time()
    # Créer un pool de threads pour le traitement parallèle des images
    with concurrent.futures.ThreadPoolExecutor(max_workers=nombre_threads) as executor:
        # Lancer le traitement de chaque image dans un thread séparé
        futures = [executor.submit(process_image, chemin_image) for chemin_image in fichiers_images]
        
        # Attendre la fin de tous les threads
        concurrent.futures.wait(futures)
    end_time = time.time()
    exe_time = end_time - start_time
    vitesse = len(fichiers_images) / exe_time
    print(f"Lecture de {len(fichiers_images)} images en parallele avec {nombre_threads} threads.")
    print("Temps de lecture:", exe_time, "secondes")
    print(f"la vitesse de lecture est: {vitesse} images/seconde")
