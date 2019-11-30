from neopixel import NeoPixel
from machine import Pin
from random import getrandbits


class NeoPixelMatrix(NeoPixel):

    black = (0, 0, 0)
    white = (255, 255, 255)
    
    def __init__(self, p, w, h):
        super().__init__(Pin(p), w*h)
        self.h = h
        self.w = w
        self.m = 100

    def _map(self, v):
        r = int((v[0] / 255) * (self.m))
        g = int((v[1] / 255) * (self.m))
        b = int((v[2] / 255) * (self.m))
        return (r, g, b)

    def rnd(self):
        return (getrandbits(8), getrandbits(8), getrandbits(8))

    def sxy(self, x, y, v):
        if x < self.w and y < self.h and x >=0 and y >=0:
            if y % 2 == 0:
                self[(self.h - 1 - y) * self.w + x] = self._map(v)
            else:
                self[((self.h - y) * self.w) - x - 1] = self._map(v)

    def clr(self):
        self.fill(self.black)
        self.write()