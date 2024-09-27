from os import path
import random
import cv2 as cv
from PIL import ImageFont, ImageDraw, Image
import numpy as np
from os import path
def gerarLista() -> list:
    lista = [[],[],[],[],[]]
    for i in range(ncol):
        lista[i] = genRange(steps*i+1,steps*(i+1))
    return lista

def hasDuplicateList(lista: list) -> bool:
    for i in range(len(lista)):
        for j in range(i+1, len(lista)):
            if lista[i] == lista[j]:
                return True
    return False

def genRange(min: int, max: int, size=5) -> list:
    lista = []
    flag = True
    while flag:
        for _ in range(size):
            lista.append(random.randint(min,max))
        
        flag = hasDuplicateList(lista)
        if flag:
            lista = []
    lista.sort()
    return lista

def hasDuplicateTable(allTables: list, table: list) -> bool:
    if allTables.count(table) == 0:
        return False
    return True

def write(draw, j, k, text, font):
    x =42+107*j
    y = 210+116*k
    if text == "100":
        x -= 10
        y += 5
    draw.text((x, y), text, font=font, fill=(0,0,0))

nmin = 1
nmax = 100
steps = 20
ncol = 5
nrow = 5
ammount = 1000

base = cv.imread("bingo-base.png")
imgPath = "cartelas/"

allTables = []

for i in range(ammount):
    img = base
    flag = True
    while flag:
        table = gerarLista()
        if not hasDuplicateTable(allTables, table):
            flag = False
    flag = True
    # print(table)
    allTables.append(table)


    # Convert to PIL Image
    cv2_im_rgb = cv.cvtColor(img, cv.COLOR_BGR2RGB)
    pil_im = Image.fromarray(cv2_im_rgb)

    draw = ImageDraw.Draw(pil_im)

    # Choose a font
    font = ImageFont.truetype("BigBlueTerm437NerdFont-Regular.ttf", 50)
    smallfont = ImageFont.truetype("BigBlueTerm437NerdFont-Regular.ttf", 40)

    # Draw the text         
    for j in range(nrow):
        for k in range(ncol):
            if j == 2 and k == 2:
                continue
            if table[j][k]  < 10:
                write(draw, j,k, f"0{table[j][k]}",font)
            elif table[j][k] == 100:
                write(draw, j,k, f"{table[j][k]}",smallfont)
            else:
                write(draw, j,k, f"{table[j][k]}",font)


    draw.text((130, 765), f"{i+1}", font=smallfont, fill=(0,0,0))
    # Save the image
    cv2_im_processed = cv.cvtColor(np.array(pil_im), cv.COLOR_RGB2BGR)

    cv.imwrite(path.join(imgPath + f'bingo{i+1}.png'),cv2_im_processed)