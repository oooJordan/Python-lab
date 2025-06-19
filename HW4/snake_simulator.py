#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import images


def generate_snake(start_img: str, position: list[int, int], commands: str, out_img: str) -> int:
    coda = 1
    posnake = [position]
    pos_dopo_x,pos_dopo_y = position[0],position[1]
    red = (255,0,0)
    green = ( 0,255,0)
    gray = (128,128,128)
    orange = (255,128,0)
    dir_dic = {'NW':(-1,-1),'N':(0,-1),'NE':(1,-1),'W':(-1,0),'E':(1,0),'SW':(-1,1),'S':(0,1),'SE':(1,1)}
    img = images.load(start_img)
    comm = commands.split()

    def simuove(posnake, img, pos_dopo_x, pos_dopo_y, move_tail):
        img[posnake[-1][1]][posnake[-1][0]] = green
        if move_tail:
            img[posnake[-(coda+1)][1]][posnake[-(coda+1)][0]] = gray
    
    for i in comm:
        dove_va=dir_dic.get(i)
        x = pos_dopo_x
        y = pos_dopo_y
        pos_dopo_x=(x+dove_va[0])%len(img[0])
        pos_dopo_y=(y+dove_va[1])%len(img)
        move_tail = True
        if img[pos_dopo_y][pos_dopo_x]==red or img[pos_dopo_y][pos_dopo_x]==green:
            print(img[pos_dopo_y][pos_dopo_x])
            break
        elif img[y][pos_dopo_x] == green and img[pos_dopo_y][x] == green:
            break
        elif img[pos_dopo_y][pos_dopo_x]==orange:
            coda += 1
            move_tail = False
        posnake.append([pos_dopo_x,pos_dopo_y])
        simuove(posnake,img, pos_dopo_x,pos_dopo_y, move_tail)
        # images.visd(img)
    images.save(img, out_img)
    return coda
    
