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
        @return {int, float}
    """
    @staticmethod
    def _process(cir_val):
        while cir_val > .5:
            cir_val -= 1
        while cir_val <= -.5:
            cir_val += 1
        return cir_val
    """
        Process the value in the Angle instance using the Angle process method.
        @return {Angle}
        @see Angle._process(cir_val)
    """
    def process(self):
        self.__val = Angle._process(self.__val)
        return self
    """
        Class constructor for class Angle. Taking initial value and optionally the value mode.
        @param {int, float} val initial angle value
        @param {Angle.Mode} mode mode of the initial angle value
        @see Angle.process(self)
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
        @return {int, float}
    """
    def rad(self):
        return self.__val * 2 * math.pi
    """
        Return the size of the angle in degrees (DEG mode)
        @return {int, float}
    """
    def deg(self):
        return self.__val * 360
    """
        Return the size of the angle in circumference (CIR mode)
        @return {int, float}
    """
    def cir(self):
        return self.__val
    """
        Return the size of the angle in the default mode.
        @return {int, float}
        @see Angle.rad(self)
        @see Angle.deg(self)
        @see Angle.cir(self)
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
        @see Angle.process(self)
    """
    def setRad(self, val):
        self.__val = val / 2 / math.pi
        self.process()
    """
        Set the value of the angle via DEG mode
        @param {int, float} val new value of the angle in DEG mode
        @see Angle.process(self)
    """
    def setDeg(self, val):
        self.__val = val / 360
        self.process()
    """
        Set the value of the angle via CIR mode
        @param {int, float} val new value of the angle in CIR mode
        @see Angle.process(self)
    """
    def setCir(self, val):
        self.__val = val
        self.process()
    """
        Set the value of the angle via a mode given by the user (which defaults to defaultMode)
        @param {int, float} val new value in the user-given mode
        @param {Angle.Mode} mode mode of the new value given
        @see Angle.process(self)
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
        @return {str}
        @see Angle.get(self)
    """
    def __str__(self):
        return str(self.get()) + [" rad", "°", ""][Angle.defaultMode.value]
    """
        Shorthand function for using the constructor with RAD mode
        @param {int, float} val the initial value for the Angle object
        @return {Angle}
    """
    @staticmethod
    def Rad(val):
        return Angle(val, Angle.Mode.RAD)
    """
        Shorthand function for using the constructor with DEG mode
        @param {int, float} val the initial value for the Angle object
        @return {Angle}
    """
    @staticmethod
    def Deg(val):
        return Angle(val, Angle.Mode.DEG)
    """
        Shorthand function for using the constructor with CIR mode
        @param {int, float} val the initial value for the Angle object
        @return {Angle}
    """
    @staticmethod
    def Cir(val):
        return Angle(val, Angle.Mode.CIR)
    """
        Add two Angle objects regardless of mode and autoprocess the obtained value to fit in [-.5, .5) range in CIR mode.
        @param {Angle} other the other angle to be added
        @return {Angle}
    """
    def __add__(self, other):
        if isinstance(other, Angle):
            return Angle(self.__val + other.__val, Angle.Mode.CIR)
        else:
            raise GameGeoTypeError("Second operand should be an Angle but is {}".format(type(other)))
    """
        Subtract two Angle objects regardless of mode and autoprocess the obtained value to fit in [-.5, .5), CIR.
        @param {Angle} other the other angle to be subtracted
        @return {Angle}
    """
    def __sub__(self, other):
        if isinstance(other, Angle):
            return Angle(self.__val - other.__val, Angle.Mode.CIR)
        else:
            raise GameGeoTypeError("Second operand should be an Angle but is {}".format(type(other)))
    """
        Multiply an angle object and a number and autoprocess the result to fit in [-.5, .5), CIR.
        @param {Angle} other the number to be multiplied
        @return {Angle}
    """
    def __mul__(self, other):
        if isinstance(other, int) or isinstance(other, float):
            return Angle(self.__val * other, Angle.Mode.CIR)
        else:
            raise GameGeoTypeError("Second operand should be a number but is {}".format(type(other)))
    """
        Divide an angle object by a number and autoprocess the result to fit in [-.5, .5), CIR.
        @param {Angle} other the number serving as denominator
        @return {Angle}
    """
    def __div__(self, other):
        if isinstance(other, int) or isinstance(other, float):
            return Angle(self.__val / other, Angle.Mode.CIR)
        else:
            raise GameGeoTypeError("Second operand should be a number but is {}".format(type(other)))
    """
        Returns a copy of the current angle.
        @return {Angle}
    """
    def copy(self):
        return Angle(self.__val, Angle.Mode.CIR)

"""
    Point, supporting basic related calculations. May be optimized later.
"""
class Point:
    """
        Class constructor for class Point. Taking x, y, and optionally z coordinates
        @param {int, float} x x-coordinate of the point
        @param {int, float} y y-coordinate of the point
        @param {int, float} z z-coordinate of the point
    """
    def __init__(self, x, y, z = 0):
        self.x = x
        self.y = y
        self.z = z
    """
        Equal comparator for Point objects.
        @param {Point} other the other point object to be conpared with
        @return {bool}
    """
    def __eq__(self, other):
        if isinstance(other, Point):
            return self.x == other.x and self.y == other.y and self.z == other.z
        else:
            raise GameGeoTypeError("Second operand type is not Point")
    """
        Add a vector to a point.
        @param {Vector} other the vector to be added
        @return {Point}
    """
    def __add__(self, other):
        if isinstance(other, Vector):
            return Point(self.x + other.x, self.y + other.y, self.z + other.z)
        else:
            raise GameGeoTypeError("Second operand type not recognized")
    """
        Subtract a vector from a point.
        @param {Vector} other the vector to be subtracted
        @return {Point}
    """
    """
        Calculate the vector from the other point to the one.
        @param {Point} other the other point
        @return {Vector}
    """
    def __sub__(self, other):
        if isinstance(other, Point):
            return Vector(self.x - other.x, self.y - other.y, self.z + other.z)
        elif isinstance(other, Vector):
            return Point(self.x - other.x, self.y - other.y, self.z + other.z)
        else:
            raise GameGeoTypeError("Second operand type not recognized")
    """
        Calculate the distance between two points. Returns the length of the vector between them.
        @param {Point} a the first point
        @param {Point} b the second point
        @return {float}
        @see Vector.abs(self)
    """
    @staticmethod
    def dist(a, b):
        if isinstance(a, Point) and isinstance(b, Point):
            return (a - b).abs()
        else:
            raise GameGeoTypeError("Arguments are not points")
    """
        Judges whether a point is on a LineSegment.
        @param {LineSegment} container the container line segment
        @return {bool}
        @see Vector.crossp(a, b)
        @see Line.getVec(self)
        @see Vector.abs(self)
        @see Vector.dotp(a, b)
    """
    """
        Judges whether a point is on a Line.
        @param {Line} container the container line
        @return {bool}
        @see Vector.crossp(a, b)
        @see Line.getVec(self)
        @see Vector.abs(self)
    """
    """
        Judges whether a point is on a FilledCircle.
        @param {FilledCircle} container the container filled-circle
        @return {bool}
        @see Point.dist(a, b)
    """
    """
        Judges whether a point is on a Point (the same point).
        @param {Point} container the container point
        @return {bool}
        @see Point.__eq__(self, other)
    """
    def on(self, container):
        if isinstance(container, LineSegment):
            return (self == container.p1 or Vector.crossp(container.getVec(), self - container.p1).abs() == 0) and (Vector.dotp(container.p1 - self, container.p2 - self) <= 0)
        elif isinstance(container, Line):
            return (self == container.p1 or Vector.crossp(container.getVec(), self - container.p1).abs() == 0)
        elif isinstance(container, FilledCircle):
            return Point.dist(self, container.center) <= container.radius
        elif isinstance(container, Point):
            return self == container
        else:
            raise GameGeoTypeError("Container type not recognized")
    """
        Returns the xy-direction of the other point with respect to the one.
        @param {Point} other the other point
        @return {Angle}
        @see Vector.xy_direction(self)
    """
    def xy_direction(self, other):
        if isinstance(other, Point):
            return (other - self).xy_direction()
        else:
            raise GameGeoTypeError("The argument of xy_direction should be a point")
    """
        Returns the plane-z-direction of the other point with respect to the one
        @param {Point} other the other point
        @return {Angle}
        @see Vector.planez_direction(self)
    """
    def planez_direction(self, other):
        if isinstance(other, Point):
            return (other - self).planez_direction()
        else:
            raise GameGeoTypeError("The argument of planez_direction should be a point")
    """
        Expresses the point in a string as coordinates. Auto-trims to xy-coordinates if z is 0.
        @return {str}
    """
    def __str__(self):
        if self.z == 0:
            return "Point({:f}, {:f})".format(self.x, self.y)
        return "Point({:f}, {:f}, {:f})".format(self.x, self.y, self.z)
    """
        Converts a vector to a point.
        @return {Point}
    """
    @staticmethod
    def fromVector(vec):
        return Point(vec.x, vec.y, vec.z)
    """
        Returns a copy of the point.
        @return {Point}
    """
    def copy(self):
        return Point(self.x, self.y, self.z)

"""
    Vector, supporting basic related calculations. May be optimized later.
"""
class Vector:
    """
        Class constructor for class Vector. Taking x, y, and optionally z components.
        @param {int, float} x the x component
        @param {int, float} y the y component
        @param {int, float} z the z component
    """
    def __init__(self, x, y, z = 0):
        self.x = x
        self.y = y
        self.z = z
    """
        Adds the other vector to the one.
        @param {Vector} other the other vector
        @return {Vector}
    """
    def __add__(self, other):
        if isinstance(other, Vector):
            return Vector(self.x + other.x, self.y + other.y, self.z + other.z)
        else:
            raise GameGeoTypeError("Second operand type not recognized")
    """
        Gets the vector of same magnitude and opposite direction (i.e. negative vector).
        @return {Vector}
    """
    def __neg__(self):
        return Vector(-self.x, -self.y, -self.z)
    """
        Subtracts the other vector from the one.
        @param {Vector} other the other vector
        @return {Vector}
    """
    def __sub__(self, other):
        if isinstance(other, Vector):
            return Vector(self.x - other.x, self.y - other.y, self.z - other.z)
        else:
            raise GameGeoTypeError("Second operand type not recognized")
    """
        Multiplies the vector by a scalar.
        @param {int, float} other the scalar
        @return {Vector}
    """
    def __mul__(self, other):
        if isinstance(other, int) or isinstance(other, float):
            return Vector(self.x * other, self.y * other, self.z * other)
        else:
            raise GameGeoTypeError("Vector multiplied with unsupported type {}".format(type(other)))
    """
        Divides the vector by a scalar.
        @param {int, float} other the scalar
        @return {Vector}
    """
    def __div__(self, other):
        if isinstance(other, int) or isinstance(other, float):
            return Vector(self.x / other, self.y / other, self.z / other)
        else:
            raise GameGeoTypeError("Vector multiplied with unsupported type {}".format(type(other)))
    """
        Calculates the dot product of two vectors.
        @param {Vector} a the first vector
        @param {Vector} b the second vector
        @return {int, float}
    """
    @staticmethod
    def dotp(a, b):
        if isinstance(a, Vector) and isinstance(b, Vector):
            return a.x * b.x + a.y * b.y + a.z * b.z
        else:
            raise GameGeoTypeError("Operand types not recognized")
    """
        Calculates the cross product of two vectors.
        @param {Vector} a the first vector
        @param {Vector} b the second vector
        @return {Vector}
    """
    @staticmethod
    def crossp(a, b):
        if isinstance(a, Vector) and isinstance(b, Vector):
            return Vector(a.y * b.z - a.z * b.y, a.z * b.x - a.x * b.z, a.x * b.y - a.y * b.x)
        else:
            raise GameGeoTypeError("Operand types not recognized")
    """
        Calculates the modulus of the vector.
        @return {float}
    """
    def abs(self):
        return math.sqrt(self.x * self.x + self.y * self.y + self.z * self.z)
    """
        Calculates the unit vector along the direction of this vector.
        @return {Vector}
        @see Vector.abs(self)
    """
    def unit(self):
        sz = self.abs()
        return Vector(self.x / sz, self.y / sz, self.z / sz)
    """
        Expresses the other vector as a vector in a custom cartesian coordinate with +x-axis being the direction of this vector.
        @return {Vector}
        @see Vector.unit(self)
    """
    def xy_alignx(self, other):
        u = self.unit()
        c1 = complex(u.x, u.y)
        c2 = complex(other.x, other.y)
        c2prime = c2 / c1
        return Vector(c2prime.real, c2prime.imag, other.z)
    """
        Given the other vector as a vector in a custom cartesian coordinate with +x-axis being the direction of this vector, put it back.
        @return {Vector}
        @see Vector.unit(self)
    """
    def xy_restore(self, other):
        u = self.unit()
        c1 = complex(u.x, u.y)
        c2 = complex(other.x, other.y)
        c2prime = c2 * c1
        return Vector(c2prime.real, c2prime.imag, other.z)
    """
        Calculates the xy-direction of the vector.
        @return {Angle}
        @see Angle.Cir(val)
        @see Angle.Rad(val)
    """
    def xy_direction(self):
        if self.x == 0:
            return Angle.Cir(.25 if self.y >= 0 else -.25)
        else:
            return Angle.Rad(math.atan(self.y / self.x)) + (Angle.Cir(.5) if self.x < 0 else Angle.Cir(0))
    """
        Calculates the plane-z-direction of the vector.
        @return {Angle}
        @see Angle.Cir(val)
        @see Angle.Rad(val)
    """
    def planez_direction(self):
        planarLength = math.sqrt(self.x * self.x + self.y * self.y)
        if planarLength == 0:
            return Angle.Cir(.25 if self.z >= 0 else -.25)
        else:
            return Angle.Rad(math.atan(self.z / planarLength))
    """
        Expresses the vector in a string as components. Auto-trims to xy-coordinates if z is 0.
        @return {str}
    """
    def __str__(self):
        if self.z == 0:
            return "Vector({:f}, {:f})".format(self.x, self.y)
        return "Vector({:f}, {:f}, {:f})".format(self.x, self.y, self.z)
    """
        Converts a point to a vector.
        @return {Vector}
    """
    @staticmethod
    def fromPoint(pt):
        return Vector(pt.x, pt.y, pt.z)
    """
        Returns a copy of the vector.
        @return {Vector}
    """
    def copy(self):
        return Vector(self.x, self.y, self.z)

"""
    Line, supporting basic related calculations. May be optimized later.
"""
class Line:
    """
        Enumeration of line relationships. Includes non-coplanar, crossing, parallel and identical.
    """
    class LineRelationships(Enum):
        NON_COPLANAR = 1
        CROSSING = 2
        PARALLEL = 3
        IDENTICAL = 4
    """
        Class constructor for class Line. Taking two points on the line as arguments.
        @param {Point} p1 the first point
        @param {Point} p2 the second point
    """
    def __init__(self, p1, p2):
        if isinstance(p1, Point) and isinstance(p2, Point):
            self.p1 = p1
            self.p2 = p2
        else:
            raise GameGeoTypeError("Arguments provided are not points.")
    """
        Distance to a point.
        @param {Point} p the point
        @return {float}
        @see Vector.crossp(a, b)
        @see Vector.abs(self)
    """
    def dist(self, p):
        return Vector.crossp(p - self.p1, p - self.p2).abs() / (self.p2 - self.p1).abs()
    """
        Gets the vector from P1 on the line to P2.
        @return {Vector}
    """
    def getVec(self):
        return self.p2 - self.p1
    """
        Gets the relationship between two lines. Includes non-coplanar, crossing, parallel and identical.
        May be optimized later.
        @param {Line} l1 the first line
        @param {Line} l2 the second line
        @return {Line.LineRelationships}
        @see Vector.crossp(a, b)
        @see Line.getVec(self)
        @see Point.__sub__(self, other)
        @see Vector.abs(self)
        @see Line.dist(self, p)
    """
    @staticmethod
    def relationship(l1, l2):
        if isinstance(l1, Line) and isinstance(l2, Line):
            v1 = Vector.crossp(l1.getVec(), l2.p1 - l1.p1)
            v2 = Vector.crossp(l1.getVec(), l2.p2 - l1.p1)
            if Vector.crossp(v1, v2).abs() != 0:
                return Line.LineRelationships.NON_COPLANAR
            elif Vector.crossp(l1.getVec(), l2.getVec()).abs() != 0:
                return Line.LineRelationships.CROSSING
            elif l1.dist(l2.p1) > 0:
                return Line.LineRelationships.PARALLEL
            else:
                return Line.LineRelationships.IDENTICAL
        else:
            raise GameGeoTypeError("Arguments provided are not lines.")
    """
        Calculates the intersection between two lines. Returns a point only when lines are crossing.
        May be optimized later.
        @param {Line} l1 the first line
        @param {Line} l2 the second line
        @return {Point, None}
        @see Line.relationship(l1, l2)
        @see Vector.dotp(a, b)
        @see Vector.crossp(a, b)
    """
    @staticmethod
    def _intersection(l1, l2):
        if isinstance(l1, Line) and isinstance(l2, Line):
            if Line.relationship(l1, l2) != Line.LineRelationships.CROSSING:
                return None
            else:
                a = l1.p2 - l1.p1
                b = l2.p2 - l2.p1
                c = l2.p1 - l1.p1
                x = l1.p1 + a * (Vector.dotp(Vector.crossp(c, b), Vector.crossp(a, b)) / (Vector.crossp(a, b).abs() ** 2))
                return x
        else:
            raise GameGeoTypeError("Arguments provided are not lines.")
    """
        Calculates the intersection between this line and another using Line._intersection()
        May be optimized later.
        @param {Line} other the other line
        @return {Point, None}
        @see Line._intersection(l1, l2)
    """
    def intersection(self, other):
        return Line._intersection(self, other)
    """
        Calculates the perpendicular point from a point to this line.
        @param {Point} pt the point
        @return {Point}
        @see Vector.dotp(a, b)
        @see Point.__sub__(self, other)
        @see Line.getVec(self)
        @see Point.fromVector(vec)
        @see Vector.fromPoint(pt)
        @see Vector.__mul__(self, other)
        @see Vector.__add__(self, other)
    """
    def perpendicularP(self, pt):
        if isinstance(pt, Point):
            a = Vector.dotp(self.p2 - pt, self.getVec())
            b = -Vector.dotp(self.p1 - pt, self.getVec())
            return Point.fromVector(Vector.fromPoint(self.p1) * a + Vector.fromPoint(self.p2) * b)
        else:
            raise GameGeoTypeError("Argument for Line.perpendicularP has to be a Point.")
    """
        Expresses the line as a set of two points.
        @return {str}
        @see Point.__str__(self)
    """
    def __str__(self):
        return "Line({}, {})".format(self.p1, self.p2)
    """
        Returns a copy of the line.
        @return {Line}
        @see Point.copy(self)
    """
    def copy(self):
        return Line(self.p1.copy(), self.p2.copy())

"""
    Line segment, supporting basic related calculations. May be optimized later.
"""
class LineSegment(Line):
    """
        Enumeration of line relationships. Includes non-coplanar, crossing, parallel, same-line and other.
    """
    class LineRelationships(Enum):
        NON_COPLANAR = 1
        CROSSING = 2
        PARALLEL = 3
        SAME_LINE = 4
        OTHER = 5
    """
        Class constructor for class LineSegment. Taking two points on the line as arguments.
        @param {Point} p1 the first point
        @param {Point} p2 the second point
        @see Line.__init__(self, p1, p2)
    """
    def __init__(self, p1, p2):
        super().__init__(self, p1, p2)
    """
        Gets the relationship between two line segments. Includes non-coplanar, crossing, parallel, same-line and other.
        May be optimized later.
        @param {Line} l1 the first line
        @param {Line} l2 the second line
        @return {Line.LineRelationships}
        @see Vector.crossp(a, b)
        @see Line.getVec(self)
        @see Point.__sub__(self, other)
        @see Vector.abs(self)
        @see Vector.__add__(self, other)
        @see Line.dist(self, p)
    """
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
            elif l1.dist(l2.p1) > 0:
                return LineSegment.LineRelationships.PARALLEL
            else:
                return LineSegment.LineRelationships.SAME_LINE
        else:
            raise GameGeoTypeError("Arguments provided are not lines.")
    """
        Expresses the line segment as a set of two end points.
        @return {str}
        @see Point.__str__(self)
    """
    def __str__(self):
        return "LineSegment({}, {})".format(self.p1, self.p2)
    """
        Returns a copy of the line segment.
        @return {LineSegment}
        @see Point.copy()
    """
    def copy(self):
        return LineSegment(self.p1.copy(), self.p2.copy())

"""
    Filled circle, supporting basic related calculations. May be optimized later.
"""
class FilledCircle:
    """
        Class constructor for class FilledCircle. Takes the center (point) and the radius (number) as arguments.
        @param {Point} center the center of the filled circle
        @param {int, float} radius the radius of the filled circle
    """
    def __init__(self, center, radius):
        self.center = center
        self.radius = radius
    """
        Get the point at which the filled circle and an object is intersecting.
        Will return the closest points feasible. Will return the perpendicular point if intersecting with a line / line segment.
        @param {LineSegment, Line, FilledCircle, Point} obj the object
        @return {Point}
        @see Line.dist(self, p)
        @see Point.on(self, container)
        @see Point.__eq__(self, other)
        @see Point.dist(a, b)
        @see Point.fromVector(vec)
        @see Vector.fromPoint(pt)
        @see Vector.__mul__(self, other)
        @see Vector.__add__(self, other)
        @see Line.perpendicularP(self, pt)
        @see Point.__add__(self, other)
        @see Point.__sub__(self, other)
    """
    def intersect(self, obj):
        if isinstance(obj, LineSegment):
            # If the line doesn't even intersect with the circle
            if obj.dist(self.center) > self.radius:
                return None
            # If at least one point of the segment is in the circle
            if obj.p1.on(self) and obj.p2.on(self):
                if obj.p1 == obj.p2:
                    return obj.p1
                d1 = Point.dist(obj.p1, self.center)
                d2 = Point.dist(obj.p2, self.center)
                return Point.fromVector(Vector.fromPoint(obj.p1) * (d2 / (d1 + d2)) + Vector.fromPoint(obj.p2) * (d1 / (d1 + d2)))
            # Both points are out
            footp = obj.perpendicularP(self.center)
            return footp if footp.on(obj) else None
        elif isinstance(obj, Line):
            if obj.dist(self.center) <= self.radius:
                footp = obj.perpendicularP(self.center)
                return footp if footp.on(obj) else None
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
    """
        Expresses the filled circle as a center point and a radius.
        @return {str}
        @see Point.__str__(self)
    """
    def __str__(self):
        return "Circle({}, {:f})".format(self.center, self.radius)
    """
        Returns a copy of the filled circle.
        @return {FilledCircle}
        @see Point.copy(self)
    """
    def copy(self):
        return FilledCircle(self.center.copy(), self.radius)

"""
    Empty main function that will be called only if this module is the entry point.
"""
def main():
    pass

if __name__ == "__main__":
    main()
