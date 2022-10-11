import random

def sign(x):
    if x > 0:
        return 1
    elif x < 0:
        return -1
    else:
        return 0

class Agent:
    x: int
    y: int
    name: str
    def __init__(self, name: str) -> None:
        self.name = name
        self.x, self.y = 0, 0
        self.tx, self.ty = 0, 0
        self.seeking = False

    def update(self):
        if self.seeking:
            # increase deltax by 1, then deltay by 1
            dx = sign(self.tx - self.x)
            dy = sign(self.ty - self.y)

            if dx == 0 and dy == 0:
                self.seeking = False
            else:    
                self.x += dx
                self.y += dy

        else:
            sz = 10
            self.tx = random.randint(-sz, sz)
            self.ty = random.randint(-sz, sz)
            self.seeking = True