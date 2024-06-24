import pygame

pygame.init()

window = pygame.display.set_mode()

x,y = window.get_size()

pygame.quit()

print(x)
print(y)
print(x,y)
#ekranın genişliğini ve window yüksekliğini bulmak için kullanılır