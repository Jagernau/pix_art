import os
from functions import check_directories, check_in_dir_empty
from class_grid_image import GridImage

base_dir = os.path.dirname(os.path.abspath(__file__))
input_dir = "in_pic/" # The directory where the input images are stored.
output_dir = "out_pic/" # The directory where the output images will be saved.

in_dir = os.path.join(base_dir, input_dir)
out_dir = os.path.join(base_dir, output_dir)


# Usage example 
try:
    check_directories(in_dir=in_dir, out_dir=out_dir)
    check_in_dir_empty(in_dir=in_dir)
except Exception as e:
    print(f"{e}")
else:
    pix_art = GridImage(10, in_dir_pic=in_dir, out_dir_pic=out_dir)
    pix_art.save_grided_image()

