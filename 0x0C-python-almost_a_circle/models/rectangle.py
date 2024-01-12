#!/usr/bin/python3
"""
Rectangle class which inherits from Base class
"""
from models.base import Base


class Rectangle(Base):
    """
    Represents a rectangle, which inherits from the Base class.
    """

    def __init__(self, width, height, x=0, y=0, id=None):
        """__init__ initialized constuctor
        Args:
            width (int)
            height (int)
            x (int, optional): Defaults to 0.
            y (int, optional): Defaults to 0.
            id ([type], optional): Defaults to None.
        """
        super().__init__(id)

        self.check_integer_parameter(width, 'width')
        self.check_integer_parameter(height, 'height')
        self.check_integer_parameter(x, 'x')
        self.check_integer_parameter(y, 'y')

        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y

    @property
    def width(self):
        """Getter value for width
        """
        return self.__width

    @width.setter
    def width(self, param):
        """Setter value for width
        """
        self.check_integer_parameter(param, 'width')

        self.__width = param

    @property
    def height(self):
        """Getter value for height
        """
        return self.__height

    @height.setter
    def height(self, param):
        """Setter value for height
        """
        self.check_integer_parameter(param, 'height')

        self.__height = param

    @property
    def x(self):
        """Getter value for x
        """
        return self.__x

    @x.setter
    def x(self, param):
        """Setter value for x"
        """
        self.check_integer_parameter(param, 'x')

        self.__x = param

    @property
    def y(self):
        """Getter value for y
        """
        return self.__y

    @y.setter
    def y(self, param):
        """Setter value for y
        """
        self.check_integer_parameter(param, 'y')

        self.__y = param

    def check_integer_parameter(self, value, param):
        """Args:
            width (int)
            height (int)
            x (int, optional): Defaults to 0.
            y (int, optional): Defaults to 0.
            id ([type], optional): Defaults to None.
        """
        if type(value) is not int:
            raise TypeError(param + ' must be an integer')

        if value <= 0 and param in ('width', 'height'):
            raise ValueError(param + ' must be > 0')

        if value < 0 and param in ('x', 'y'):
            raise ValueError(param + ' must be >= 0')

    def area(self):
        """
        Calculates and returns the area of the rectangle.

        Returns:
            int: The area of the rectangle.
        """
        return self.width * self.height

    def display(self):
        """Prints the rectangle using the '#' character."""
        for _ in range(self.y):
            print()
        for _ in range(self.height):
            print(" " * self.x + "#" * self.width)

    def __str__(self):
        """
        Returns a string representation of the rectangle.

        Returns:
            str: The string representation of the rectangle.
        """
        return f"[Rectangle] ({self.id}) {self.x}/{self.y} - " \
               f"{self.width}/{self.height}"

    def update(self, *args, **kwargs):
        """
        Updates the attributes of the rectangle using positional and \
                keyword arguments.
        """
        if args:
            attrs = ['id', 'width', 'height', 'x', 'y']
            for i in range(len(args)):
                setattr(self, attrs[i], args[i])
        else:
            for key, value in kwargs.items():
                setattr(self, key, value)

    def to_dictionary(self):
        """
        Returns the dictionary representation of the rectangle.

        Returns:
            dict: The dictionary representation of the rectangle.
        """
        return {
            "id": self.id,
            "width": self.width,
            "height": self.height,
            "x": self.x,
            "y": self.y
        }
