class Mapmanager():
    """ Управление картой """
    def __init__(self):
        self.model = 'block.egg' 
        self.texture = 'block.png'
        self.color = (0.5, 0.3, 0.0, 1) #rgba

        self.startNew() 
        #self.addBlock((0,10, 0))

    def startNew(self):
        """создаёт основу для новой карты""" 
        self.land = render.attachNewNode("Land") 
    def addBlock(self, position):
        self.block = loader.loadModel(self.model)
        self.block.setTexture(loader.loadTexture(self.texture)) 
        self.block.setPos(position)
        self.block.setColor(self.color)
        self.block.reparentTo(self.land)

    def clear(self):
        self.land.removeNode()
        self.startNew()

    def loadLand(self, filename):
        self.clear()
        with open(filename) as file:
            y = 0
            for line in file:
                x = 0
                line = line.split(' ')
                for z in line: 
                    for z0 in range(int(z)+1):
                        self.addBlock((x,y,z0))
                    x += 1
                y += 1