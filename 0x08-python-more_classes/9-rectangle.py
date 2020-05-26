#!/usr/bin/python3
"""[Defines Class rectangle]"""


class Rectangle:
    """[Class Rectangle]

    Raises:
        TypeError: [width must be an integer]
        ValueError: [width must be >= 0]
        TypeError: [height must be an integer]
        ValueError: [height must be >= 0]

    Returns:
        [int] -- [width or height of rectangle ]
    """
    number_of_instances = 0
    print_symbol = '#'

    def __init__(self, width=0, height=0):
        """[initializes rectangle]

        Keyword Arguments:
            width {int} -- [rectangle width] (default: {0})
            heigth {int} -- [rectangle height] (default: {0})
        """
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

    @property
    def width(self):
        """[Gets the width of the rectangle]

        Returns:
            [int] -- [width of the rectangle]
        """
        return self.__width

    @width.setter
    def width(self, value):
        """[Sets the width of the rectangle]

        Arguments:
            value {[int]} -- [New size for width]

        Raises:
            TypeError: [width must be an integer]
            ValueError: [width must be >= 0]
        """
        if type(value) is not int:
            raise TypeError('width must be an integer')
        if value < 0:
            raise ValueError('width must be >= 0')
        self.__width = value

    @property
    def height(self):
        """[Gets the height of the rectangle]

        Returns:
            [int] -- [height of the rectangle]
        """
        return self.__height

    @height.setter
    def height(self, value):
        """[Sets the height of the rectangle]

        Arguments:
            value {[int]} -- [New size for height]

        Raises:
            TypeError: [height must be an integer]
            ValueError: [height must be >= 0]
        """
        if type(value) is not int:
            raise TypeError('height must be an integer')
        if value < 0:
            raise ValueError('height must be >= 0')
        self.__height = value

    def area(self):
        """[Defines the area of ​​a triangle]

        Returns:
            [int] -- [triangle area]
        """
        return self.__width * self.__height

    def perimeter(self):
        """[Defines the perimeter of a triangle]

        Returns:
            [type] -- [triangle perimeter]
        """
        if self.__width == 0 or self.__height == 0:
            return 0
        return 2 * (self.__height + self.__width)

    def __str__(self):
        """
        [print the rectangle with the character print_symbol variable]

        Returns:
            [string] -- [text string containing the triangle representation]
        """
        string = ''

        if self.width == 0 or self.height == 0:
            return string
        for count in range(self.height):
            string += str(self.print_symbol) * self.width
            if count < self.height - 1:
                string += '\n'
        return string

    def __repr__(self):
        """
        Returns:
            [str] -- ['official' version of rectangle]
        """
        return 'Rectangle({}, {})'.format(self.width, self.height)

    def __del__(self):
        """[prints a message when an instance is deleted]
        """
        print('Bye rectangle...')
        Rectangle.number_of_instances -= 1

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """[compare the area of ​​2 rectangles]

        Arguments:
            rect_1 {[Rectangle]} -- [rectangle 1]
            rect_2 {[Rectangle]} -- [rectangle 2]

        Raises:
            TypeError: [if type(rect_1) is not Rectangle]
            TypeError: [if type(rect_2) is not Rectangle]

        Returns:
            [Rectangle] -- [rect_1 if both have the same area value]
        """
        if type(rect_1) is not Rectangle:
            raise TypeError('rect_1 must be an instance of Rectangle')

        if type(rect_2) is not Rectangle:
            raise TypeError('rect_2 must be an instance of Rectangle')

        return rect_1 if rect_1.area() >= rect_2.area() else False

    @classmethod
    def square(cls, size=0):
        """[use the Rectangle class to create a square]

        Keyword Arguments:
            size {int} -- [size for the square] (default: {0})

        Returns:
            [ectangle] -- [square]
        """
        new_rect = Rectangle()

        new_rect.width = size
        new_rect.height = size

        return new_rect
