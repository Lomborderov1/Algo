class Mapmanager():
    def __init__(self):
        self.model = 'block'
        self.texture = 'block.png'
        self.color = (0.7,0.2,0.35,1)

        self.startNew()
        self.addBlock((0,10,0))