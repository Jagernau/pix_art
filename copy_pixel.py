
import cv2 as cv
import math
import numpy as np


class Griding:
    def __init__(self, name: str, grid: int) -> None:
        self.name = name
        self.grid = grid
        self.griding_height = int()
        self.griding_width = int()
        self.picture_numbers = self.griding_height * self.griding_width
        self.converted = self.__convert_img()
        self.splited_pic = self.__split_pic_in_little_pics()

    
    def __convert_img(self):
        converted = cv.imread(f"pics/{self.name}")
        self.griding_height = math.floor(converted.shape[0] / self.grid)
        self.griding_width = math.floor(converted.shape[1] / self.grid)
        return converted


    def __split_pic_in_little_pics(self):
        new_len = []
        for x in range(0,self.converted.shape[0], self.grid):
            for y in range(0,self.converted.shape[1], self.grid):                   
                new_len.append(self.converted[x:x + self.grid, y:y + self.grid])
        return new_len


class CreatePic:
    def __init__(self, cls: Griding):
        self.cls = cls
        self.created_pic_array = self.__generate_pic_array()

    def __generate_pic_array(self):
        return np.full((self.cls.converted.shape[0], self.cls.converted.shape[1], 3), [0,0,0], dtype=np.uint8)
    def get_created_pic_array(self):
        return self.created_pic_array


try:
    pix_art = Griding('1999 Aphrodite (front).jpg', 10)
except BaseException:
    print("Нет такого файла")
else:
    creat = CreatePic(pix_art)
    cv.imwrite("new2.png", creat.get_created_pic_array())
