class Planet(object):
    def __init__(self):
        self.layers = []

class Layer(object):
    def __init__(self):
        self.chunks = []

class Chunk(object):
    def __init__(self):
        self.floor = []
        self.walls = []