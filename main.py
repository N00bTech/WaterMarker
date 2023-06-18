from PIL import Image
from tkinter import Tk
from tkinter.filedialog import askopenfilenames
import os

def image_collector():
    Tk().withdraw()
    files = askopenfilenames()
    images = []
    for image in files:
        images.append(image)
    return images # List of pictures/picture.

def image_watermarker(in_image_path, watermark_path, out_image_path):
    IMAGE_RESOLUTION = (2080, 2080)
    base_image = Image.open(in_image_path).resize(IMAGE_RESOLUTION, Image.Resampling.LANCZOS)
    watermark_image = Image.open(watermark_path).resize(IMAGE_RESOLUTION, Image.Resampling.LANCZOS)
    canvas = Image.new('RGBA', IMAGE_RESOLUTION, (0, 0, 0, 0))
    canvas.paste(base_image, (0, 0)), canvas.paste(watermark_image, (0, 0), mask = watermark_image)
    canvas_jpg = canvas.convert('RGB')
    canvas_jpg = canvas_jpg.resize(IMAGE_RESOLUTION, Image.Resampling.LANCZOS)
    canvas_jpg.save(out_image_path, 'JPEG', optimize = True)

    
if __name__ == "__main__":
    images = image_collector()
    directory_path = os.path.dirname(os.path.realpath(__file__))
    watermark_image = f"{directory_path}\\watermark.png" # This only works in Windows
    for image in images:
        image_format_strip = image.strip(".jpg")
        image_watermarker(image, watermark_image, f"{image_format_strip}_WaterMarked.jpg")
        print(f"{image} WaterMarked!")
        os.remove(image)

# USE SCALE FACTOR NEXT TIME
# FOR CALCULATING SIZE OF IMAGE:
# new_image_zie = (image.size[0], * scale_factor, image.size[1] * scale_factor)