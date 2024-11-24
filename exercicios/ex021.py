# Solução Chat GPT
import pygame
pygame.mixer.init()
pygame.mixer.music.load('ex021.mp3')
pygame.mixer.music.play()
#pygame.event.wait() - nao sei o motivo, mas a solucao de execucao do professor nao funcionol

while pygame.mixer.music.get_busy():
 pygame.time.Clock().tick(10)
 