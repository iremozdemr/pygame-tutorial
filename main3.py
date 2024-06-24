import pygame

pygame.init()

window = pygame.display.set_mode((500,500),pygame.RESIZABLE)
#ekran genişliği değiştirilebilir

#window = pygame.display.set_mode((500,500))
#ekran genişliği değiştirilemez

running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

pygame.quit()