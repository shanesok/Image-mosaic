# Image-mosaic
Turn any image into a mosaic made of smaller pictures — built with Python and Pillow (PIL).
##  Features
- Converts any image into a photo mosaic
- Uses average color matching to pick the best tiles
- Adjustable grid size (n x n)
- Works with any image folder as a database
## 🧩 Installation

1. Clone the repo:
   ```bash
   git clone https://github.com/username/image-mosaic.git
   cd image-mosaic
2. Install dependencies:
   ```bash
   pip install numpy
   pip install --upgrade Pillow
   pip install os
   pip install argparse
3. Run the program:
   ```bash
   python Basic_mosaic.py -i Pikachu.jpg -n 20 -o output.png

## 📸 Example
| Original | Mosaic Output |
|-----------|---------------|
| ![original](/Pikachu.jpg) | ![mosaic](output.png) |
## 🧠 How It Works
1. The program splits the input image into small kernels.
2. It calculates the average RGB color of each kernel.
3. It compares each kernel color to the average colors of all database images.
4. The best match replaces that region in the final mosaic.

## 🧠 What I Learned
- How to use NumPy arrays for image processing
- Basics of command-line interfaces with argparse
- Efficient looping and color averaging
