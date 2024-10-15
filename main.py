import os
import math
import random
from PIL import Image, ImageDraw

# Erstelle Ordner für die Kategorien
categories = ['circle', 'square', 'triangle', 'hexagon']
base_dir = 'shapes_dataset'
os.makedirs(base_dir, exist_ok=True)
for category in categories:
    os.makedirs(os.path.join(base_dir, category), exist_ok=True)

# Hilfsfunktionen zur Formenerstellung
def draw_circle(draw, size):
    radius = random.randint(20, min(size) // 2)
    x, y = random.randint(radius, size[0]-radius), random.randint(radius, size[1]-radius)
    draw.ellipse([x-radius, y-radius, x+radius, y+radius], fill=random_color())

def draw_square(draw, size):
    side = random.randint(20, min(size) // 2)
    x, y = random.randint(0, size[0]-side), random.randint(0, size[1]-side)
    draw.rectangle([x, y, x+side, y+side], fill=random_color())

def draw_triangle(draw, size):
    x1, y1 = random.randint(0, size[0]), random.randint(0, size[1])
    x2, y2 = random.randint(0, size[0]), random.randint(0, size[1])
    x3, y3 = random.randint(0, size[0]), random.randint(0, size[1])
    draw.polygon([x1, y1, x2, y2, x3, y3], fill=random_color())

def draw_hexagon(draw, size):
    x, y = random.randint(50, size[0]-50), random.randint(50, size[1]-50)
    r = random.randint(20, min(size) // 3)
    angle = 60
    points = [(x + r * math.cos(math.radians(i * angle)), y + r * math.sin(math.radians(i * angle))) for i in range(6)]
    draw.polygon(points, fill=random_color())

# Zufällige Farbwahl
def random_color():
    return tuple([random.randint(0, 255) for _ in range(3)])

# Funktion zum Bild generieren
def generate_image(shape, img_size=(200, 200)):
    img = Image.new('RGB', img_size, (255, 255, 255))
    draw = ImageDraw.Draw(img)
    
    if shape == 'circle':
        draw_circle(draw, img_size)
    elif shape == 'square':
        draw_square(draw, img_size)
    elif shape == 'triangle':
        draw_triangle(draw, img_size)
    elif shape == 'hexagon':
        draw_hexagon(draw, img_size)

    return img

# Bilder erstellen
num_images_per_category = 50
for category in categories:
    for i in range(num_images_per_category):
        img = generate_image(category)
        img.save(os.path.join(base_dir, category, f'{category}_{i+1}.png'))

print("Bilder wurden erfolgreich erstellt!")
