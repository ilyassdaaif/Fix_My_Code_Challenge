#!/usr/bin/python3

class Square():
    def __init__(self, side_length=0):
        self.side_length = side_length

    def area(self):
        """ Calculate the area of the square """
        return self.side_length ** 2

    def perimeter(self):
        """ Calculate the perimeter of the square """
        return 4 * salf.side_length

    def __str__(self):
        return "{} by {}".format(self.side_length, self.side_length)

if __name__ == "__main__":
    sq = Square(side_length=12)
    print(sq)
    print(f"Area: {sq.area()}")
    print(f"Perimeter: {sq.perimeter()}")
