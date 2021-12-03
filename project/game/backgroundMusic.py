import arcade
from game import constants as const

class BackgroundMusic():
    def __init__(self):
        self.startmusic = arcade.Sound(const.RESOURCE_PATH + "startmusic.mp3")
        self.bossmusic = arcade.Sound(const.RESOURCE_PATH + "bossmusic.mp3")
        self.endmusic = arcade.Sound(const.RESOURCE_PATH + "endmusic.mp3")
        self.endmusic1 = arcade.Sound(const.RESOURCE_PATH + "endmusic1.mp3")
        self.backgroundmusic = arcade.Sound(const.RESOURCE_PATH + "backgroundmusic.mp3")
        self.playing = None
        self.id = 0

    def play(self, soundID):
        self.stopPlay()
        if soundID == 0:
            self.playing = arcade.play_sound(self.startmusic, volume = .3, looping = True)
            self.id = soundID
        elif soundID == 1:
            self.playing = arcade.play_sound(self.backgroundmusic, volume = .3, looping = True)
            self.id = soundID
        elif soundID == 2:
            self.playing = arcade.play_sound(self.bossmusic, volume = .3, looping = True)
            self.id = soundID
        elif soundID == 3:
            self.playing = arcade.play_sound(self.endmusic, volume = .3, looping = True)
            self.id = soundID
        elif soundID == 4:
            self.playing = arcade.play_sound(self.endmusic1, volume = .3, looping = True)
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