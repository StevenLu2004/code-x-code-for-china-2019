import math
from enum import Enum

class GameGeoTypeError(TypeError):
    """Game geometry type error"""

"""
    Angle supports storage and calculation of angles in all forms.
"""
class Angle:
    """
        Mode of angle input/output. Will NOT affect the sorage type.
    """
    class Mode(Enum):
        RAD = 0
        DEG = 1
        CIR = 2
    defaultMode = Mode.RAD
    """
        Input an angle in CIR mode and get another one within [-.5, .5) in CIR
        @param {int, float} cir_val value in CIR mode
    """
    @staticmethod
    def process(cir_val):
        while cir_val > .5:
            cir_val -= 1
        while cir_val <= -.5:
            cir_val += 1
        return cir_val
    """
        Process the value in the Angle instance using the Angle process method.
    """
    def process(self):
        self.__angle = Angle.process(self.__angle)
        return self
    """
        Class constructor taking initial value and optionally the value mode.
        @param {int, float} val initial angle value
        @param {Angle.Mode} mode mode of the initial angle value
    """
    def __init__(self, val, mode = defaultMode):
        if mode == Angle.Mode.RAD:
            self.__val = val / 2 / math.pi
        elif mode == Angle.Mode.DEG:
            self.__val = val / 360
        elif mode == Angle.Mode.CIR:
            self.__val = val
        else:
            raise GameGeoTypeError("Angle mode is unknown")
        self.process()
    """
        Return the size of the angle in radians (RAD mode)
    """
    def rad(self):
        return self.__val * 2 * math.pi
    """
        Return the size of the angle in degrees (DEG mode)
    """
    def deg(self):
        return self.__val * 360
    """
        Return the size of the angle in circumference (CIR mode)
    """
    def cir(self):
        return self.__val
    """
        Return the size of the angle in the default mode.
    """
    def get(self):
        if Angle.defaultMode == Angle.Mode.RAD:
            return self.rad()
        elif Angle.defaultMode == Angle.Mode.DEG:
            return self.deg()
        elif Angle.defaultMode == Angle.Mode.CIR:
            return self.cir()
        else:
            raise GameGeoTypeError("Default angle type is unknown")
    """
        Set the value of the angle via RAD mode
        @param {int, float} val new value of the angle in RAD mode
    """
    def setRad(self, val):
        self.__val = val / 2 / math.pi
        self.process()
    """
        Set the value of the angle via DEG mode
        @param {int, float} val new value of the angle in DEG mode
    """
    def setDeg(self, val):
        self.__val = val / 360
        self.process()
    """
        Set the value of the angle via CIR mode
        @param {int, float} val new value of the angle in CIR mode
    """
    def setCir(self, val):
        self.__val = val
        self.process()
    """
        Set the value of the angle via a mode given by the user (which defaults to defaultMode)
        @param {int, float} val new value in the user-given mode
        @param {Angle.Mode} mode mode of the new value given
    """
    def set(self, val, mode = defaultMode):
        if mode == Angle.Mode.RAD:
            self.__val = val / 2 / math.pi
        elif mode == Angle.Mode.DEG:
            self.__val = val / 360
        elif mode == Angle.Mode.CIR:
            self.__val = val
        else:
            raise GameGeoTypeError("Angle mode is unknown")
        self.process()
    """
        Expresses the value of the angle as a string using the defaultMode
    """
    def __str__(self):
        return str(self.get()) + [" rad", "°", ""][Angle.defaultMode.value]
    """
        Shorthand function for using the constructor with RAD mode
        @param {int, float} val the initial value for the Angle object
    """
    @staticmethod
    def Rad(val):
        return Angle(val, Angle.Mode.RAD)
    """
        Shorthand function for using the constructor with DEG mode
        @param {int, float} val the initial value for the Angle object
    """
    @staticmethod
    def Deg(val):
        return Angle(val, Angle.Mode.DEG)
    """
        Shorthand function for using the constructor with CIR mode
        @param {int, float} val the initial value for the Angle object
    """
    @staticmethod
    def Cir(val):
        return Angle(val, Angle.Mode.CIR)
    """
        Add two Angle objects regardless of mode and autoprocess the obtained value to fit in [-.5, .5) range in CIR mode.
        @param {Angle} other the other angle to be added
    """
    def __add__(self, other):
        if isinstance(other, Angle):
            return Angle(self.val + other.val, Angle.Mode.CIR)
        else:
            raise GameGeoTypeError("Second operand should be an Angle but is {}".format(type(other)))
    """
        Subtract two Angle objects regardless of mode and autoprocess the obtained value to fit in [-.5, .5), CIR.
        @param {Angle} other the other angle to be subtracted
    """
    def __sub__(self, other):
        if isinstance(other, Angle):
            return Angle(self.val - other.val, Angle.Mode.CIR)
        else:
            raise GameGeoTypeError("Second operand should be an Angle but is {}".format(type(other)))
    """
        Multiply an angle object and a number and autoprocess the result to fit in [-.5, .5), CIR.
        @param {Angle} other the number to be multiplied
    """
    def __mul__(self, other):
        if isinstance(other, int) or isinstance(other, float):
            return Angle(self.val * other, Angle.Mode.CIR)
        else:
            raise GameGeoTypeError("Second operand should be a number but is {}".format(type(other)))
    """
        Divide an angle object by a number and autoprocess the result to fit in [-.5, .5), CIR.
        @param {Angle} other the number serving as denominator
    """
    def __div__(self, other):
        if isinstance(other, int) or isinstance(other, float):
            return Angle(self.val / other, Angle.Mode.CIR)
        else:
            raise GameGeoTypeError("Second operand should be a number but is {}".format(type(other)))

"""
    Point, supporting basic related calculations. May be optimized later.
"""
class Point:
    def __init__(self, x, y, z = 0):
        self.x = x
        self.y = y
        self.z = z
    def __eq__(self, other):
        if isinstance(other, Point):
            return self.x == other.x and self.y == other.y and self.z == other.z
        else:
            raise GameGeoTypeError("Second operand type is not Point")
    def __add__(self, other):
        if isinstance(other, Vector):
            return Point(self.x + other.x, self.y + other.y, self.z + other.z)
        else:
            raise GameGeoTypeError("Second operand type not recognized")
    def __sub__(self, other):
        if isinstance(other, Point):
            return Vector(self.x - other.x, self.y - other.y, self.z + other.z)
        elif isinstance(other, Vector):
            return Point(self.x - other.x, self.y - other.y, self.z + other.z)
        else:
            raise GameGeoTypeError("Second operand type not recognized")
    @staticmethod
    def dist(a, b):
        if isinstance(a, Point) and isinstance(b, Point):
            return (a - b).abs()
        else:
            raise GameGeoTypeError("Arguments are not points")
    def on(self, container):
        if isinstance(container, LineSegment):
            return (self == container.p1 or Vector.crossp(container.getVec(), self - container.p1).abs() == 0) and (Vector.dotp(container.p1 - self, container.p2 - self) <= 0)
        elif isinstance(container, FilledCircle):
            return Point.dist(self, container.center) <= container.radius
        elif isinstance(container, Point):
            return self == container
        else:
            raise GameGeoTypeError("Container type not recognized")
    def xy_direction(self, other):
        if isinstance(other, Point):
            if self.x == other.x:
                a = Angle.Cir(.25 if other.y > self.y else -.25)
            else:
                a = Angle.Rad(math.atan((other.y - self.y) / (other.x - self.x))) + (Angle.Cir(.5) if other.x - self.x < 0 else Angle.Cir(0))
            return a
        else:
            raise GameGeoTypeError("The argument of xy_direction should be a point")
    def __str__(self):
        if self.z == 0:
            return "Point({:.4f}, {:.4f})".format(self.x, self.y)
        return "Point({:.4f}, {:.4f}, {:.4f})".format(self.x, self.y, self.z)

class Vector:
    def __init__(self, x, y, z = 0):
        self.x = x
        self.y = y
        self.z = z
    def __add__(self, other):
        if isinstance(other, Vector):
            return Vector(self.x + other.x, self.y + other.y, self.z + other.z)
        else:
            raise GameGeoTypeError("Second operand type not recognized")
    def __sub__(self, other):
        if isinstance(other, Vector):
            return Vector(self.x - other.x, self.y - other.y, self.z + other.z)
        else:
            raise GameGeoTypeError("Second operand type not recognized")
    def __mul__(self, other):
        if isinstance(other, int) or isinstance(other, float):
            return Vector(self.x * other, self.y * other, self.z * other)
        else:
            raise GameGeoTypeError("Vector multiplied with unsupported type {}".format(type(other)))
    @staticmethod
    def dotp(a, b):
        if isinstance(a, Vector) and isinstance(b, Vector):
            return a.x * b.x + a.y * b.y + a.z * b.z
        else:
            raise GameGeoTypeError("Operand types not recognized")
    @staticmethod
    def crossp(a, b):
        if isinstance(a, Vector) and isinstance(b, Vector):
            return Vector(a.y * b.z - a.z * b.y, a.z * b.x - a.x * b.z, a.x * b.y - a.y * b.x)
        else:
            raise GameGeoTypeError("Operand types not recognized")
    def abs(self):
        return math.sqrt(self.x * self.x + self.y * self.y + self.z * self.z)
    def __str__(self):
        if self.z == 0:
            return "Vector({:.4f}, {:.4f})".format(self.x, self.y)
        return "Vector({:.4f}, {:.4f}, {:.4f})".format(self.x, self.y, self.z)

class Line:
    class LineRelationships(Enum):
        NON_COPLANAR = 1
        CROSSING = 2
        PARALLEL = 3
        IDENTICAL = 4
    def __init__(self, p1, p2):
        if isinstance(p1, Point) and isinstance(p2, Point):
            self.p1 = p1
            self.p2 = p2
        else:
            raise GameGeoTypeError("Arguments provided are not points.")
    def dist(self, p):
        return Vector.crossp(p - p1, p - p2).abs() / (p2 - p1).abs()
    def getVec(self):
        return self.p2 - self.p1
    @staticmethod
    def relationship(l1, l2):
        if isinstance(l1, Line) and isinstance(l2, Line):
            v1 = Vector.crossp(l1.getVec(), l2.p1 - l1.p1)
            v2 = Vector.crossp(l1.getVec(), l2.p2 - l1.p1)
            if Vector.crossp(v1, v2).abs() != 0:
                return Line.LineRelationships.NON_COPLANAR
            elif Vector.crossp(l1.getVec(), l2.getVec()).abs() != 0:
                return Line.LineRelationships.CROSSING
            elif abs(l1.dist(l2.p1)) > 0:
                return Line.LineRelationships.PARALLEL
            else:
                return Line.LineRelationships.IDENTICAL
        else:
            raise GameGeoTypeError("Arguments provided are not lines.")
    @staticmethod
    def intersection(l1, l2):
        if isinstance(l1, Line) and isinstance(l2, Line):
            if Line.relationship(l1, l2) != Line.LineRelationships.CROSSING:
                return None
            else:
                a = l1.p2 - l1.p1
                b = l2.p2 - l2.p1
                c = l2.p1 - l1.p1
                x = l1.p1 + a * (Vector.dotp(Vector.crossp(c, b), Vector.crossp(a, b)) / (Vector.crossp(a, b) ** 2))
                return x
        else:
            raise GameGeoTypeError("Arguments provided are not lines.")
    def intersection(self, other):
        return Line.intersection(self, other)
    def __str__(self):
        return "Line({}, {})".format(self.p1, self.p2)

class LineSegment(Line):
    class LineRelationships(Enum):
        NON_COPLANAR = 1
        CROSSING = 2
        PARALLEL = 3
        SAME_LINE = 4
        OTHER = 5
    def __init__(self, p1, p2):
        super().__init__(self, p1, p2)
    @staticmethod
    def relationship(l1, l2):
        if isinstance(l1, LineSegment) and isinstance(l2, LineSegment):
            v1 = Vector.crossp(l1.getVec(), l2.p1 - l1.p1)
            v2 = Vector.crossp(l1.getVec(), l2.p2 - l1.p1)
            if Vector.crossp(v1, v2).abs() != 0:
                return LineSegment.LineRelationships.NON_COPLANAR
            elif Vector.crossp(l1.getVec(), l2.getVec()).abs() != 0:
                v3 = Vector.crossp(l2.getVec(), l1.p1 - l2.p1)
                v4 = Vector.crossp(l2.getVec(), l1.p2 - l2.p1)
                f_1thru2 = ((v1 + v2).abs() < max(v1.abs(), v2.abs())) or v1.abs() == 0 or v2.abs() == 0
                f_2thru1 = ((v3 + v4).abs() < max(v3.abs(), v4.abs())) or v3.abs() == 0 or v4.abs() == 0
                if f_1thru2 and f_2thru1:
                    return LineSegment.LineRelationships.CROSSING
                else:
                    return LineSegment.LineRelationships.OTHER
            elif abs(l1.dist(l2.p1)) > 0:
                return LineSegment.LineRelationships.PARALLEL
            else:
                return LineSegment.LineRelationships.SAME_LINE
        else:
            raise GameGeoTypeError("Arguments provided are not lines.")
    def __str__(self):
        return "LineSegment({}, {})".format(self.p1, self.p2)

class FilledCircle:
    def __init__(self, center, radius):
        self.center = center
        self.radius = radius
    def intersect(self, obj):
        if isinstance(obj, LineSegment):
            # If the line doesn't even intersect with the circle
            if obj.dist(self.center) > self.radius:
                return None
            # If at least one point of the segment is in the circle
            if obj.p1.on(self) and obj.p2.on(self):
                # p = (Vector(obj.p1.x, obj.p1.y, obj.p1.z) + Vector(obj.p2.x, obj.p2.y, obj.p2.z)) * 0.5
                # p = Point(p.x, p.y, p.z)
                pass # Do nothing
            # Both points are out
            a = Vector.dotp(obj.p1 - self.center, obj.getVec())
            b = -Vector.dotp(obj.p2 - self.center, obj.getVec())
            footp = a * Vector(obj.p1.x, obj.p1.y, obj.p1.z) + b * Vector(obj.p2.x, obj.p2.y, obj.p2.z)
            footp = Point(footp.x, footp.y, footp.z)
            return footp.on(obj)
        elif isinstance(obj, Line):
            if obj.dist(self.center) > self.radius:
                a = Vector.dotp(obj.p1 - self.center, obj.getVec())
                b = -Vector.dotp(obj.p2 - self.center, obj.getVec())
                footp = a * Vector(obj.p1.x, obj.p1.y, obj.p1.z) + b * Vector(obj.p2.x, obj.p2.y, obj.p2.z)
                footp = Point(footp.x, footp.y, footp.z)
                return footp.on(obj)
            else:
                return None
        elif isinstance(obj, FilledCircle):
            d = Point.dist(self.center, obj.center)
            if self.radius + obj.radius >= d:
                return self.center + (obj.center - self.center) * ((d - obj.radius) / d)
            else:
                return None
        elif isinstance(obj, Point):
            return obj if self.radius >= Point.dist(self.center, obj) else None
    def __str__(self):
        return "Circle({}, {:.4f})".format(self.center, self.radius)

def main():
    pass

if __name__ == "__main__":
    main()
