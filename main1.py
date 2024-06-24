import pygame

pygame.init()
#pygame modülünü başlatmak için kullanılır

canvas = pygame.display.set_mode((500,500))
#window size

pygame.display.set_caption("my canvas")
#window title

image = pygame.image.load("image.jpg")
pygame.display.set_icon(image)
#window icon

running = True

while running:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    
    pygame.display.update()