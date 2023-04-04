import pandas as pd
import cv2 as cv
import math
import numpy as np
import sys


class Griding:
    def __init__(self, name: str, grid: int) -> None:
        self.name = name
        self.grid = grid
        self.griding_height = int()
        self.griding_width = int()
        self.picture_numbers = self.griding_height * self.griding_width
        self.converted = self.__convert_img()
        self.splited_pic = self.split_pic_in_little_pics()

    
    def __convert_img(self):
        converted = cv.imread(f"pics/{self.name}")
        self.griding_height = math.floor(converted.shape[0] / self.grid)
        self.griding_width = math.floor(converted.shape[1] / self.grid)
        return converted
    
    def rgb(self, long_list):
        blue = 0
        green = 0
        red = 0
        for i in long_list:
            for b in i:
                blue += b[2]
                green += b[1]
                red += b[0]
        return [round(red / (self.grid*self.grid)), round(green / (self.grid*self.grid)), round(blue / (self.grid*self.grid))]
 
            
    def split_pic_in_little_pics(self):
        new_len = np.full((self.converted.shape[0], self.converted.shape[1], 3), [0,0,0], dtype=np.uint8)
        for x in range(0,self.converted.shape[0], self.grid):
            for y in range(0,self.converted.shape[1], self.grid):                   
                new_len[x:x + self.grid, y:y + self.grid] = self.rgb(self.converted[x:x + self.grid, y:y + self.grid])
        return new_len




pix_art = Griding('1999 Aphrodite (front).jpg', 20)
cv.imwrite("new4.jpg", pix_art.split_pic_in_little_pics())
#    print(len(pix_art.split_pic_in_little_pics()))
