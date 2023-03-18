import cv2 as cv

import math

import numpy as np



converted = cv.imread('pics/1999 Aphrodite (front).jpg')

print(f"Высота картинки: {converted.shape[0]}\nШирина картинки: {converted.shape[1]}")
grid = int(input("Разбить "))

def info_picture(converted, grid):
    """
    Разбиает картинку на квадраты.
    Размер квадрата - переменная = grid.
    Принимает прочитанную картинку
    cv = converted.
    """
    
    height_in_cells = converted.shape[0] / grid
    width_in_cells = converted.shape[1] / grid
    pictures_numbers = height_in_cells * width_in_cells
    
    h = math.floor(height_in_cells)
    w = math.floor(width_in_cells)
    p = math.floor(pictures_numbers)

    dict_pic = {}
        
    x = 0    
    for i in range(h):
        
        if i == 0:
            x += 0
        else:
            x += grid

        y = 0     
        for f in range(w):
            if f == 0:
                y += 0
            else:
                y += grid
            dict_pic[i,f] = converted[x:x + grid, y:y + grid]
            
    return dict_pic

small_pics = info_picture(converted, grid)
print(len(small_pics))

    
def sum_rgb(first, grid):
    """
    Сумма RGB одного квадрата
    """
    
    colors = []    
    for x in range(grid):
        for y in range(grid):
            colors.append(first[x][y])

    blue_sum = 0
    green_sum = 0
    red_sum = 0
    for c in range(grid*grid):
        blue_sum += colors[c][2]
        green_sum += colors[c][1]
        red_sum += colors[c][0]
    rgb = [round(red_sum / (grid*grid)), round(green_sum / (grid*grid)), round(blue_sum / (grid*grid))]
    return rgb


copy_small = small_pics


for f in small_pics.keys():

    first = small_pics[f]
    
    copy_small[f] = sum_rgb(first, grid)
#cv2_imshow(converted)

list_color = copy_small
for col in copy_small.keys():
    b = copy_small[col]
    a = np.full((grid,grid,3),b, dtype=np.uint8)
    list_color[col] = a


big_pic = np.full((converted.shape[0], converted.shape[1], 3), [0,0,0], dtype=np.uint8)

def great_pic_color(big_pic,converted,grid,list_color):
    """
    Функция которая рисует маленькие
    квадраты в большом big_pic
    """
    great = big_pic
    height_in_cells = converted.shape[0] / grid
    width_in_cells = converted.shape[1] / grid
    pictures_numbers = height_in_cells * width_in_cells
    
    h = math.floor(height_in_cells)
    w = math.floor(width_in_cells)
    p = math.floor(pictures_numbers)
   
    x = 0
    for i in range(h):
        if i == 0:
            x += 0
        else:
            x += grid
        
        y = 0
        for f in range(w):
            if f == 0:
                y += 0
            else:
                y += grid
   
            great[x:x+grid,y:y+grid] = list_color[i,f]
                        
    return great

#cv.imwrite("new.png", great_pic_color(big_pic,converted,grid,list_color))

#print(f"Квадратов в высоту  {round(converted.shape[0]/grid)}\nВ длину {round(converted.shape[1]/grid)}")

#he = int(input("По x "))
#wi = int(input("По y "))

#cv2_imshow(info_picture(converted, grid)[he,wi])
#cv2_imshow(list_color[he,wi])
#print(list_color[he,wi][0][0])
