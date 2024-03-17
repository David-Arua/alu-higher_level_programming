#!/usr/bin/python3
"""Returns list of pascal triangles"""


def pascal_triangle(n):
    """
    Returns a list of lists representing the Pascal's triangle of n.

    Parameters:
    n: int
        The number of rows to generate.

    Returns:
    list
        A list of lists, each representing a row of the triangle.
    """
    if n <= 0:
        return []

    # Create an empty triangle
    triangle = [[1]]

    # Generate subsequent rows of the triangle
    for i in range(1, n):
        row = [1] * (i + 1)
        for j in range(1, i):
            row[j] = triangle[i-1][j-1] + triangle[i-1][j]
        triangle.append(row)

    return triangle
