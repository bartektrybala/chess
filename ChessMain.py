"""
This is our main driver filer. 
It will responsible for handling user input and displaying the current GameState object.
"""

import pygame as p
import ChessEngine

WIDHT = HEIGHT = 512    #400 is another option
DIMENSION = 8           #dimentions of a chess board are 8x8
SQ_SIZE = HEIGHT // DIMENSION
MAX_FPS = 15            #for animations later on
IMAGES = {}

"""
Initialize a global dictionary of images. This will be called exactly once in the main
"""

def loadImages():
    pieces = ['wp', 'wR', 'wN', 'wB', 'wK', 'wQ', 'bp', 'bR', 'bN', 'bB', 'bK', 'bQ']
    for piece in pieces:
        IMAGES[piece] = p.transform.scale(p.image.load('images/' + piece + '.png'), (SQ_SIZE, SQ_SIZE))
    #Note: we can access an image by saying 'IMAGES['wp']'

'''
The main driver for our code. This will handle user input and updating the graphics
'''
def main():
    p.init()
    screen = p.display.set_mode((WIDHT, HEIGHT))
    clock = p.time.Clock()
    screen.fill(p.Color('white'))
    gs = ChessEngine.GameState()
    loadImages()    #only do this once, before the while loop
    running = True
    while running:
        for e in p.event.get():
            if e.type == p.QUIT:
                running = False
        drawGameState(screen, gs)
        clock.tick(MAX_FPS)
        p.display.flip()
'''
Resposible for all the graphics within a current game state.
'''

def drawGameState(screen, gs):
    drawBoard(screen) #draw squares on the board
    #add in piece highliting or move suggestions (later)
    drawPieces(screen, gs.board) #draw pieces on top of those squares

'''
Draw the squares on the board.
'''
def drawBoard(screen):
    colors = [p.Color('white'), p.Color('gray')]
    for r in range(DIMENSION):
        for c in range(DIMENSION):
            color = colors[((r+c) % 2)]
            p.draw.rect(screen, color, p.Rect(c*SQ_SIZE, r*SQ_SIZE, SQ_SIZE, SQ_SIZE))



'''
Draw the pieces on the board using the current GamaState.board
'''
def drawPieces(screen, board):
    pass

if __name__ == '__main__':
     main() 