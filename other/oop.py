from math import sqrt, pi


class Line:
    def __init__(self, coor1, coor2):
        self.coor1 = coor1
        self.coor2 = coor2

    @property
    def distance(self):
        x1, y1 = self.coor1
        x2, y2 = self.coor2
        return sqrt(((x2 - x1) ** 2) + ((y2 - y1) ** 2))

    @property
    def slope(self):
        x1, y1 = self.coor1
        x2, y2 = self.coor2
        return (y2 - y1) / (x2 - x1)


coordinate1 = (3, 2)
coordinate2 = (8, 10)

line1 = Line(coordinate1, coordinate2)
print(line1.distance)
print(line1.slope)


class Cylinder:
    """
    Create a cylinder object and assiciated values.

    param height: The height of the cylinder
    param radius: The redius of the cylinder
    """
    def __init__(self, height=1, radius=1):
        self.height = height
        self.radius = radius

    @property
    def volume(self):
        """
        Creates a calculated property of the volume of the cylinder.
        """
        return pi * self.radius ** 2 * self.height

    @property
    def surface_area(self):
        return (2 * pi * self.radius * self.height) + (2 * pi * self.radius ** 2)


cylinder1 = Cylinder(2, 2)
print(cylinder1.volume)
print(cylinder1.surface_area)
