import sys, pygame
from pygame.locals import*
Color_screen = (230,230,230)
Color_line = (50,50,50)
screen=pygame.display.set_mode((500,400))
screen.fill(Color_screen)
# roof
pygame.draw.line(screen,Color_line,(140,95),(250,20))   # /
pygame.draw.line(screen,Color_line,(370,95),(250,20))   # \
# body
pygame.draw.line(screen,Color_line,(370,95),(370,300))    # |
pygame.draw.line(screen,Color_line,(140,95),(140,300))    # |
pygame.draw.line(screen,Color_line,(140,95),(370,95))     # --
pygame.draw.line(screen,Color_line,(140,300),(370,300))     # --
# door
pygame.draw.line(screen,Color_line,(230,220),(230,300))    # |
pygame.draw.line(screen,Color_line,(180,220),(180,300))    # |
pygame.draw.line(screen,Color_line,(230,220),(180,220))     # --
# window
pygame.draw.line(screen,Color_line,(280,120),(280,180))    # |
pygame.draw.line(screen,Color_line,(350,120),(350,180))    # |
pygame.draw.line(screen,Color_line,(280,120),(350,120))     # --
pygame.draw.line(screen,Color_line,(280,180),(350,180))     # --
# Chimney
pygame.draw.line(screen,Color_line,(170,40),(170,75))    # |
pygame.draw.line(screen,Color_line,(185,40),(185,65))    # |
pygame.draw.line(screen,Color_line,(170,40),(185,40))     # --
pygame.display.flip()
while True:
    for events in pygame.event.get():
        if events.type == QUIT:
            sys.exit(0)