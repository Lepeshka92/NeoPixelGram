from random import getrandbits


class Empty(object):

    def __init__(self, npm):
        self.fps = 200
        self.npm = npm

    def run(self, arg):
        self.npm.clr()
        self.npm.write()

class Fire(object):

    def __init__(self, npm):
        self.fps = 400
        self.npm = npm

        self._n = 255 // self.npm.h

    def run(self, arg):
        for y in range(self.npm.h):
            c = (255, 255 - y * self._n, 0)
            b = 1 if y > self.npm.h // 2 else 2
            for x in range(self.npm.w):
                if getrandbits(b) == 1 or y == self.npm.h - 1:
                    self.npm.sxy(x, y, c)
                else:
                    self.npm.sxy(x, y, self.npm.black)
        
        self.npm.write()

class Pong(object): 

    def __init__(self, npm):
        self.fps = 100
        self.npm = npm
        
        self._y = 1
        self._x = self.npm.w // 2 - 1
        self._dx = 1
        self._dy = 1

    def run(self, arg):
        self.npm.sxy(self._x, self._y, self.npm.black)

        self._x += self._dx
        self._y += self._dy

        if self._x == 1 or self._x == self.npm.w - 2:
            self._dx *= -1
            
        if self._y == 0 or self._y == self.npm.h - 1:
            self._dy *= -1
            
        if self._dx == -1:
            for i in range(self.npm.h):
                self.npm.sxy(0, i, self.npm.black)
            for i in range(-1, 2):
                self.npm.sxy(0, self._y + i, self.npm.white)    
        else:
            for i in range(self.npm.h):
                self.npm.sxy(self.npm.w - 1, i, self.npm.black)
            for i in range(-1, 2):
                self.npm.sxy(self.npm.w - 1, self._y + i, self.npm.white)
        
        self.npm.sxy(self._x, self._y, self.npm.rnd())
        self.npm.write()
        
        
class Heart(object):

    def __init__(self, npm):
        self.fps = 100
        self.npm = npm
        
        self._c = self.npm.w // 2
        self._p = [(self._c, 1),
                  (self._c - 1, 0),
                  (self._c + 1, 0),
                  (self._c - 2, 1),
                  (self._c + 2, 1),
                  (self._c - 2, 2),
                  (self._c + 2, 2),
                  (self._c - 1, 3),
                  (self._c + 1, 3),
                  (self._c, 4)]
        self._n = 1
        self._s = 20

    def run(self, arg):
        for i in self._p:
            self.npm.sxy(i[0], i[1], (self._n, 0, 0))
            
        self._n = min(self._n + self._s, self.npm.m)
        if self._n == self.npm.m or self._n == 0:
            self._s *= -1
        
        self.npm.write()

