import pygame
import sys

# 1. Initialize Pygame
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
Bullet = pygame.transform.scale(Bullet, (30, 30))  # bullets shouldn't be 200x200

# 2. Set up the display window (Width, Height)
screen = pygame.display.set_mode((2000, 1250))
pygame.display.set_caption("My First Pygame Window")

x1 = 1000
y1 = 1000
starter = True
alive = True

# --- Bullet list: each bullet is just [x, y] so we can update it in place ---
bullet_list = []
BULLET_SPEED = 15
SHOOT_COOLDOWN = 15   # frames between shots, so holding space doesn't fire 60/sec
shoot_timer = 0

GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)

font = pygame.font.SysFont("comicsansms", 325)
font2 = pygame.font.SysFont("comicsansms", 400)
text = font.render("Start", True, (255, 255, 255))
text2 = font2.render("SPACE GAME", True, (255, 255, 255))

# 3. Create a clock object to control the frame rate
clock = pygame.time.Clock()


def create_bullet(x, y):
    """Add a new bullet at the tip of the ship."""
    bullet_list.append([x, y])


def update_bullets():
    """Move every bullet up the screen and drop the ones that fly off-screen."""
    for bullet in bullet_list:
        bullet[1] -= BULLET_SPEED  # move up

    # keep only bullets that are still on screen
    bullet_list[:] = [b for b in bullet_list if b[1] > -30]


def draw_bullets():
    for bullet in bullet_list:
        screen.blit(Bullet, (bullet[0], bullet[1]))


def draw_aliens():
    pass  # TODO: aliens go here later


def game():
    global x1, y1, shoot_timer

    if not alive:
        return

    pressed = pygame.key.get_pressed()
    if pressed[pygame.K_a]:
        x1 -= 8
    if pressed[pygame.K_d]:
        x1 += 8
    if pressed[pygame.K_w]:
        y1 -= 8
    if pressed[pygame.K_s]:
        y1 += 8

    # cooldown counts down every frame; only shoot when it hits 0
    if shoot_timer > 0:
        shoot_timer -= 1
    if pressed[pygame.K_SPACE] and shoot_timer == 0:
        create_bullet(x1 + 85, y1 - 10)
        shoot_timer = SHOOT_COOLDOWN

    update_bullets()

    screen.fill((0, 0, 0))
    draw_aliens()
    draw_bullets()
    screen.blit(Ship, (x1, y1))


# Main Game Loop
running = True
while running:
    # --- Event Handling Loop ---
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # --- Game Logic + Drawing ---
    game()

    # Update the full display Surface to the screen
    pygame.display.flip()

    # --- Frame Rate Cap ---
    clock.tick(60)

# Clean exit out of the application
pygame.quit()
sys.exit()
# Main Game Loop
running = True