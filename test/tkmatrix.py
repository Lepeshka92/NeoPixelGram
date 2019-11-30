from tkinter import Tk, Canvas
from time import sleep
from random import randrange

class TkMatrix(object):
    black = (0, 0, 0)
    white = (255, 255, 255)
    
    def __init__(self, w, h):
        self.w = w
        self.h = h
        self.s = 50
        self.n = w * h
        self.matrix = []
        for i in range(self.n):
            self.matrix.append("#000000")
        self.canvas = Canvas(Tk(),
                             width=self.s*self.w,
                             height=self.s*self.h,
                             bg="#000000")
        self.canvas.grid()
    
    def __setitem__(self, index, val):
        self.matrix[index] = self._from_rgb(val)
    
    def sxy(self, x, y, v):
        if x >=0 and x < self.w and y >=0 and y < self.h:
            self.matrix[x * self.h + y] = self._from_rgb(v)
    
    def write(self):
        for x in range(self.w):
            for y in range(self.h):
                self.canvas.create_rectangle(x * self.s,
                                             y * self.s,
                                             x * self.s + self.s,
                                             y * self.s + self.s,
                                             fill=self.matrix[x * self.h + y],
                                             outline='#cccccc')
        self.canvas.update()
    
    def clr(self):
        for i in range(self.n):
            self.matrix[i] = "#000000"
        self.write()
    
    def rnd(self):
        return (randrange(255), randrange(255), randrange(255))
    
    def _from_rgb(self, rgb):
        return "#%02x%02x%02x" % rgb
    
    def play(self, cls):
        obj = cls(self)
        fps = obj.fps / 1000
        try:
            while True:
                obj.run(None)
                sleep(fps)
        except Exception as e:
            print(e)
