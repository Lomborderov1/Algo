from direct.showbase.ShowBase import ShowBase
from mapmanager import Mapmanager

class Game(ShowBase):
    def __init__(self):
        ShowBase.__init__(self)
        self.lend = Mapmanager()
        bass.camLens.setFov

game = Game()
game.run