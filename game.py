import pygame, sys, os
from pygame.locals import *

class Constants:
    # Tiles are square
    TileSize = 32
    NumTilesWidth = 20
    NumTilesHeight = 20

class Tile:
    pass

class TileCache:
    def __init__(self, filenames):
        self.filenames = filenames
        self.imageCache = {}

    def loadAllImages(self):
        for filename in self.filenames:
            img = pygame.image.load(os.path.join("player.png"))
            img.load()
            imageCache[filename] = img

    def getImage(filename):
        return imgCache[filename]

class Game:
    def __init__(self):
        self.tileCache = TileCache([])
        print("Loading tiles to title cache...")
        self.tileCache.loadAllImages()
        pygame.init()
        height = Constants.TileSize * Constants.NumTilesHeight
        width = Constants.TileSize * Constants.NumTilesWidth
        self.screen = pygame.display.set_mode((height, width))
        self.height = Constants.NumTilesHeight
        self.width = Constants.NumTilesWidth
        self.tileSize = Constants.TileSize

        self.x = 10
        self.y = 10

        # Finally, run the game loop
        self.gameLoop()

    # Main Game Loop
    def gameLoop(self):
        x = self.x
        y = self.y
        while True:
            # Process events to happen in the game
            for event in pygame.event.get():
                print(event)
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_LEFT:
                        x = x - 1
                    elif event.key == pygame.K_RIGHT:
                        x = x + 1
                    elif event.key == pygame.K_UP:
                        y = y - 1
                    elif event.key == pygame.K_DOWN:
                        y = y + 1

            for row in range(self.height):
                for column in range(self.width):
                    pygame.draw.rect(self.screen, (0,255,0), (column*self.tileSize, row * self.tileSize, self.tileSize, self.tileSize))

            squirrel = pygame.image.load(os.path.join("squirrelright.png"))
            self.screen.blit(squirrel, (x * self.tileSize, y * self.tileSize))
            pygame.display.flip()
            pygame.display.update()


# Play the game
Game().gameLoop()
