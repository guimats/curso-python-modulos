# Pillow: redimensionando imagens com Python
# Essa biblioteca é o Photoshop do Python 😂
# pip install pillow
from PIL import Image
from pathlib import Path

ROOT_FOLDER = Path(__file__).parent
ORIGINAL = ROOT_FOLDER / 'original.JPG'
NEW_IMAGE = ROOT_FOLDER / 'new.JPG'

pil_image = Image.open(ORIGINAL)

# print(pil_image.size)
width, height = pil_image.size
exif = pil_image.info['exif']  # puxa info da imagem original

new_width = 640
# regra de 3 para manter proporção original
new_height = round(height * new_width / width)
print(width, height)
print(new_width, new_height)

new_image = pil_image.resize(size=(new_width, new_height))
new_image.save(
    NEW_IMAGE,
    optimize=True,
    quality=70,
    exif=exif,
)
