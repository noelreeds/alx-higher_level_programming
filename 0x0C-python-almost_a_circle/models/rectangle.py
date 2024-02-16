#!/usr/bin/python3
"""This is a Rectangle Module"""
from models.base import Base


class Rectangle(Base):
    """Class Rectangle"""
    def __init__(self, width, height, x=0, y=0, id=None):
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    """retrieves width attribute"""
    @property
    def width(self):
        return self.__width

    """sets the width attribute"""
    @width.setter
    def width(self, value):
        if type(value) is not int:
            raise TypeError('width must be an integer')
        elif value <= 0:
            raise ValueError('width must be > 0')
        self.__width = value

    """retrieves height attribute"""
    @property
    def height(self):
        return self.__height

    """sets the height attribute"""
    @height.setter
    def height(self, value):
        if type(value) is not int:
            raise TypeError('height must be an integer')
        elif value <= 0:
            raise ValueError('height must be > 0')
        self.__height = value

    """retrives y attribute"""
    @property
    def y(self):
        return self.__y

    """sets y attribute"""
    @y.setter
    def y(self, value):
        if type(value) is not int:
            raise TypeError('y must be an integer')
        elif value < 0:
            raise ValueError('y must be >= 0')
        self.__y = value

    """retrieves x attribute"""
    @property
    def x(self):
        return self.__x

    """validates x attributes"""
    @x.setter
    def x(self, value):
        if type(value) is not int:
            raise TypeError('x must be an integer')
        elif value < 0:
            raise ValueError('x must be >= 0')
        self.__x = value

    """returns the area value"""
    def area(self):
        area = self.__height * self.__width
        return area

    """prints a rectangle of '#' to stdout"""
    def display(self):
        for var2 in range(self.__y):
            print()
        for var in range(self.__height):
            for var3 in range(self.__x):
                print(" ", end="")
            for var1 in range(self.__width):
                print('#', end="")
            print()

    """overrides the __str__ method"""
    def __str__(self):
        pass