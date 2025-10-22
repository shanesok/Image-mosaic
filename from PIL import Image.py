import numpy as np
from PIL import Image
import os

def main():
    n=10
    path_input_image = "C:/Users/asdfa/OneDrive/Documents/GitHub/Image-mosaic/Pikachu.jpg"
    path_database = "C:/Users/asdfa/OneDrive/Documents/GitHub/Image-mosaic/bart_simpson"
    path_output = "C:/Users/asdfa/OneDrive/Documents/GitHub/Image-mosaic/output.png"
    I = load_image(path_input_image)
    width, height = I.size
    output = create_empty_image(width, height, n)
    rankl_list = process_database(path_database)
    kernel_avg = process_kernel()
    best_db_img = compare_kernel2ranklist()
    write_best_to_output()
    save_image(output, path_output)

def write_best_to_output():
    pass

def create_empty_image(width, height, n):
    ouput = Image.new("RGB", (width//n*28, height//n*28), color=(255, 255, 255))
    return ouput

def compare_kernel2ranklist():
    pass

def process_kernel():
    pass
database = []
def process_database(path_database):
    
    for filename in os.listdir(path_database):
        if filename.lower().endswith(('.jpg', '.jpeg', '.png')):
            img_path = os.path.join(path_database, filename)
            db_img = load_image(img_path)

            # compute average color
            pixels = list(db_img.getdata())
            r = sum(p[0] for p in pixels) / len(pixels)
            g = sum(p[1] for p in pixels) / len(pixels)
            b = sum(p[2] for p in pixels) / len(pixels)
            
            database.append((img_path, (r, g, b)))
    return database

def load_image(path_input_image):
    I = Image.open(path_input_image)
    return I

def save_image(output, path_output):
    output.save(path_output, format="JPEG")

if __name__ == "__main__":
    main()
print(database[0])