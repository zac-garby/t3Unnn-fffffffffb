CHUNK_SIZE = 64

class Planet(object):
    def __init__(self, height, chunk_width, chunk_height):
        self.chunk_width = chunk_width
        self.chunk_height = chunk_height
        self.height = height
        self.layers = []

        for z in range(height):
            self.layers.append(Layer(self))

class Layer(object):
    def __init__(self, planet):
        self.chunks = []
        self.planet = planet

        for y in range(planet.chunk_height):
            row = []
            for x in range(planet.chunk_width):
                row.append(Chunk(self))
            self.chunks.append(row)


class Chunk(object):
    def __init__(self, layer):
        self.floor = []
        self.walls = []

        for y in range(CHUNK_SIZE):
            floor_row = []
            walls_row = []
            for x in range(CHUNK_SIZE):
                floor_row.append(Tile())
                walls_row.append(Tile())
            self.floor.append(floor_row)
            self.walls.append(walls_row)

class Tile(object):
    def __init__(self):
        pass