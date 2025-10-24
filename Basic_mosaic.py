import numpy as np
from PIL import Image
import os
import argparse

def main():
    
    path_cwd = os.getcwd()
    parser = argparse.ArgumentParser(description='Basic mosaic generator')
    parser.add_argument('-i', '--input_image_path', type=str, default=os.path.join(path_cwd,"Pikachu.jpg"), help='path to the input image')
    parser.add_argument('-db', '--database_path', type=str, default=os.path.join(path_cwd,"bart_simpson"), help='path to the image database')
    parser.add_argument('-dbs', '--database_image_size', type=int, default=28, help='size of the database images')
    parser.add_argument('-ks', '--kernel_size', type=int, default=20, help='size of the kernel')
    parser.add_argument('-o', '--output_image_path', type=str, default=os.path.join(path_cwd,"output.png"), help='path to the output image')
    args = parser.parse_args()
    
    path_input_image = args.input_image_path
    n = args.kernel_size
    path_database = args.database_path
    path_output = args.output_image_path
    dbs = args.database_image_size
    
    I = load_image(path_input_image)
    width, height = I.size
    output = create_empty_image(width, height, n, dbs)
    rankl_list = process_database(path_database)
    kernel_avg = process_kernel(I, n, width, height)
    best_db_img = compare_kernel2ranklist(rankl_list, kernel_avg)
    write_best_to_output(best_db_img, output, n, width, height, dbs)
    save_image(output, path_output)

def write_best_to_output(best_db_img, output, n, width, height, dbs):
    index = 0
    for i in range(width // n):
        for j in range(height // n):
            left = i * dbs
            upper = j * dbs
            box = (left, upper)
            db_img = load_image(best_db_img[index])
            db_img_resized = db_img.resize((dbs, dbs))
            output.paste(db_img_resized, box)
            index += 1

def create_empty_image(width, height, n, dbs):
    ouput = Image.new("RGB", (width//n*dbs, height//n*dbs), color=(255, 255, 255))
    return ouput

def compare_kernel2ranklist(rankl_list, kernel_avg):
    best_img = []
    for i in range(len(kernel_avg)):
        RGB1 = abs(np.subtract(kernel_avg[i][1], rankl_list[0][1]))
        smallest_diff = sum(RGB1)
        best_img_val = rankl_list[0][0]
        for j in range(1,len(rankl_list)):
            RGB2 = abs(np.subtract(kernel_avg[i][1], rankl_list[j][1]))
            current_diff = sum(RGB2)
            if current_diff < smallest_diff:
                smallest_diff = current_diff
                best_img_val = rankl_list[j][0]
        best_img.append(best_img_val)
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
            pixels = np.array(kernel_img.getdata())
            [r, g, b] = sum(p for p in pixels) // len(pixels)
            kernel.append([kernel_img, [r, g, b]])
    return kernel

def process_database(path_database):
    database = []
    for filename in os.listdir(path_database):
        if filename.lower().endswith(('.jpg', '.jpeg', '.png')):
            img_path = os.path.join(path_database, filename)
            db_img = load_image(img_path)
            # compute average color
            pixels = np.array(db_img.getdata())
            [r, g, b] = sum(p for p in pixels) // len(pixels)
            database.append([img_path, [r, g, b]])
    return database

def load_image(path_input_image):
    I = Image.open(path_input_image)
    return I

def save_image(output, path_output):
    output.save(path_output, format="JPEG")

if __name__ == "__main__":
    main()