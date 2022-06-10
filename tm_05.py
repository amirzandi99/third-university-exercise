import sys, pygame
from pygame.locals import*

def main():
    Color_screen = (230,230,230)
    Color_line1 = (50,50,230)
    Color_line2 = (230,50,50)
    screen = pygame.display.set_mode((500,400))
    screen.fill(Color_screen)
    # A
    pygame.draw.line(screen,Color_line1,(80,250),(130,150))   # /
    pygame.draw.line(screen,Color_line1,(180,250),(130,150))  # \
    pygame.draw.line(screen,Color_line1,(100,210),(160,210))  # --
    # Z
    pygame.draw.line(screen,Color_line2,(280,150),(370,150))   # --
    pygame.draw.line(screen,Color_line2,(280,250),(370,150))   # /
    pygame.draw.line(screen,Color_line2,(280,250),(370,250))   # --
    pygame.display.flip()
    while True:
        for events in pygame.event.get():
            if events.type == QUIT:
                sys.exit(0)
# 
# 
if __name__ == "__main__":
    main()