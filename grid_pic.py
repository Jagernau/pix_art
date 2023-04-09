import cv2 as cv
import numpy as np
import os
import glob


base_dir = os.path.dirname(os.path.abspath(__file__))
input_dir = "in_pic/" # The directory where the input images are stored.
output_dir = "out_pic/" # The directory where the output images will be saved.

in_dir = os.path.join(base_dir, input_dir)
out_dir = os.path.join(base_dir, output_dir)


def check_directories(in_dir, out_dir):
    """
    Checks the existence of directories 'in_pic' and 'out_pic'.
    If the directories do not exist, creates them.
    """
    try:
        if not os.path.isdir(in_dir):
            os.makedirs(in_dir)
            print(f'Directory "{in_dir}" was successfully created.')

        if not os.path.isdir(out_dir):
            os.makedirs(out_dir)
            print(f'Directory "{out_dir}" was successfully created.')
    
    except Exception:
        print("Directories cannot be created.")

def check_in_dir_empty(in_dir):
    """
    Raises a SystemExit if the specified input directory is empty.
    """
    if len(os.listdir(in_dir)) == 0:
        raise FileNotFoundError(f"Directory {in_dir} is empty")
    else:
        pass


class GridImage:
    """
    A class for splitting an image into smaller square pieces and calculating their average color.
    """

    def __init__(self, grid_size: int, in_dir_pic: str, out_dir_pic: str, file_name: str = None) -> None:
        """
        Initializes the GridingPic class.

        Args:
            grid_size (int): The size of the grid squares in pixels.
            in_dir_pic (str): The directory containing the input image.
            out_dir_pic (str): The directory where the output images will be saved.
            file_name (str, optional): The name of the file to convert. Defaults to None.
        """

        self.in_dir_pic = in_dir_pic
        self.out_dir_pic = out_dir_pic
        self.grid_size = grid_size
        self.file_name = file_name
        self.converted = self.__convert_image()

    def get_last_file(self, directory: str) -> str:
        """
        Returns the most recently created file in the specified directory.

        Args:
            directory (str): The directory to search.

        Returns:
            str: The name of the most recently created file.
        """
        last_file = max(glob.iglob(os.path.join(directory, "*")), key=os.path.getctime)
        return last_file


    def __convert_image(self) -> np.ndarray:
        """
        Converts the specified image file to a NumPy array.

        Returns:
            np.ndarray: The image as a NumPy array.
        """
        try:
            if self.file_name is not None:
                filepath = os.path.join(self.in_dir_pic, self.file_name)
            else:
                latest_file = self.get_last_file(self.in_dir_pic)
                filepath = os.path.join(self.in_dir_pic, latest_file)
            return cv.imread(filepath)
        except Exception:
            print("File is not convertible")


    def __sum_rgb(self, one_square: np.ndarray) -> list[int]:
        """
        Calculates the average RGB values of a single grid square.

        Args:
            one_square (np.ndarray): A single grid square.

        Returns:
            list[int]: The average RGB values of the grid square as a list.
        """
        blue = 0
        green = 0
        red = 0
        for row in one_square:
            for pixel in row:
                blue += pixel[2]
                green += pixel[1]
                red += pixel[0]
        return [round(red / (self.grid_size * self.grid_size)),
                round(green / (self.grid_size * self.grid_size)),
                round(blue / (self.grid_size * self.grid_size))]


    def grid_image_in_little_images(self) -> np.ndarray:
        """
        Divides an image into smaller squares and calculates the average color of each square.
        Saves the resulting grid of colors as a NumPy array.
        
        Args:
            None
        
        Returns:
            np.ndarray: A NumPy array containing the grid of color averages.
        """
        ready_grid_array = np.full((self.converted.shape[0], self.converted.shape[1], 3), [0, 0, 0], dtype=np.uint8)
        for x in range(0, self.converted.shape[0], self.grid_size):
            for y in range(0, self.converted.shape[1], self.grid_size):
                ready_grid_array[x:x + self.grid_size, y:y + self.grid_size] = self.__sum_rgb(self.converted[x:x + self.grid_size, y:y + self.grid_size])
        return ready_grid_array

    
    def get_color_of_square(self, x: int, y: int) -> list[int]:
        """
        Calculates the average RGB values of a specified grid square.

        Args:
            x (int): The x-coordinate of the top-left corner of the square.
            y (int): The y-coordinate of the top-left corner of the square.

        Returns:
            list[int]: The average RGB values of the specified square as a list.
        """
        one_square = self.converted[x:x + self.grid_size, y:y + self.grid_size]
        return self.__sum_rgb(one_square)


    def save_grided_image(self, file_name = None) -> None:
        """
        Saves the gridded image to a file.

        Args:
            file_name (str): The name of the file to save the gridded image to.
        """
        try:
            if file_name is not None:
                filepath = os.path.join(self.out_dir_pic, file_name)
            else:
                latest_file = self.get_last_file(self.in_dir_pic).split("/")[-1]
                filepath = os.path.join(self.out_dir_pic, latest_file)

            cv.imwrite(filepath, self.grid_image_in_little_images())
        except Exception:
            print("There is nothing to save, or the file cannot be saved to this directory")


# Usage example 
try:
    check_directories(in_dir=in_dir, out_dir=out_dir)
    check_in_dir_empty(in_dir=in_dir)
except Exception as e:
    print(f"{e}")
else:
    pix_art = GridImage(10, in_dir_pic=in_dir, out_dir_pic=out_dir)
    pix_art.save_grided_image()

