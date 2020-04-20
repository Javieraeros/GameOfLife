import pygame
import numpy as np
import time
from functions import *

pygame.init()

width, height = 1000, 1000
screen = pygame.display.set_mode((width, height))

bg = 25, 25, 25
screen.fill(bg)

nxC, nyC = 25, 25

dimCW = width / nxC
dimCH = height / nyC

gameState = np.zeros((nxC, nyC))
# gameState[12, 12] = 1
# gameState[11, 12] = 1
# gameState[11, 11] = 1
# gameState[11, 13] = 1
# gameState[12, 11] = 1
# gameState[12, 13] = 1
gameState[13, 11] = 1
gameState[13, 12] = 1
gameState[13, 13] = 1

pauseExec = False
endGame = False

while not endGame:

    newGameState = np.copy(gameState)
    screen.fill(bg)

    for y in range(0, nxC):
        for x in range(0, nyC):
            if not pauseExec:
                n_neigh = calculategamestate(gameState, x, nxC, y, nyC)

                # Rule 1: Dead cell with 3 alive neighs, revives
                # Rule 2: Alive cell with less than 2 or more than 3 alive neighs, dead
                if gameState[x, y] == 0 and n_neigh == 3:
                    newGameState[x, y] = 1
                elif gameState[x, y] == 1 and (n_neigh < 2 or n_neigh > 3):
                    newGameState[x, y] = 0

            poly = [(x * dimCW, y * dimCH),
                    ((x + 1) * dimCW, y * dimCH),
                    ((x + 1) * dimCW, (y + 1) * dimCH),
                    (x * dimCW, (y + 1) * dimCH)]
            if newGameState[x, y] == 0:
                pygame.draw.polygon(screen, (128, 128, 128), poly, 1)
            else:
                pygame.draw.polygon(screen, (255, 255, 255), poly, 0)

    ev = pygame.event.get()
    for event in ev:
        if event.type == pygame.KEYDOWN:
            pauseExec = not pauseExec
        elif event.type == pygame.QUIT:
            endGame = True
        mouseClick = pygame.mouse.get_pressed()
        if sum(mouseClick) > 0:
            posX, posY = pygame.mouse.get_pos()
            celX, celY = int(np.floor(posX / dimCW)), int(np.floor(posY / dimCH))
            newGameState[celX, celY] = not gameState[celX, celY]

    gameState = np.copy(newGameState)
    time.sleep(0.1)
    pygame.display.flip()
