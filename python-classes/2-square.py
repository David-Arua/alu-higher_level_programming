#!/usr/bin/python3
"""creates class square"""


class Square:
    """Defines size"""

    def __init__(self, size=0) -> None:
        self.__size = size
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
