from micropython import schedule
from machine import Timer

from npm import NeoPixelMatrix
from api import TelegramBot
from modes.basic import *
from modes.ticker import *

nmatrix = NeoPixelMatrix(2, 12, 6) #pin, width, height
tlg = TelegramBot('TelegramToken')

actions = ('Pong', 'Fire', 'Heart')
keyboard = [[str(i) for i in range(len(actions))]]
current = globals()[actions[0]](nmatrix)

utimer = Timer(-1)
utimer.init(period=current.fps,
            mode=Timer.PERIODIC,
            callback=lambda t:schedule(current.run, None))

auto_n = auto_c = 0
while True:
    
    message = tlg.update()
    
    if message:        
        auto_n = 0
        
        if message[2].isdigit():
            n = int(message[2]) % len(actions)
            utimer.deinit()
            nmatrix.clr()
            current = globals()[actions[n]](nmatrix)
            utimer.init(period=current.fps,
                        mode=Timer.PERIODIC,
                        callback=lambda t:schedule(current.run, None))
            tlg.send(message[0], 'Mode set')
        
        elif '/text' in message[2]:
            utimer.deinit()
            nmatrix.clr()
            current = Ticker(nmatrix)
            current.txt(message[2][5:])
            utimer.init(period=current.fps,
                        mode=Timer.PERIODIC,
                        callback=lambda t:schedule(current.run, None))
        
        elif '/start' in message[2]:
            tlg.send(message[0], 'Select mode', keyboard)
        elif '/empty' in message[2]:
            current = Empty(nmatrix)
            tlg.send(message[0], 'Empty mode set')
        elif '/bright' in message[2]:
            nmatrix.m = int(message[2].split()[1]) % 256
            tlg.send(message[0], 'Bright set')
        else:
            tlg.send(message[0], 'Not Found', keyboard)
    else:
        auto_n = (auto_n + 1) % 10
        if auto_n == 0:
            auto_c = (auto_c + 1) % len(actions)
            utimer.deinit()
            nmatrix.clr()
            current = globals()[actions[auto_c]](nmatrix)
            utimer.init(period=current.fps,
                        mode=Timer.PERIODIC,
                        callback=lambda t:schedule(current.run, None))

utimer.deinit()
nmatrix.clr()