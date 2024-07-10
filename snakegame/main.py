#https://www.youtube.com/watch?v=XGf2GcyHPhc , stopped at 1:04:03
import pygame
import math
import random
import sys
import tkinter as tk
from tkinter import messagebox

#w is the width/length of the screen

class cube(object):
    rows = 0
    w = 0
    pass


class snake(object):
   body = []
   turns = {}
   def ___init___(self, color, pos):
       self.color = color
       self.head = cube(pos) #head has the position of the cube
       self.body.append(self.head) #body will go after the head
       self.directx = 0 
       self.directy = 1 #it starts out moving down

    def move(self):
       for event in pygame.event.get():
           if event.type == pygame.QUIT:
                pygame.quit()
            keys = pygame.key.get_pressed() #gets a list of all possible keys and if they were pressed. 
           for key in keys: #gives all of the key values, and then 1 or 0 if they are/are not clicked
                if keys[pygame.K_LEFT]:
                    self.directx = -1
                    self.directy = 0
                    self.turns[self.head.pos[:]] = [self.directx, self.directy] #says that there is a new turn, at that position, and self.directx, self.directy, is the direction it turns
                elif keys[pygame.K_RIGHT]:
                    self.directx = 1
                    self.directy = 0
                    self.turns[self.head.pos[:]] = [self.directx, self.directy]
                elif keys[pygame.K_UP]:
                    self.directx = 0
                    self.directy = -1
                    self.turns[self.head.pos[:]] = [self.directx, self.directy]
                elif keys[pygame.K_DOWN]:
                    self.directx = 0
                    self.directy = 1
                    self.turns[self.head.pos[:]] = [self.directx, self.directy]
        for i, c in enumerate(self.body): #looks through all the positions on the snake
            p = c.pos[:]      #[:] makes  a copy of the list
               
        

def drawGrid(w, rows, surface):
    sizeBetween = w//rows #distance between each row and column in the grid
    x = 0
    y = 0

    for i in range(rows):
        x = x + sizeBetween
        y = y + sizeBetween

        pygame.draw.line(surface, (255,255,255), (x,0),(x,w)) #vertical line: (x,0) is start position and (x,w) is the end position of the line
        pygame.draw.line(surface, (255,255,255), (0,y),(w,y)) #(255,255,255) is white

def redrawWindow(surface):
    global rows
    global width

    surface.fill((0,0,0)) #fills screen with a color; (0,0,0) is black
    drawGrid(width, rows, surface)
    pygame.display.update()


def randomSnack(rows, items):
    pass

def message_box(subject, content):
    pass

def main():
    global width
    global rows
    width = 500
    height = 500
    rows = 20
    win = pygame.display.set_mode((width, width))
    #s = snake((0, 0, 255), (10,10)) #(0, 0, 255) is blue
    flag = True

    clock = pygame.time.Clock()

    while flag:
        pygame.time.delay(50) #delays program by 50 millisecond every time so the program isnt too fast
        clock.tick(10) #keeps the game running at 10 FPS(aka snake can move 10 blocks in 1 second)
        redrawWindow(win)
    pass


main()

