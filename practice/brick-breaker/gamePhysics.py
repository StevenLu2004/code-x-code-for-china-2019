import gameGeometry as geo
from timeit import default_timer as timer

class Particle:
    def __init__(self, pos = geo.Point(0, 0), vel = geo.Vector(0, 0)):
        self.pos = pos.copy()
        self.vel = vel.copy()
        self.playing = False
    def move(self):
        if self.playing:
            t = timer()
            self.pos += self.vel * (t - self.timestamp)
            self.timestamp = t
    def play(self):
        self.playing = True
        self.timestamp = timer()
    def pause(self):
        self.move()
        self.playing = False
    def setPos(self, pos = geo.Point(0, 0)):
        self.pos = pos.copy()
    def setVel(self, vel = geo.Vector(0, 0)):
        self.vel = vel.copy()
    def bounce(self, pset):
        v1 = pset[0] - self.pos
        v2 = v1.xy_alignx(self.vel)
        v2.y = -v2.y
        self.vel = -v1.xy_restore(v2)
