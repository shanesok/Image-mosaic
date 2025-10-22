import numpy as np
from PIL import Image
import os


best_img = []

def main():
    n=10
    path_input_image = "C:/Users/asdfa/OneDrive/Documents/GitHub/Image-mosaic/Pikachu.jpg"
    path_database = "C:/Users/asdfa/OneDrive/Documents/GitHub/Image-mosaic/bart_simpson"
    path_output = "C:/Users/asdfa/OneDrive/Documents/GitHub/Image-mosaic/output.png"
    I = load_image(path_input_image)
    width, height = I.size
    output = create_empty_image(width, height, n)
    rankl_list = process_database(path_database)
    kernel_avg = process_kernel(I, n, width, height)
    best_db_img = compare_kernel2ranklist(rankl_list, kernel_avg)
    write_best_to_output(best_db_img, output, n, width, height)
    save_image(output, path_output)

def write_best_to_output(best_db_img, output, n, width, height):
    index = 0
    for i in range(width // n):
        for j in range(height // n):
            left = i * 28
            upper = j * 28
            box = (left, upper)
            db_img = load_image(best_img[index])
            db_img_resized = db_img.resize((28, 28))
            output.paste(db_img_resized, box)
            index += 1

def create_empty_image(width, height, n):
    ouput = Image.new("RGB", (width//n*28, height//n*28), color=(255, 255, 255))
    return ouput

def compare_kernel2ranklist(rankl_list, kernel_avg):
    counter = 0
    for i in range(len(kernel_avg)):
        R1, G1, B1 = kernel_avg[i][1][0] - rankl_list[0][1][0], kernel_avg[i][1][1] - rankl_list[0][1][1], kernel_avg[i][1][2] - rankl_list[0][1][2]
        smallest_diff = R1+G1+B1
        best_img_val = rankl_list[0][0]
        for j in range(1,len(rankl_list)):
            R2, G2, B2 = kernel_avg[i][1][0] - rankl_list[j][1][0], kernel_avg[i][1][1] - rankl_list[j][1][1], kernel_avg[i][1][2] - rankl_list[j][1][2]
            current_diff = R2+G2+B2
            if current_diff < smallest_diff:
                counter += 1
                smallest_diff = current_diff
                best_img_val = rankl_list[j][0]
        best_img.append(best_img_val)
    print(counter)
    return best_img

def process_kernel(I, n, width, height):
    kernel = []
    width_kernel = width // n
    height_kernel = height // n
    for i in range(width_kernel):
        for j in range(height_kernel):
            left = i * n
            upper = j * n
            right = left + n
            lower = upper + n
            box = (left, upper, right, lower)
            kernel_img = I.crop(box)
            # compute average color
            pixels = list(kernel_img.getdata())
            r = sum(p[0] for p in pixels) // len(pixels)
            g = sum(p[1] for p in pixels) // len(pixels)
            b = sum(p[2] for p in pixels) // len(pixels)
            kernel.append((kernel_img, [r, g, b]))
    return kernel


def process_database(path_database):
    database = []
    for filename in os.listdir(path_database):
        if filename.lower().endswith(('.jpg', '.jpeg', '.png')):
            img_path = os.path.join(path_database, filename)
            db_img = load_image(img_path)
            # compute average color
            pixels = list(db_img.getdata())
            r = sum(p[0] for p in pixels) // len(pixels)
            g = sum(p[1] for p in pixels) // len(pixels)
            b = sum(p[2] for p in pixels) // len(pixels)
            database.append((img_path, (r, g, b)))
    return database

def load_image(path_input_image):
    I = Image.open(path_input_image)
    return I

def save_image(output, path_output):
    output.save(path_output, format="JPEG")

if __name__ == "__main__":
    main()
for i in range(len(best_img)-1):
    a = 0
    if best_img[i] != best_img[i+1] and a < 3:
        print(best_img[i], best_img[i+1])
        a += 1