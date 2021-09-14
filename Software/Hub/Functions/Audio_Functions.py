# Audio functions
# https://ttsmp3.com/


import pygame
import os
from time import sleep

#soundPath = "Sounds/MP3/AWS_Connected.mp3"
#soundPath = "Sounds/WAV/AWS_Connected.wav"

def mp3Sound(sound):
    pygame.mixer.init()
    pygame.mixer.music.load(sound)
    sleep(1)
    pygame.mixer.music.set_volume(1.0)
    pygame.mixer.music.play()

    while pygame.mixer.music.get_busy() == True:
        pass

def wavSound(sound):
    import pygame
    pygame.mixer.init()
    pygame.mixer.music.load(sound)
    pygame.mixer.music.play()
    while pygame.mixer.music.get_busy() == True:
        continue
    
def cliSound(sound):
    os.system('aplay /home/pi/Documents/Python/Hub/' + sound)




#mp3Sound(soundPath)
