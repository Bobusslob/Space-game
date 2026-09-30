import pygame
import sys
import random

pygame.init()

Ship = pygame.image.load("Assets/Ship.png")
Tank = pygame.image.load("Assets/Tank.png")
Alien1 = pygame.image.load("Assets/Alien1.png")
Alien2 = pygame.image.load("Assets/Alien2.png")
Alien3 = pygame.image.load("Assets/Alien3.png")
Bullet = pygame.image.load("Assets/Bullet.png")

Ship = pygame.transform.scale(Ship, (200, 200))
Tank = pygame.transform.scale(Tank, (200, 200))
Alien1 = pygame.transform.scale(Alien1, (200, 200))
Alien2 = pygame.transform.scale(Alien2, (200, 200))
Alien3 = pygame.transform.scale(Alien3, (200, 200))
Bullet = pygame.transform.scale(Bullet, (30, 30))  


screen = pygame.display.set_mode((2000, 1250))
pygame.display.set_caption("My First Pygame Window")

x1 = 1000
y1 = 1000
x2 = 725
y2 = 800
starter = True
alive = True

bullet_list = []
enemy_list=[]
BULLET_SPEED = 15
SHOOT_COOLDOWN = 15   
ENEMY_SPEED=2.5
ENEMY_COOLDOWN=50
spawn_timer=0
shoot_timer = 0
first=True
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)

font = pygame.font.SysFont("comicsansms", 325)
font2 = pygame.font.SysFont("comicsansms", 400)
text = font.render("Start", True, (255, 255, 255))
text2 = font2.render("SPACE GAME", True, (255, 255, 255))

clock = pygame.time.Clock()


def create_bullet(x, y):
    global bullet_list
    bullet_list.append([x, y])


def update_bullets():
    global bullet_list, bullet
    for bullet in bullet_list:
        bullet[1] -= BULLET_SPEED  

    bullet_list[:] = [b for b in bullet_list if b[1] > -30]


def draw_bullets():
    for bullet in bullet_list:
        screen.blit(Bullet, (bullet[0], bullet[1]))

def create_enemys(ranx):
    enemy_list.append([ranx, 0])

def update_enemy():
    for enemy in enemy_list:
        enemy[1]+= ENEMY_SPEED
        
    enemy_list[:] = [e for e in enemy_list if e[1]]

def draw_enemys():
    global bullet_list, bullet
    for enemy in enemy_list:
        screen.blit(Alien1, (enemy[0], enemy[1]))
        enemy_rect=Alien1.get_rect(topleft=(enemy[0], enemy[1]))
        bullet_rects=[Bullet.get_rect(topleft=(bullet[0], bullet[1])) for bullet in bullet_list]
        for bullet_rect in bullet_rects:
            if enemy_rect.colliderect(bullet_rect):
                enemy_list.remove(enemy)
                bullet_list.remove(bullet)
                break
        if enemy_rect.colliderect(Ship.get_rect(topleft=(x1, y1))):
            global alive
            alive = False
            break
def death():
    global alive,bullet_list, enemy_list,x1,y1
    if alive==False:
        screen.fill((0, 0, 0))
        game_over_text = font.render("Game Over", True, (255, 255, 255))
        screen.blit(game_over_text, (450, 500))
        pygame.draw.rect(screen, GREEN, [x2, y2, 600, 200])
        screen.blit(text,(x2, y2))
        pygame.display.update()
        mouse=pygame.mouse.get_pressed()
        if mouse[0] and alive==False:
            mouse_position=pygame.mouse.get_pos()
            if mouse_position[0]>x2 and mouse_position[0]<x2+600 and mouse_position[1]>y2 and mouse_position[1]<y2+200 and event.type==pygame.MOUSEBUTTONDOWN:
                alive=True
                bullet_list=[]
                enemy_list=[]
                screen.fill((0, 0, 0))
                x1 = 1000
                y1 = 1000
                screen.blit(Ship, (x1, y1))
                return alive
def start():
    global first
    if first:
        screen.fill((0, 0, 0))
        screen.blit(text2, (75, 500))
        pygame.draw.rect(screen, GREEN, [x2, y2, 600, 200])
        screen.blit(text,(x2, y2))
        pygame.display.update()
        mouse=pygame.mouse.get_pressed()
        if mouse[0] and first:
            mouse_position=pygame.mouse.get_pos()
            if mouse_position[0]>x2 and mouse_position[0]<x2+600 and mouse_position[1]>y2 and mouse_position[1]<y2+200 and event.type==pygame.MOUSEBUTTONDOWN:
                first=False
                screen.fill((0, 0, 0))
                return first
                
def game():
    global x1, y1, shoot_timer, spawn_timer, alive
    if first:
        start()
        return
    if not alive:
        death()
        return
    if spawn_timer > 0:
        spawn_timer -= 1
    if len(enemy_list)<=42 and spawn_timer==0:
        ranx = random.randint(0, 1750)
        create_enemys(ranx)
        spawn_timer = ENEMY_COOLDOWN
    pressed = pygame.key.get_pressed()
    if pressed[pygame.K_a]:
        x1 -= 8
    if pressed[pygame.K_d]:
        x1 += 8
    if pressed[pygame.K_w]:
        y1 -= 8
    if pressed[pygame.K_s]:
        y1 += 8
    if shoot_timer > 0:
        shoot_timer -= 1
    if pressed[pygame.K_SPACE] and shoot_timer == 0:
        create_bullet(x1 + 85, y1 - 10)
        shoot_timer = SHOOT_COOLDOWN
    
    update_bullets()
    update_enemy()
    screen.fill((0, 0, 0))
    
    draw_bullets()
    draw_enemys()
    screen.blit(Ship, (x1, y1))
        

running = True
while running:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    game()


    pygame.display.flip()


    clock.tick(60)


pygame.quit()
sys.exit()

running = True