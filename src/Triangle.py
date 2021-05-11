import numpy as np

class Triangle(object):
    def __init__(self, a, b, c, color):
        self.a = a # a point
        self.b = b # b point
        self.c = c # c point
        self.color = color
        self.u = self.b - self.a #direction vector
        self.v = self.c - self.a #direction vector

    def __repr__(self):
        return "Triangle(%s,%s,%s)" %(repr(self.a), repr(self.b), repr(self.c))

    def intersectionParameter(self, ray):
        w = ray.origin - self.a
        dv = np.cross(ray.direction, self.v)
        #dv = ray.direction.cross(self.v)
        dvu = dv.dot(self.u)
        if dvu == 0.0:
            return None
        wu = np.cross(w, self.u)
        #wu = w.cross(self.u)
        r = dv.dot(w) / dvu
        s = wu.dot(ray.direction) / dvu
        if 0<=r and r<=1 and 0<=s and s<=1 and r+s<=1:
            return wu.dot(self.v) / dvu
        else:
            return None

    def normalAt(self, p):
        return self.normalized(self.u.cross(self.v))

    def normalized(self, p):
        vecLength = np.sqrt(p.dot(p))
        return np.array(p/vecLength)

    def colorAt(self, ray):
        return self.color.getColor()