import os
from functions import check_directories, check_in_dir_empty
from class_grid_image import GridImage
import click

base_dir = os.path.dirname(os.path.abspath(__file__))
input_dir = "in_pic/" # The directory where the input images are stored.
output_dir = "out_pic/" # The directory where the output images will be saved.

in_directory = os.path.join(base_dir, input_dir)
out_directory = os.path.join(base_dir, output_dir)



# Usage example
@click.command()
@click.option("-g", "--grid_size", "grid_size", type=int, help="size of crushing squares image")
@click.option("-f", "--file_name", "file_name", default=None, type=str, help="the name of the file to be converted")
@click.option("-i", "--input_dir", "input_pic_dir", default=in_directory, type=str, help='the directory from which images will be converted is located in the root folder by default "in_pic/"')
@click.option("-o", "--output_dir", "output_pic_dir", default=out_directory, type=str, help='the directory from which images will be converted is located in the root folder by default "out_pic/"')
def main(grid_size, file_name, input_pic_dir, output_pic_dir):
    try:
        check_directories(in_dir=input_pic_dir, out_dir=output_pic_dir)
        check_in_dir_empty(in_dir=input_pic_dir)
    except Exception as e:
        print(f"{e}")
    else:
        pix_art = GridImage(grid_size=grid_size, in_dir_pic=input_pic_dir, out_dir_pic=output_pic_dir, file_name=file_name)
        pix_art.save_grided_image()

if __name__ == "__main__":
    main()
