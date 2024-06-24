import pygame

pygame.init()
#pygame modülünü başlatmak için kullanılır

canvas = pygame.display.set_mode((500,500))
pygame.display.set_caption("my canvas")

running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            
    pygame.display.update()