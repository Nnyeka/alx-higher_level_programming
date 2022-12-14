#!/usr/bin/python3
"""Defines a Rectangle class."""

class Rectangle:
    """Represents a rectangle."""

    def __init__(self, width=0, height=0):
        """initializes a new Rectangle.

        Args:
            width (int): The width of the object rectangle.
            height (int): The height of the object rectangle.
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """Get and set private width of the rectangle."""
        return self.__width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Get and set private width of the rectangle."""
        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value
        
    def area(self):
        """returns the rectangle area"""
        return (self.__width * self.__height)
        
    def perimeter(self):
        """Method that returns the rectangle perimeter"""
        if self.__width == 0 or self.__height == 0:
            return (0)
        return ((self.__width * 2) + (self.__height * 2))
    
    def __str__(self):
        """Method that returns the printable representation of the rectangle.
        prints the rectangle with the # character
        """
        if self.__width == 0 or self.__height == 0:
            return ("")
        
        rectangle = []
        for i in range(self.__height):
            [rectangle.append('#') for j in range(self.__width)]
            if i != self.__height - 1:
                rectangle.append('\n')
        return ("".join(rectangle))
