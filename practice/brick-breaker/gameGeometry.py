import math

class GameGeoTypeError(TypeError):
    """Game geometry type error"""

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

class FilledCircle:
    def __init__(self, center, radius):
        self.center = center
        self.radius = radius
    def intersect(self, obj):
        if isinstance(obj, LineSegment):
            # If the line doesn't even intersect with the circle
            if obj.dist(self.center) > self.radius:
                return False
            # If at least one point of the segment is in the circle
            if obj.p1.on(self) or obj.p2.on(self):
                return True
            # Both points are out
            a = Vector.dotp(obj.p1 - self.center, obj.getVec())
            b = -Vector.dotp(obj.p2 - self.center, obj.getVec())
            footp = a * Vector(obj.p1.x, obj.p1.y, obj.p1.z) + b * Vector(obj.p2.x, obj.p2.y, obj.p2.z)
            footp = Point(footp.x, footp.y, footp.z)
            return footp.on(obj)
        elif isinstance(obj, Line):
            return obj.dist(self.center) > self.radius
        elif isinstance(obj, FilledCircle):
            return self.radius + obj.radius >= Point.dist(self.center, obj.center)

def main():
    while True:
        print(eval(input))

if __name__ == "__main__":
    main()
