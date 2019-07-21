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
        canv.delete(self.rect)
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
        self.particle = phys.Particle(pos = geo.Point(gVars.windowDm[0] / 2, gVars.windowDm[1] / 2))
        self.circle = canv.create_oval(centerX - radius, centerY - radius, centerX + radius, centerY + radius, state = "hidden")
        self.filledCircle = geo.FilledCircle(self.particle.pos, radius)
        self.canv = canv
        self.on = False
        self.colliPoints = []
    def __del__(self):
        canv.delete(self.circle)
    def move(self):
        if not self.on:
            self.particle.play()
            self.on = True
        self.particle.move()
        self.filledCircle.center = self.particle.pos.copy()
    def setv(self, vel):
        self.particle.setVel(vel)
    def resetColli(self):
        self.colliPoints = []
    def checkColli(self, obj):
        p = self.filledCircle.intersect(obj)
        if p != None:
            self.colliPoints.append(p)
        return p
    def resolveColli(self):
        if self.colliPoints:
            self.particle.bounce(self.colliPoints)
            self.resetColli()
    def updateDrawing(self):
        self.canv.coords(self.circle, (self.filledCircle.center.x - self.filledCircle.radius, self.filledCircle.center.y - self.filledCircle.radius, self.filledCircle.center.x + self.filledCircle.radius, self.filledCircle.center.y + self.filledCircle.radius))
