from typing import List, Set;
from gridObj import grids
import pygame
import pygame.freetype
import random
class main:
    def __init__(self):
        global size, rows, distanceBtwRows
        size = 500
        rows = 4
        distanceBtwRows = size // rows
        window = pygame.display.set_mode((int(size * 2.5),size))

        play = True
        self.redraw(window)
        clock=pygame.time.Clock()
        pygame.font.init()
        font = pygame.font.Font(pygame.font.get_default_font(), 30)
        
        
        
        while play: 
            for event in pygame.event.get():
                self.addFont(window, gri.numInaccuracies())
                if event.type == pygame.QUIT:
                    exit()
                elif event.type == pygame.MOUSEBUTTONUP:
                    pos = pygame.mouse.get_pos()
                    if(not gri.retValue(pos[0], pos[1])):
                        gri.changeVal(pos[0], pos[1])
            ticks=pygame.time.get_ticks()
            if(gri.numInaccuracies() != 0):
                self.setTime(window, ticks, clock, font)
    def grid(self, window, size, rows):
        distanceBtwRows = size // rows
        x = 0
        y = 0
        for _ in range(rows + 1):


            pygame.draw.line(window, (0,0,0), (x,0), (x,size))
            pygame.draw.line(window, (0,0,0), (0,y), (size, y))

            z = x + size * 1.5
            pygame.draw.line(window, (0,0,0), (z,0), (z,size))
            pygame.draw.line(window, (0,0,0), (size*1.5,y), (size*3,y))
            
            x+=distanceBtwRows
            y+=distanceBtwRows

    def addImage(self, filepath, window, size, rows, x, y):
        distanceBtwRows = size // rows
        #add relative path below
        print(filepath)
        dieFive = pygame.image.load("images/" + filepath)
        dieFive = pygame.transform.scale(dieFive, (int(distanceBtwRows *.95), int(distanceBtwRows * .95)))
        window.blit(dieFive, (x, y))

    def getFalseValues(self, size, rows, numDifferences, chosenImages, window):
        global gri
        fls = set()
        while len(fls) < numDifferences:
            n = random.randint(0, rows**2 - 1)
            fls.add(n)
        print(fls)
        arr = [True for _ in range(rows**2)]
        #fill in the falses in arr
        for i in fls:
            arr[i] = False
        gri = grids(arr, size, rows)
        self.AddCorrectImages(arr, chosenImages, window, size, rows)
        return arr
        
    def AddCorrectImages(self, arr, chosenImages, window, size, rows):
        images= ['one.png', "two1.png", "two2.png", "three1.png", "three2.png", "four.png", "five.png", "six1.png", "six2.png"]
        x = size * 1.5 + 1
        y = 0
        num = 0
        for i in chosenImages:
            if y >= distanceBtwRows*rows and (x + distanceBtwRows)>= distanceBtwRows*rows * 2.5:
                break
            elif y < distanceBtwRows*rows:
                if arr[num] is False:
                    self.addImage(images[self.exclude(i, images)], window, size, rows, x, y)
                else:
                    self.addImage(images[i], window, size, rows, x, y)
                y += distanceBtwRows + 2
            else:
                x += distanceBtwRows + 1
                y = 0
                if arr[num] is False:
                    self.addImage(images[self.exclude(i, images)], window, size, rows, x, y)
                else:
                    self.addImage(images[i], window, size, rows, x, y)
                y += distanceBtwRows + 2
            num = num + 1
            
    def exclude(self, i, images):
        n = random.randint(0, len(images) - 1)
        while n is i:
            n = random.randint(0, len(images) - 1)
        return n

    def fillImages(self, window, size, rows, numDifferences):
        images= ['one.png', "two1.png", "two2.png", "three1.png", "three2.png", "four.png", "five.png", "six1.png", "six2.png"]
        x = 0
        y = 0
        fill = False
        chosenImages = list()
        while not fill:
            n = random.randint(0, len(images) - 1)
            
            if y >= distanceBtwRows*rows and (x + distanceBtwRows)>= distanceBtwRows*rows:
                fill = True
            elif y < distanceBtwRows*rows:
                self.addImage(images[n], window, size, rows, x, y)
                print(images[n])
                chosenImages.append(n)
                y += distanceBtwRows + 2
            else:
                x += distanceBtwRows + 1
                y = 0
        print(chosenImages)
        falseValues = self.getFalseValues(size, rows, numDifferences, chosenImages, window)
            
    def redraw(self, window):
        global size, rows, distanceBtwRows
        window.fill((255, 255, 255))
        self.grid(window, size, rows)
        self.fillImages(window, size, rows, 4)
        pygame.display.update()

    def addFont(self, window, num):
        pygame.font.init()
        font = pygame.font.Font(pygame.font.get_default_font(), 30)

        # now print the text
        text_surface = font.render("Innaccuracies:" + str(num), True, (0, 0, 0), (255, 255, 255))
        window.blit(text_surface, (size *1.02,size//2))
        pygame.display.update()

    def setTime(self, window, ticks, clock, font):
        pygame.font.init()
        
        millis=ticks%1000
        seconds=int(ticks/1000 % 60)
        minutes=int(ticks/60000 % 24)
        out='{minutes:02d}:{seconds:02d}:{millis:02d}'.format(minutes=minutes, millis=millis, seconds=seconds)
        text_surface = font.render(out, True, (255, 0, 0), (255, 255, 255))
        window.blit(text_surface, (size *1.1,size// 1.5))
        pygame.display.flip()
        clock.tick(60)

m = main()
