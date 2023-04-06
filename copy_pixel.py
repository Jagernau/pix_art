import cv2 as cv
import math
import numpy as np
import os
import glob

class GridingPic:
    BASE_DIR = os.path.dirname(os.path.abspath(__file__))
    IN_PICS_DIR = "pics/" # Input directory containing pictures
    OUT_PICS_DIR = "out_pics/" # Output directory for storing processed pictures

    def __init__(self, grid: int, file_name=None) -> None:
        self.file_name = file_name
        self.grid = grid
        self.griding_height = int()
        self.griding_width = int()
        self.picture_numbers = self.griding_height * self.griding_width
        self.converted = self.__convert_img()

    
    def __convert_img(self) -> np.ndarray:
        if self.file_name != None:
            filepath = os.path.join(self.BASE_DIR, self.IN_PICS_DIR + self.file_name)
        if self.file_name == None:
            filepath = os.path.join(self.BASE_DIR,self.IN_PICS_DIR, max(glob.iglob(os.path.join(self.BASE_DIR, self.IN_PICS_DIR, "*")), key=os.path.getctime))
        converted = cv.imread(filepath)
        self.griding_height = math.floor(converted.shape[0] / self.grid)
        self.griding_width = math.floor(converted.shape[1] / self.grid)
        return converted
   

    def __sum_rgb(self, one_square: np.ndarray) -> list[int]:
        blue = 0
        green = 0
        red = 0
        for i in one_square:
            for b in i:
                blue += b[2]
                green += b[1]
                red += b[0]
        return [round(red / (self.grid*self.grid)), round(green / (self.grid*self.grid)), round(blue / (self.grid*self.grid))]
 
            
    def grid_pic_in_little_pics(self) -> np.ndarray:
        ready_grid_array = np.full((self.converted.shape[0], self.converted.shape[1], 3), [0,0,0], dtype=np.uint8)
        for x in range(0,self.converted.shape[0], self.grid):
            for y in range(0,self.converted.shape[1], self.grid):                   
                ready_grid_array[x:x + self.grid, y:y + self.grid] = self.__sum_rgb(self.converted[x:x + self.grid, y:y + self.grid])
        return ready_grid_array

pix_art = GridingPic(50)
cv.imwrite("new4.jpg", pix_art.grid_pic_in_little_pics())
