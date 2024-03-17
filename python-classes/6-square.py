#!/usr/bin/python3
"""creates class square with private instance
    attribute size and public instance method"""


class Square:
    """Defines private instance attribute"""

    def __init__(self, size=0, position=(0, 0)) -> None:
        self.size = size
        self.position = position

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @property
    def position(self):
        return self.__position

    @position.setter
    def position(self, value):
        check = 0
        while 1:
            if type(value) is not tuple or len(value) != 2:
                check += 1
                break
            if type(value[0]) is not int or type(value[1]) is not int:
                check += 1
                break
            if value[0] < 0 or value[1] < 0:
                check += 1
            break
        if check == 0:
            self.__position = value
        else:
            raise TypeError("position must be a tuple of 2 positive integers")

    def area(self):
        """Calculates the area of the square"""
        return (self.__size ** 2)

    def my_print(self):
        """prints square of size using #"""
        if self.__size > 0:
            for y in range(self.__position[1]):
                print()
            for column in range(self.__size):
                for x in range(self.__position[0]):
                    print(" ", end="")
                for row in range(self.__size):
                    print("#", end="")
                print()
        else:
            print()
