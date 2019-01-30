"""
    Facade Pattern : Home Theater System

"""

class OnOff():
    
    def on(self):
        print(self.__class__.__name__, 'is on')
    
    def off(self):
        print(self.__class__.__name__ + 'is off')

class Screen():
    def up(self):
        print('Screen is up')
    def down(self):
        print('Screen is down')

class PopcornMachine(OnOff):
    def pop(self):
        print('Pop the popcorn')

class Lights(OnOff):
    def setDim(self, num):
        print('Set Light dim to {0}'.format(num))

        
class Amplifier(OnOff):

    def setTuner(self, tuner):
        self.tuner = tuner
    def setDvd(self, dvdPlayer):
        self.dvdPlayer = dvdPlayer
    def setSurroundSound(self):
        print('Set the Stereo Sound')
    def setVolume(self, num):
        self.volume = num
        print('Set volume to {0}.'.format(num))

class DvdPlayer(OnOff):

    def play(self):
        print('Dvd is playing')
    def stop(self):
        print('Dvd is stoping')

class Projector(OnOff):

    def tvMode(self):
        print('Turn to Tv mode')
        
        
# Facade Class
class HomeTheaterFacade():
    def __init__(self, screen, popcorn, light, amplifier, dvdPlayer, projector):
        self.screen = screen
        self.popcorn = popcorn
        self.light = light
        self.amplifier = amplifier
        self.dvdPlayer = dvdPlayer
        self.projector = projector
        
    def watchMovie(self):
        print('Get ready to watch a movie ...')
        self.popcorn.on()
        self.popcorn.pop()
        
        self.light.setDim(10)
        self.screen.down()
        
        self.projector.on()
        self.projector.tvMode()
        
        self.amplifier.on()
        self.amplifier.setDvd(self.dvdPlayer)
        self.amplifier.setVolume(5)
        
        self.dvdPlayer.on()
        self.dvdPlayer.play()
    
    def endMovie(self):
        print('Shutting movie theater down ...')
        
        self.popcorn.off()
        self.light.on()
        self.screen.up()
        self.projector.off()
        self.amplifier.off()
        self.dvdPlayer.stop()
        self.dvdPlayer.off()

        
# Test
if __name__ == '__main__':
    homeTheater = HomeTheaterFacade(Screen(), PopcornMachine(), Lights(), Amplifier(), DvdPlayer(), Projector())
    
    homeTheater.watchMovie()
    homeTheater.endMovie()