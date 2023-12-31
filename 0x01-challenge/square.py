#!/usr/bin/python3
"""module to print a square
"""


class Square():
    """prints a square
    """

    width = 0
    height = 0

    def __init__(self, *args, **kwargs):
        """initialise self
        """

        for key, value in kwargs.items():
            setattr(self, key, value)

    def area_of_my_square(self):
        """area of the square
        """

        return self.width * self.height

    def permiter_of_my_square(self):
        """perimeter of the square
        """

        return (self.width * 2) + (self.height * 2)

    def __str__(self):
        """string representation of the width and height of the square
        """

        return "{}/{}".format(self.width, self.height)


if __name__ == "__main__":
    """wrapper line
    """

    s = Square(width=12, height=9)
    print(s)
    print(s.area_of_my_square())
    print(s.permiter_of_my_square())
