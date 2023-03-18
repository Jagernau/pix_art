
from typing import Tuple
import cv2 as cv
import math
import os


class Convert:
    def __init__(self):
        self.__name = str
        self.__convert = None
        self.__height = int
        self.__width = int

    def get_name(self):
        return self.__name


    def convert_name(self, name: str) -> None:
        if os.path.exists(f"pics/{name}"):
            self.__name = name
            convert = cv.imread(f"pics/{name}")
            self.__convert = convert
            self.__height = convert.shape[0]
            self.__width = convert.shape[1]
            
        else:
            raise SystemError(1)
    
    def get_converted(self):
        return self.__convert


    def get_size(self) -> Tuple[int,int]:
        return self.__height, self.__width



class Griding:
    def __init__(self, cls: Convert, grid: int) -> None:
        self.grid = grid
        self.__griding_height = math.floor(cls.get_size()[0] / grid)
        self.__griding_width = math.floor(cls.get_size()[1] / grid)
        self.picture_numbers = self.__griding_height * self.__griding_width
        self.__converted = cls.get_converted()



    def split_pic_in_little_pics(self):
        alin = []
        x = 0
        for i in range(self.__griding_height):
            if i == 0:
                x += 0
            else:
                x += self.grid

            y = 0
            for z in range(self.__griding_width):
                if z == 0:
                    y += 0
                else:
                    y += self.grid
                    
                alin.append(self.__converted[x:x + self.grid, y:y + self.grid])
        print(len(alin))
                
        


pic = Convert()
pic.convert_name('1999 Aphrodite (front).jpg')

grid = Griding(pic, 10)
grid.split_pic_in_little_pics()



