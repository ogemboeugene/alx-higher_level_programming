#!/usr/bin/python3
"""
Square class that inherits from Rectangle
"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """
    Represents a square, which inherits from the Rectangle class.
    """

    def __init__(self, size, x=0, y=0, id=None):
        """
        Initializes a Square object.

        Args:
            size (int): The size of the square (width and height).
            x (int, optional): The x-coordinate of the square's position.
                               Defaults to 0.
            y (int, optional): The y-coordinate of the square's position.
                               Defaults to 0.
            id (int, optional): The unique identifier for the square.
                                Defaults to None.
        """
        super().__init__(size, size, x, y, id)

    def update(self, *args, **kwargs):
        """
        Updates the attributes of the square.

        Args:
            *args: Variable length argument list (no-keyworded arguments).
            **kwargs: Keyworded arguments.
        """
        if args and len(args) > 0:
            attributes = ["id", "size", "x", "y"]
            for i, value in enumerate(args):
                setattr(self, attributes[i], value)
        elif kwargs:
            for key, value in kwargs.items():
                setattr(self, key, value)

    def __str__(self):
        """
        Returns a string representation of the square.

        Returns:
            str: The string representation of the square.
        """
        return f"[Square] ({self.id}) {self.x}/{self.y} - {self.width}"

    @property
    def size(self):
        """
        Gets the size of the square.

        Returns:
            int: The size of the square.
        """
        return self.width

    @size.setter
    def size(self, value):
        """
        Sets the size of the square.

        Args:
            value (int): The size of the square.
        """
        self.width = value
        self.height = value

    def to_dictionary(self):
        """
        Returns the dictionary representation of the square.

        Returns:
            dict: The dictionary representation of the square.
        """
        return {
            "id": self.id,
            "size": self.width,
            "x": self.x,
            "y": self.y
        }
