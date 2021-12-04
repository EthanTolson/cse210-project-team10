from arcade import Sound
from arcade import play_sound
from game import constants as const

class BackgroundMusic():
    def __init__(self):
        self.startmusic = Sound(const.RESOURCE_PATH + "startmusic.mp3")
        self.bossmusic = Sound(const.RESOURCE_PATH + "bossmusic.mp3")
        self.endmusic = Sound(const.RESOURCE_PATH + "endmusic.mp3")
        self.endmusic1 = Sound(const.RESOURCE_PATH + "endmusic1.mp3")
        self.backgroundmusic = Sound(const.RESOURCE_PATH + "backgroundmusic.mp3")
        self.playing = None
        self.id = 0

    def play(self, soundID):
        self.stopPlay()
        if soundID == 0:
            self.playing = play_sound(self.startmusic, volume = .3, looping = True)
            self.id = soundID
        elif soundID == 1:
            self.playing = play_sound(self.backgroundmusic, volume = .2, looping = True)
            self.id = soundID
        elif soundID == 2:
            self.playing = play_sound(self.bossmusic, volume = .2, looping = True)
            self.id = soundID
        elif soundID == 3:
            self.playing = play_sound(self.endmusic, volume = .3, looping = True)
            self.id = soundID
        elif soundID == 4:
            self.playing = play_sound(self.endmusic1, volume = .3, looping = True)
            self.id = soundID

    def stopPlay(self):
        if self.playing != None:
            if self.startmusic.is_playing(self.playing):
                self.startmusic.stop(self.playing)
            elif self.backgroundmusic.is_playing(self.playing):
                self.backgroundmusic.stop(self.playing)
            elif self.bossmusic.is_playing(self.playing):
                self.bossmusic.stop(self.playing)
            elif self.endmusic.is_playing(self.playing):
                self.endmusic.stop(self.playing)
            elif self.endmusic1.is_playing(self.playing):
                self.endmusic1.stop(self.playing)

    def getPlayingID(self):
        return self.id