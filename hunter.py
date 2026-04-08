import pygame

pygame.init()
width = 1290
height = 650
screen = pygame.display.set_mode((width, height))
run = True

field = pygame.image.load("pic\\field5.jpg").convert_alpha()
field = pygame.transform.scale(field, (1290, 650))
gun = pygame.image.load("pic\\scope.webp").convert_alpha()
gun = pygame.transform.scale(gun, (220, 230))
bird = pygame.image.load("pic\\bird-removebg-preview.png")
bird = pygame.transform.scale(bird, (120, 80))
blood = pygame.image.load("pic\\blood-removebg-preview.png")
blood = pygame.transform.scale(blood, (120, 80))
bird2 = pygame.image.load("pic\\bird2-removebg-preview.png")
bird2 = pygame.transform.scale(bird2, (80, 50))
bird3 = pygame.image.load("pic\\bird3-removebg-preview.png")
bird3 = pygame.transform.scale(bird3, (80, 50))

x = 0
y = 200
x2 = 1300
y2 = 400
x3 = 0
y3 = 300
not_hit = True
not_hit2 = True
not_hit3 = False
clock = pygame.time.Clock()
speed = 0.8
speed2 = 0.6
white = (255, 255, 255)
green = (0, 255, 0)
blue = (0, 0, 128)
font = pygame.font.Font('freesansbold.ttf', 32)
bird_rect = bird.get_rect(center=(0, 0))
kill_count = 0

while run:

    screen.blit(field, (0, 0))
    screen.blit(bird, bird_rect)
    pos = pygame.mouse.get_pos()
    state = pygame.mouse.get_pressed()

    if not_hit:
        screen.blit(bird, (x, y))
    if not_hit2:
        screen.blit(bird2, (x2, y2))
    if not_hit3:
        screen.blit(bird3, (x3, y3))
    if state[0]:
        screen.blit(gun, (pos[0] - 100, pos[1] - 250))
    else:
        screen.blit(gun, (pos[0] - 100, pos[1] - 170))

    if pos[0] - 65 < x and pos[0] + 65 > x and pos[1] - 150 < y and pos[1] - 35 > y and state[0]:
        screen.blit(blood, (x, y))
        x = 0
        y = 0
        kill_count += 1
        not_hit = False
    if pos[0] - 50 <= x2 and pos[0] - 0 >= x2 and pos[1] - 170 < y2 and pos[1] - 60 > y2 and state[0]:
        screen.blit(blood, (x2, y2))
        x2 = 0
        y2 = 0
        kill_count += 1
        not_hit2 = False
    if pos[0] - 40 <= x3 and pos[0] >= x3 and pos[1] - 230 < y3 and pos[1] - 60 > y3 and state[0]:
        screen.blit(blood, (x3, y3))
        x3 = 0
        y3 = 0
        kill_count += 1
        not_hit3 = False
    text = font.render(str(pos[0]) + ' ' + str(pos[1]), True, green, (1, 166, 248))
    textRect = text.get_rect()
    textRect.center = (1150, 50)
    screen.blit(text, textRect)

    x3 += 5
    x += 5
    y -= speed
    x2 -= 5
    y2 -= speed2
    if x > 1290:
        x = 0
    if y > 220:
        speed *= -1
    if y < 200:
        speed *= -1
    if x2 < 0:
        x2 = 1320
    if y2 > 420:
        speed2 *= -1
    if y2 < 400:
        speed2 *= -1
    if x3 > 1290:
        x3 = 0

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    clock.tick(60)
    pygame.display.flip()
pygame.quit()