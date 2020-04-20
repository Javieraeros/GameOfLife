def calculategamestate(gameState, x, nxC, y, nyC):
    return gameState[(x - 1) % nxC, (y - 1) % nyC] + \
           gameState[x % nxC, (y - 1) % nyC] + \
           gameState[(x + 1) % nxC, (y - 1) % nyC] + \
           gameState[(x - 1) % nxC, y % nyC] + \
           gameState[(x + 1) % nxC, y % nyC] + \
           gameState[(x - 1) % nxC, (y + 1) % nyC] + \
           gameState[x % nxC, (y + 1) % nyC] + \
           gameState[(x + 1) % nxC, (y + 1) % nyC]
