import tkinter as TK
import gameGeometry as geo
import gamePhysics as phys
import globalVars as gVars

class StaticRectangle:
    def __init__(self, canv, centerX, centerY, width, height):
        self.rect = canv.create_rectangle(centerX - width / 2, centerY - height / 2, centerX + width / 2, centerY + height / 2, state = "hidden")
        self.cornerPoints = [\
            geo.Point(centerX - width / 2, centerY - height / 2), \
            geo.Point(centerX + width / 2, centerY - height / 2), \
            geo.Point(centerX + width / 2, centerY + height / 2), \
            geo.Point(centerX - width / 2, centerY + height / 2)\
        ]
        self.sideSegments = [\
            geo.LineSegment(self.cornerPoints[0], self.cornerPoints[1]), \
            geo.LineSegment(self.cornerPoints[1], self.cornerPoints[2]), \
            geo.LineSegment(self.cornerPoints[2], self.cornerPoints[3]), \
            geo.LineSegment(self.cornerPoints[3], self.cornerPoints[0])\
        ]
        self.canv = canv
    def __del__(self):
        self.canv.delete(self.rect)
    def helpColli(self, circle):
        f = False
        for p in self.cornerPoints:
            f = f or (circle.checkColli(p))
        if f:
            return f
        for s in self.sideSegments:
            f = f or (circle.checkColli(s))
        return f

class Circle:
    def __init__(self, canv, centerX, centerY, radius):
        self.particle = phys.Particle(pos = geo.Point(centerX, centerY))
        self.circle = canv.create_oval(centerX - radius, centerY - radius, centerX + radius, centerY + radius, state = "hidden")
        self.filledCircle = geo.FilledCircle(self.particle.pos.copy(), radius)
        self.canv = canv
        self.on = False
        self.colliPoints = []
        self.touching = []
    def __del__(self):
        self.canv.delete(self.circle)
    def move(self):
        if not self.on:
            self.particle.play()
            self.on = True
        self.particle.move()
        self.filledCircle.center = self.particle.pos.copy()
    def stop(self):
        if self.on:
            self.particle.pause()
            self.on = False
    def setv(self, vel):
        self.particle.setVel(vel)
    def setp(self, pos):
        self.particle.setPos(pos)
        self.filledCircle.center = self.particle.pos.copy()
    def resetColli(self):
        self.colliPoints = []
    def checkColli(self, obj):
        p = self.filledCircle.intersect(obj)
        if p != None:
            if not (obj in self.touching):
                self.colliPoints.append(p)
                self.touching.append(obj)
        else:
            if obj in self.touching:
                self.touching.remove(obj)
        return p
    def resolveColli(self):
        if self.colliPoints:
            self.particle.bounce(self.colliPoints)
            self.resetColli()
    def updateDrawing(self):
        self.canv.coords(self.circle, (self.filledCircle.center.x - self.filledCircle.radius, self.filledCircle.center.y - self.filledCircle.radius, self.filledCircle.center.x + self.filledCircle.radius, self.filledCircle.center.y + self.filledCircle.radius))
    def helpColli(self, circle):
        return circle.checkColli(self.filledCircle) != None
