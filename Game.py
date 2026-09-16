import pygame
import sys
# test test
# 1. Initialize Pygame
pygame.init()
Ship= pygame.image.load("Assets/Ship.png")
Tank= pygame.image.load("Assets/Tank.png")
Alien1= pygame.image.load("Assets/Alien1.png")
Alien2= pygame.image.load("Assets/Alien2.png")
Alien3= pygame.image.load("Assets/Alien3.png")
Bullet= pygame.image.load("Assets/Bullet.png")
Ship=pygame.transform.scale(Ship, (200, 200))
Tank=pygame.transform.scale(Tank, (200, 200))
Alien1=pygame.transform.scale(Alien1, (200, 200))
Alien2=pygame.transform.scale(Alien2, (200, 200))
Alien3=pygame.transform.scale(Alien3, (200, 200))
# 2. Set up the display window (Width, Height)
screen = pygame.display.set_mode((2000, 1250))
x1=1000
y1=1000
x=2000
y=1250
starter=True
alive=True
bullet_list = []
GREEN = (  0, 255,   0)
RED = (  255, 0,   0)
BLUE = (  0, 0,   255)
font = pygame.font.SysFont("comicsansms",325)
font2 = pygame.font.SysFont("comicsansms",400)
text = font.render("Start", True, (255, 255, 255))
text2 = font2.render("SPACE GAME", True, (255, 255, 255))
pygame.display.set_caption("My First Pygame Window")
class Bullets():
    def __init__(self, bullet, pos):
        self.set_bullet(bullet)
        self.set_pos(pos)
    def set_bullet(self,bullet):
            self._bullet=bullet
    def get_bullet(self):
            return self._bullet
    def set_pos(self,pos):
            self._pos=pos
    def get_pos(self):
            return self._pos
# 3. Create a clock object to control the frame rate
clock = pygame.time.Clock()
screen.fill((0, 0, 0)) 
# Main Game Loop
running = True
while running:
    
    # --- Event Handling Loop ---
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # --- Game Logic ---
    # (Your player movement and collision code will go here)

    # --- Drawing / Rendering ---
    # Fill the screen with an RGB color (Red, Green, Blue)
    def drawAliens():
        print()
    def Game():
        if alive:
            global x1, y1, bullet_list
            pressed = pygame.key.get_pressed()
            if pressed[pygame.K_a]:
                x1 = x1 - 8
                print(x1)
            if pressed[pygame.K_d]:
                x1 = x1 + 8
                print(x1)
            if pressed[pygame.K_w]:
                y1 = y1 - 8
                print(y1)
            if pressed[pygame.K_s]:
                y1 = y1 + 8
                print(y1)
            print(x1)
            print(y1)
            
            if pressed[pygame.K_SPACE]:
                bullet_list.append((x1+85 , y1-10))  
            screen.fill((0, 0, 0))
            screen.blit(Ship, (x1, y1))              
        

    # Update the full display Surface to the screen

    Game()
    pygame.display.flip()

    # --- Frame Rate Cap ---
    # Limits the loop to exactly 60 frames per second
    clock.tick(60)

# Clean exit out of the application
pygame.quit()
sys.exit()
