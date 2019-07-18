import tkinter as TK

class Rectangle:
    def __init__(self, canv, centerX, centerY, width, height):
        self.rect = canv.create_rectangle(centerX - width / 2, centerY - height / 2, centerX + width / 2, centerY + height / 2)
