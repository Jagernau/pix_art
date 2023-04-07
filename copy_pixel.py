import cv2 as cv
import numpy as np
import os
import glob


in_dir = "in_pic/"
out_dir = "out_pic/"


def check_directories(in_dir, out_dir):
    """
    Проверяет наличие директорий "in_pic" и "out_pic"
    Если директории отсутствуют, создает их
    """
    if not os.path.isdir(in_dir):
        os.makedirs(in_dir)  # Создаем директорию "in_pic"
        print(f'Директория "{in_dir}" успешно создана')
    
    if not os.path.isdir(out_dir):
        os.makedirs(out_dir)  # Создаем директорию "out_pic"
        print(f'Директория "{out_dir}" успешно создана')
    
    print('Проверка директорий завершена')


class GridingPic:
    """
    A class for splitting an image into smaller square pieces and calculating their average color.
    """

    base_dir = os.path.dirname(os.path.abspath(__file__))

    def __init__(self, grid_size: int, file_name: str = None, in_dir_pic: str = "in_pic/", out_dir_pic: str = "out_pic/") -> None:
        """
        Initializes an instance of the GridingPic class.

        Args:
            grid_size (int): The size of the grid in pixels.
            file_name (str): The path to the image file to be processed. If not specified, the latest image in the "pics" directory will be used.
        """
        self.in_dir_pic = in_dir_pic
        self.out_dir_pic = out_dir_pic
        self.grid_size = grid_size
        self.file_name = file_name
        self.converted = self.__convert_image()

    def get_last_file(self, directory: str) ->str:
            last_file = max(glob.iglob(os.path.join(self.base_dir, directory, "*")), key=os.path.getctime)
            return last_file


    def __convert_image(self) -> np.ndarray:
        """
        Converts the specified image file to a NumPy array.

        Returns:
            np.ndarray: The image as a NumPy array.
        """
        if self.file_name is not None:
            filepath = os.path.join(self.base_dir, self.in_dir_pic, self.file_name)
        else:
            latest_file = self.get_last_file(self.in_dir_pic)
            filepath = os.path.join(self.base_dir, self.in_dir_pic, latest_file)

        return cv.imread(filepath)


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


    def grid_pic_in_little_pics(self) -> np.ndarray:
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


    def save_grided_pic(self, file_name = None) -> None:
        """
        Saves the gridded image to a file.

        Args:
            file_name (str): The name of the file to save the gridded image to.
        """
        if file_name is not None:
            filepath = os.path.join(self.base_dir, self.out_dir_pic, file_name)
        else:
            latest_file = self.get_last_file(self.in_dir_pic).split("/")[-1]
            filepath = os.path.join(self.base_dir, self.out_dir_pic, latest_file)

        cv.imwrite(filepath, self.grid_pic_in_little_pics())


pix_art = GridingPic(10)
pix_art.save_grided_pic()
