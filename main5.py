import pygame

pygame.init()

window = pygame.display.set_mode((500,500))

window.fill("purple")
#arka plan rengi

pygame.draw.rect(window,"pink",pygame.Rect(30,30,60,60))
#dikdörtgen çizme

image = pygame.image.load("image.jpg")
window.blit(image,(100,100))
#image ekleme

running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    pygame.display.flip()
    #ekranı güncelleme

pygame.quit()