import os
import random
from PIL import Image

# Funktion zum Laden aller Bilder aus den Unterordnern
def load_images_from_subfolders(base_dir, img_size=(200, 200)):
    images = []
    for folder in os.listdir(base_dir):
        folder_path = os.path.join(base_dir, folder)
        if os.path.isdir(folder_path):
            for img_file in os.listdir(folder_path):
                img_path = os.path.join(folder_path, img_file)
                img = Image.open(img_path).resize(img_size)  # Größe anpassen
                images.append(img)
    return images

# Funktion zum Erstellen eines großen Bildes aus zufällig angeordneten Bildern
def create_collage(images, grid_size, img_size=(200, 200)):
    # Berechne die Größe des großen Bildes
    collage_width = grid_size[0] * img_size[0]
    collage_height = grid_size[1] * img_size[1]
    
    # Erstelle ein neues leeres Bild (weiß)
    collage_img = Image.new('RGB', (collage_width, collage_height), (255, 255, 255))
    
    # Zufällig mischen
    random.shuffle(images)
    
    # Füge die Bilder im Raster hinzu
    idx = 0
    for y in range(grid_size[1]):
        for x in range(grid_size[0]):
            if idx < len(images):
                collage_img.paste(images[idx], (x * img_size[0], y * img_size[1]))
                idx += 1
    
    return collage_img

# Hauptprogramm
base_dir = 'shapes_dataset'  # Pfad zum Ordner mit den Bildern
img_size = (200, 200)  # Größe der einzelnen Bilder
grid_size = (10, 20)  # Grid-Größe (z.B. 10x20 für 200 Bilder)

# Lade alle Bilder
images = load_images_from_subfolders(base_dir, img_size)

# Erstelle das große Bild
collage_img = create_collage(images, grid_size, img_size)

# Speichere das große Bild
collage_img.save('collage.png')

print("Collage wurde erfolgreich erstellt und gespeichert!")
