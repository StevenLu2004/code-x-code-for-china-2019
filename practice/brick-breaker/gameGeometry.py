import math

class GameGeoTypeError(TypeError):
    """Game geometry type error"""

class Point:
    def __init__(self, x, y, z = 0):
        self.x = x
        self.y = y
        self.z = z
    def __add__(self, other):
        if type(other) == Vector:
            return Point(self.x + other.x, self.y + other.y, self.z + other.z)
        else:
            raise GameGeoTypeError("Second operand type not recognized")
    def __sub__(self, other):
        if type(other) == Point:
            return Vector(self.x - other.x, self.y - other.y, self.z + other.z)
        elif type(other) == Vector:
            return Point(self.x - other.x, self.y - other.y, self.z + other.z)
        else:
            raise GameGeoTypeError("Second operand type not recognized")

class Vector:
    def __init__(self, x, y, z = 0):
        self.x = x
        self.y = y
        self.z = z
    def __add__(self, other):
        if type(other) == Vector:
            return Point(self.x + other.x, self.y + other.y, self.z + other.z)
        else:
            raise GameGeoTypeError("Second operand type not recognized")
    def __sub__(self, other):
        if type(other) == Vector:
            return Point(self.x - other.x, self.y - other.y, self.z + other.z)
        else:
            raise GameGeoTypeError("Second operand type not recognized")
    @staticmethod
    def dotp(a, b):
        if type(a) == type(b) == Vector:
            return a.x * b.x + a.y * b.y + a.z * b.z
        else:
            raise GameGeoTypeError("Operand types not recognized")
    @staticmethod
    def crossp(a, b):
        if type(a) == type(b) == Vector:
            return Vector(a.y * b.z - a.z * b.y, a.z * b.x - a.x * b.z, a.x * b.y - a.y * b.x)
        else:
            raise GameGeoTypeError("Operand types not recognized")
    def abs(self):
        return math.sqrt(self.x * self.x + self.y * self.y + self.z * self.z)

class Line:
    class LineRelationships(Enum):
        ON_DIFFERENT_PLANES = 1
        CROSSING = 2
        PARALLEL = 3
        IDENTICAL = 4
    def __init__(self, p1, p2):
        if type(p1) == type(p2) == Point:
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
        if type(l1) == type(l2) == Line:
            v1 = Vector.crossp(l1.getVec(), l2.p1 - l1.p1)
            v2 = Vector.crossp(l1.getVec(), l2.p2 - l1.p1)
            if Vector.crossp(v1, v2).abs() != 0:
                return Line.LineRelationships.ON_DIFFERENT_PLANES
            elif Vector.crossp(l1.getVec(), l2.getVec()).abs() != 0:
                return Line.LineRelationships.CROSSING
            elif abs(l1.dist(l2.p1)) <= 1e-8:
                return Line.LineRelationships.PARALLEL
            else:
                return Line.LineRelationships.IDENTICAL
        else:
            raise GameGeoTypeError("Arguments provided are not lines.")

class LineSegment(Line):
    class LineRelationships(Enum):
        ON_DIFFERENT_PLANES = 1
        CROSSING = 2
        PARALLEL = 3
        OTHER = 4
    def __init__(self, p1, p2):
        super().__init__(self, p1, p2)
    @staticmethod
    def relationship(l1, l2):
        if type(l1) == type(l2) == LineSegment:
            v1 = Vector.crossp(l1.getVec(), l2.p1 - l1.p1)
            v2 = Vector.crossp(l1.getVec(), l2.p2 - l1.p1)
            if Vector.crossp(v1, v2).abs() != 0:
                return LineSegment.LineRelationships.ON_DIFFERENT_PLANES
            elif (v1 + v2).abs() < max(v1.abs(), v2.abs()):
                return LineSegment.LineRelationships.CROSSING
