import pygame
from pygame.locals import *


pygame.init()

SCREEN_WIDTH, SCREEN_HEIGHT = 1000, 800
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)

running = True

pezzi = {
    # Torri, cavalli, alfieri, regina e re bianchi
    "A1": "torre_bianca", "B1": "cavallo_bianco", "C1": "alfiere_bianco",
    "D1": "regina_bianca", "E1": "re_bianco", "F1": "alfiere_bianco",
    "G1": "cavallo_bianco", "H1": "torre_bianca",

    # Pedoni bianchi
    "A2": "pedone_bianco", "B2": "pedone_bianco", "C2": "pedone_bianco",
    "D2": "pedone_bianco", "E2": "pedone_bianco", "F2": "pedone_bianco",
    "G2": "pedone_bianco", "H2": "pedone_bianco",

    # Pedoni neri
    "A7": "pedone_nero", "B7": "pedone_nero", "C7": "pedone_nero",
    "D7": "pedone_nero", "E7": "pedone_nero", "F7": "pedone_nero",
    "G7": "pedone_nero", "H7": "pedone_nero",

    # Torri, cavalli, alfieri, regina e re neri
    "A8": "torre_nera", "B8": "cavallo_nero", "C8": "alfiere_nero",
    "D8": "regina_nero", "E8": "re_nero", "F8": "alfiere_nero",
    "G8": "cavallo_nero", "H8": "torre_nera",
}

pedone_bianco = pygame.image.load("pedone_bianco.png")
pedone_bianco = pygame.transform.scale(pedone_bianco, (50, 50))  
torre_bianca = pygame.image.load("torre_bianca.png")
torre_bianca = pygame.transform.scale(torre_bianca, (50, 50))
alfiere_bianco = pygame.image.load("alfiere_bianco.png")
alfiere_bianco = pygame.transform.scale(alfiere_bianco, (50, 50))  
cavallo_bianco = pygame.image.load("cavallo_bianco.png")
cavallo_bianco = pygame.transform.scale(cavallo_bianco, (50, 50))  
regina_bianca = pygame.image.load("regina_bianca.png")
regina_bianca = pygame.transform.scale(regina_bianca, (50, 50))
re_bianco = pygame.image.load("re_bianco.png")
re_bianco = pygame.transform.scale(re_bianco, (50, 50))

pedone_nero = pygame.image.load("pedone_nero.png")
pedone_nero = pygame.transform.scale(pedone_nero, (50, 50))
torre_nera = pygame.image.load("torre_nera.png")
torre_nera = pygame.transform.scale(torre_nera, (50, 50))
alfiere_nero = pygame.image.load("alfiere_nero.png")
alfiere_nero = pygame.transform.scale(alfiere_nero, (50, 50))
cavallo_nero = pygame.image.load("cavallo_nero.png")
cavallo_nero = pygame.transform.scale(cavallo_nero, (50, 50))
regina_nera = pygame.image.load("regina_nera.png")
regina_nera = pygame.transform.scale(regina_nera, (50, 50))
re_nero = pygame.image.load("re_nero.png")
re_nero = pygame.transform.scale(re_nero, (50, 50))
                                                     


while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            row = mouse_x // 100
            col = mouse_y // 100
            print(row)
            print(col)
            
        #SCACCHIERA
        for row in range(8):
            for col in range(0,8):
                color = WHITE if (row + col) % 2 == 0 else BLACK
                pygame.draw.rect(screen, color, (col * 100, row * 100, 100, 100))
                
                #INSERIMENTO PEDONI BIANCHI
                if row == 6:
                    screen.blit(pedone_bianco, (col * 100 + 25, row * 100 + 25)) 
                #INSERIMENTO TORRI BIANCHE
                if row == 7 and col == 0 or row == 7 and col == 7:
                    screen.blit(torre_bianca, (col * 100 + 25, row * 100 + 25)) 
                #INSERIMENTO ALFIERI BIANCHI
                if row == 7 and col == 1 or row == 7 and col == 6:
                    screen.blit(alfiere_bianco, (col * 100 + 25, row * 100 + 25)) 
                #INSERIMENTO CAVALLI BIANCHI
                if row == 7 and col == 2 or row == 7 and col == 5:
                    screen.blit(cavallo_bianco, (col * 100 + 25, row * 100 + 25)) 
                #INSERIMENTO REGINA BIANCA
                if row == 7 and col == 3:
                    screen.blit(regina_bianca, (col * 100 + 25, row * 100 + 25)) 
                #INSERIMENTO RE BIANCO
                if row == 7 and col == 4:
                    screen.blit(re_bianco, (col * 100 + 25, row * 100 + 25)) 
                
                #INSERIMENTO PEDONI NERI
                if row == 1:
                    screen.blit(pedone_nero, (col * 100 + 25, row * 100 + 25))
                #INSERIMENTO TORRI NERE
                if row == 0 and col == 0 or row == 0 and col == 7:
                    screen.blit(torre_nera, (col * 100 + 25, row * 100 + 25)) 
                #INSERIMENTO ALFIERI NERI
                if row == 0 and col == 1 or row == 0 and col == 6:
                    screen.blit(alfiere_nero, (col * 100 + 25, row * 100 + 25)) 
                #INSERIMENTO CAVALLI NERI   
                if row == 0 and col == 2 or row == 0 and col == 5:
                    screen.blit(cavallo_nero, (col * 100 + 25, row * 100 + 25)) 
                #INSERIMENTO REGINA NERA
                if row == 0 and col == 3:
                    screen.blit(regina_nera, (col * 100 + 25, row * 100 + 25)) 
                #INSERIMENTO RE BIANCO
                if row == 0 and col == 4:
                    screen.blit(re_nero, (col * 100 + 25, row * 100 + 25)) 
                
                
    pygame.display.update()
pygame.quit()
