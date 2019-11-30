from tkmatrix import TkMatrix
from random import getrandbits

class Effect(object): 

    def __init__(self, npm):
        self.fps = 100
        self.npm = npm
        
        self._r = 255
        self._g = 0
        self._b = 0

    def run(self, arg):
        for y in range(self.npm.h):
            for x in range(self.npm.w):
                if self._b == 0:
                    self._g += 5
                    self._r -= 5
                if self._r == 0:
                    self._g -= 5
                    self._b += 5
                if self._g == 0:
                    self._b -= 5
                    self._r += 5
                self.npm.sxy(x, y, (self._r, self._g , self._b))
        self.npm.write()

mtx = TkMatrix(12, 6)
mtx.play(Effect)
