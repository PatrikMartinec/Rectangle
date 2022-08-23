class Rect:
    def __init__(self, x1, y1, x2, y2):
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2

    def __repr__(self):
        return f'Rect({self.x1},{self.y1},{self.x2},{self.y2})'

    def perimeter(self):
        return 2 * (self.x2 - self.x1) + 2 * (self.y2 - self.y1)

    def area(self):
        return (self.x2 - self.x1) * (self.y2 - self.y1)

    def __eq__(self, other):
        return (self.x1 == other.x1 and self.y1 == other.y1 and
                self.x2 == other.x2 and self.y2 == other.y2)

    def __contains__(self, other):
        rect1, rect2 = self, other

        # check if the rectangle is a line, the line cannot contain a rectangle
        if (rect1.x1 == rect1.x2 or rect1.y1 == rect1.y2 or
            rect2.x1 == rect2.x2 or rect2.y1 == rect2.y2):
            return False

        # check if the one rectangle is on the left of the other and vice versa
        elif rect2.x1 >= rect1.x2 or rect1.x1 >= rect2.x2:
            return False

        # check if the one rectangle is above of the other and vice versa
        elif rect2.y1 >= rect1.y2 or rect1.y1 >= rect2.y2:
            return False

        else:
            return True

    def __and__(self, other):
        rect1, rect2 = self, other

        # points of the intersection triangle
        x1 = max(rect1.x1, rect2.x1)
        y1 = max(rect1.y1, rect2.y1)

        x2 = min(rect1.x2, rect2.x2)
        y2 = min(rect1.y2, rect2.y2)

        # no intersection
        if x1 >= x2 or y1 >= y2:
            return Rect(0, 0, 0, 0)

        return Rect(x1, y1, x2, y2)
