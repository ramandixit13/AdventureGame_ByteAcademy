#Sound module for Adventure Game

import pygame, time

def play(filename, t):
    pygame.init()
    pygame.mixer.music.load(str(filename))
    pygame.mixer.music.play()
    time.sleep(int(t))
    
if __name__ == "__main__":
    play('music/test.wav', 10)