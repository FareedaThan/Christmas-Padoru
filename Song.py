import pygame
from pygame import mixer

class ThemeSong():
    def __init__(self):
      self.lyrics = ["HASHIRE SORI YO", "KAZE NO YOU NI", "TSUKIMIHARA WO","PADORU PADORU"]
      self.count = 0
      mixer.music.set_volume(0)
    
    def set_volume(self,volume=0):
     mixer.music.set_volume(volume)
     
    def play(self):
        step = self.count % 4
        mixer.music.load(f"./ThemeSong/Padoru_Song{step+1}.wav")
        mixer.music.play(0)
        self.count +=1
        return self.lyrics[step]
     
    