"""
 
    State Pattern : Audio Player with 3 states and 4 behaivor.
    
"""
from abc import ABC, abstractmethod
 

# States Abstract class
class States(ABC):

    def __init__(self, player):
        self.player = player
    
    def changeState(self, state):
        self.player.changeState(state)
        
    @abstractmethod
    def play(self):
        pass
    @abstractmethod
    def lock(self):
        pass
    @abstractmethod
    def next(self):
        pass
    @abstractmethod
    def prev(self):
        pass    

# Concrete class
class PlayingState(States):
    def play(self):
        print('Stop the audio.')
        self.player.changeState(self.player.readyState)
    def lock(self):
        print('Change to the lock mode.')
        self.player.changeState(self.player.lockState)
    def next(self):
        print('Next ... ')
    def prev(self):
        print('Previous ... ')
    
class ReadyState(States):
    def play(self):
        print('Playing the audio.')
        self.player.changeState(self.player.playingState)
    def lock(self):
        print('Change to the lock mode.')
        self.player.changeState(self.player.lockState)
    def next(self):
        print('The player is not in playing mode. Please press the play button.')
    def prev(self):
        print('The player is not in playing mode. Please press the play button.')


class LockState(States):
    def play(self):
        self.printMode()
    def lock(self):
        print('Change to the unlock mode.')
        self.player.changeState(self.player.readyState)
    def next(self):
        self.printMode()
    def prev(self):
        self.printMode()
    def printMode(self):
        print('This is lock mode.')

        
# Context Class
class AudioPlayer():

    def __init__(self):
        self.currentStates = None
        
        self.readyState = ReadyState(self)
        self.playingState = PlayingState(self)
        self.lockState = LockState(self)
        
        self.changeState(self.readyState)
        print('The Player is Ready')
        

    def changeState(self, currentStates):
        self.currentStates = currentStates
    
    def playAudio(self):
        print('<< Play Button is pressed >>')
        self.currentStates.play()
    def lockPlayer(self):
        print('<< Lock Button is pressed >>')
        self.currentStates.lock()
    def nextAudio(self):
        print('<< Next Button is pressed >>')
        self.currentStates.next()
    def prevAudio(self):
        print('<< Prev Button is pressed >>')
        self.currentStates.prev()
        
        
# Test

if __name__ == '__main__':
    audioPlayer = AudioPlayer()
    audioPlayer.playAudio()
    
    audioPlayer.lockPlayer()
    audioPlayer.nextAudio()
    audioPlayer.prevAudio()
    audioPlayer.playAudio()
    
    audioPlayer.lockPlayer()
    audioPlayer.playAudio()
    audioPlayer.nextAudio()
    audioPlayer.prevAudio()
  