#!usr/bin/env python2.7
#coding: utf-8

from PIL import Image
import argparse

import os.path

ascii_char = list("$@B%8&WM#*oahkbdpqwmZO0QLCJUYXzcvunxrjft/\|()1{}[]?-_+~<>i!lI;:,\"^`'. ")

def get_char(r,g,b,alpha = 256):
    if alpha == 0:
        return ' '
    length = len(ascii_char)
    gray = int(0.2126 * r + 0.7152 * g + 0.0722 * b)

    unit = (256.0 + 1)/length
    return ascii_char[int(gray/unit)]



#source_img = 'lab_2.png'
source_img = 'lab_1.jpg'
WIDTH = 360
HEIGHT = 400



if __name__ == '__main__':

    img = Image.open(source_img)
    img = img.resize((WIDTH,HEIGHT), Image.NEAREST)
    
    txt = "" 
        
    for i in range(HEIGHT):
        for j in range(WIDTH):
            txt += get_char(*img.getpixel((j,i)))
        txt += '\n'

    print txt

out_jpg = open('out.txt', 'wb')
out_jpg.write(txt)