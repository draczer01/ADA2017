from random import randint
from random import choice
import pygame,sys
from pygame.locals import *



def dfs(img, coord, coloro, colorn):
        #print('p c:', pred, coord)
        p = [coord]
        vis = [coord]
        rang = 15
        while len(p)>0:
                print(len(p))
                ap = p.pop()
                vis.append(ap)
                x,y = ap
                u = (x,y+1)
                d = (x,y-1)
                l = (x-1,y)
                r = (x+1,y)
                childs = [u,d,l,r]
                for c in childs:
                        if c in vis:
                                childs.remove(c)
                if x>0 and x < img.get_width() and y>0 and y< img.get_height():
                        col = img.get_at(ap)                
                        #print('found color in img')
                        b,g,r,i = col
                        bc,gc,rc,ic = coloro
                        valid = (bc-rang <= b and b <=bc+rang) and  (gc-rang <= g and g <=gc+rang) and (rc-rang <= r and r <=rc+rang)
                        if valid:
                                print('color in spectre, set and update', ap, colorn)
                                img.set_at(ap, colorn)
                                for c in childs:
                                        if c not in p and c not in vis:
                                                p.append(c)
                
def fill():
	pygame.init()
	fondo=pygame.image.load("files/fill.png")
	pygame.display.set_caption("Bucket fill")
	ventana=pygame.display.set_mode(fondo.get_size())

        
	while True:		
            ventana.blit(fondo,(0,0))
            pygame.display.update()
            for evento in pygame.event.get():
                #obtener ubicacion del pixel
                mouse=pygame.mouse.get_pos()
                mousepress = pygame.mouse.get_pressed()
                if evento.type==QUIT :
                    print('quit')
                    pygame.quit()
                    sys.exit()
                if evento.type == pygame.MOUSEBUTTONDOWN and mousepress[0]==1:
                    col = fondo.get_at(mouse)
                    newcol = (255,0,0,255)
                    if col == newcol:
                            newcol = (0,0,255,255)
                    #fondo.set_at(mouse, newcol)
                    #dfs
                    print(mouse, col, newcol)
                    dfs(fondo, mouse, col, newcol)
                    pygame.display.update()

fill()
