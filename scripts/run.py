import argparse
import os

import mandybrot as mandy

OUTPUT_DIR = 'output'

parser = argparse.ArgumentParser()
parser.add_argument('real', type=float, default=0.012)
parser.add_argument('imag', type=float, default=-0.65)
parser.add_argument('width', type=int, default=1920)
parser.add_argument('height', type=int, default=1080)
parser.add_argument('scale', type=float, default=1.5e-2)
parser.add_argument('max_iters', type=int, default=1000)
parser.add_argument("cmap", nargs="+", type=str)
args = parser.parse_args()

# Create the output directory if it doesn't exist
if not os.path.exists(OUTPUT_DIR):
    os.makedirs(OUTPUT_DIR)

# Build the colour map
cmap = mandy.colour.build_colour_map(args.cmap, 256)

# Sample the region
data = mandy.sample.area(
    args.real, args.imag, args.width, args.height, args.scale, args.max_iters
)

img = mandy.colour.image(data, args.max_iters, cmap)
mandy.colour.encode(img).save(os.path.join(OUTPUT_DIR, "mandybrot.png"))


# def display(data):
#     """
#     Display the Mandelbrot set.
#     """
#     shape = data.shape
#     buffer = ''
#     for im in reversed(range(shape[0])):
#         for re in range(shape[1]):
#             buffer += f"{data[im, re]:4.0f}     "
#         buffer += '\n'
#     print(buffer)

# display(data)