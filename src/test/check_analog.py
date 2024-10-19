from machine import Pin, ADC


from time import sleep
class Mic:
    def __init__(self):
        self.counter = 0
        self.summer = 0
        self.maxer = 0
        self.miner = 65535
    
    def __iadd__(self, other):
        self.counter += 1
        self.summer +=other
        self.maxer = max(self.maxer, other)
        self.miner = min(self.miner, other)
        if self.counter == 10000/2:
            print(self.miner, self.maxer, self.summer/self.counter, (self.maxer-self.miner)//1000)
            self.reset()
        return self
    
    def reset(self):
        self.counter = 0
        self.summer = 0
        self.maxer = 0
        self.miner = 65535

pot1 = ADC(Pin(27))
pot2 = ADC(Pin(28))
mic1 = Mic()
mic2 = Mic()
while True:
    mic1 += pot1.read_u16()
    mic2 += pot2.read_u16()

