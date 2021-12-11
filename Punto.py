class Punto:

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def ajustar(self):
        return int((self.x * 100) + 2), int(abs((self.y * 100) + 10))
