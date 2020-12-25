import typing as t
from exceptions import DimensionError
from math import cos, sin


class Matrix:
    def __init__(self, matrix_list: list):
        self.matrix = matrix_list

        for row, row_vals in enumerate(self.matrix):
            for col, value in enumerate(row_vals):
                if not isinstance(value, (int, float)):
                    raise TypeError(f"All values must be integers or floats, but value[{row}][{col}] is {type(value)}")

    @property
    def cols(self) -> int:
        return len(self.matrix[0])

    @property
    def rows(self) -> int:
        return len(self.matrix)

    def __add__(self, other: "Matrix") -> "Matrix":
        cls = self.__class__

        if not isinstance(other, cls):
            raise TypeError(f"Matrix can only be added with other matrix, not {type(other)}")

        if not (self.rows, self.cols) == (other.rows, other.cols):
            raise DimensionError("These matrices can't be added (Wrong sizes)")

        matrix = []
        for row in range(self.rows):
            matrix.append([])
            for col in range(self.cols):
                slf = self[row][col]
                oth = other[row][col]
                matrix[row].append(slf + oth)

        return cls(matrix)

    def __sub__(self, other: "Matrix") -> "Matrix":
        cls = self.__class__

        if not isinstance(other, cls):
            raise TypeError(f"Matrix can only be subtracted by other matrix, not {type(other)}")

        if not (self.rows, self.cols) == (other.rows, other.cols):
            raise DimensionError("These matrices can't be subtracted (Wrong sizes)")

        matrix = []
        for row in range(self.rows):
            matrix.append([])
            for col in range(self.cols):
                matrix[row].append(self[row][col] - other[row][col])

        return cls(matrix)

    def __mul__(self, other: "Matrix") -> "Matrix":
        cls = self.__class__

        if not isinstance(other, cls):
            raise TypeError(f"Matrix can only be multiplied with other matrix, not {type(other)}")

        if self.cols != other.rows:
            raise DimensionError("These matrices can't be multiplied (Wrong sizes)")

        matrix = []
        for self_row in range(self.rows):
            matrix.append([])
            for other_col in range(other.cols):
                matrix[self_row].append(0)
                for self_col in range(self.cols):  # can also be other.col
                    matrix[self_row][other_col] += self[self_row][self_col] * other[self_col][other_col]

        return cls(matrix)

    def __truediv__(self, other: "Matrix") -> "Matrix":
        cls = self.__class__

        if not isinstance(other, cls):
            raise TypeError(f"Matrix can only be divided by other matrix, not {type(other)}")

        if self.cols != other.rows:
            raise DimensionError("These matrices can't be divided (Wrong sizes)")

        matrix = []
        for self_row in range(self.rows):
            matrix.append([])
            for other_col in range(other.cols):
                matrix[self_row].append(0)
                for self_col in range(self.cols):  # can also be other.col
                    matrix[self_row][other_col] += self[self_row][self_col] / other[self_col][other_col]

        return cls(matrix)

    def __floordiv__(self, other: "Matrix") -> "Matrix":
        cls = self.__class__

        if not isinstance(other, cls):
            raise TypeError(f"Matrix can only be divided by other matrix, not {type(other)}")

        if self.cols != other.rows:
            raise DimensionError("These matrices can't be divided (Wrong sizes)")

        matrix = []
        for self_row in range(self.rows):
            matrix.append([])
            for other_col in range(other.cols):
                matrix[self_row].append(0)
                for self_col in range(self.cols):  # can also be other.col
                    matrix[self_row][other_col] += self[self_row][self_col] // other[self_col][other_col]

        return cls(matrix)

    def __eq__(self, other: "Matrix") -> bool:
        if not isinstance(other, Matrix):
            raise TypeError(f"Equality comparison with Matrix can only be performed with another Matrix, got {type(other)}")

        return self.matrix == other.matrix

    def __getitem__(self, index) -> t.Union[int, float]:
        return self.matrix[index]

    def __setitem__(self, index: int, value: list) -> None:
        self.matrix[index] = value

    def __round__(self, n_digits: t.Optional[int] = None) -> "Matrix":
        cls = self.__class__

        matrix = []
        for row, row_vals in enumerate(self.matrix):
            matrix.append([])
            for value in row_vals:
                matrix[row].append(round(value, n_digits))

        return cls(matrix)

    def __abs__(self) -> "Matrix":
        cls = self.__class__

        matrix = []
        for row, row_vals in enumerate(self.matrix):
            matrix.append([])
            for value in row_vals:
                matrix[row].append(abs(value))

        return cls(matrix)

    def __len__(self) -> int:
        return len(self.matrix)

    @classmethod
    def from_vector(cls, vector: "vector.Vector") -> "Matrix":
        matrix_list = []
        for value in vector:
            matrix_list.append([value])

        return cls(matrix_list)

    @classmethod
    def get_projection_matrix(cls, in_dimensions: int = 3, out_dimensions: int = 2) -> "Matrix":
        projection_matrix = []
        for i in range(out_dimensions):
            projection_matrix.append([])
            for j in range(in_dimensions):
                if i == j:
                    projection_matrix[i].append(1)
                else:
                    projection_matrix[i].append(0)

        return cls(projection_matrix)

    @classmethod
    def get_2d_rotation_matrix(cls, clockwise: bool, angle: float) -> "Matrix":
        if clockwise:
            matrix = [
                [cos(angle), sin(angle)],
                [-sin(angle), cos(angle)]
            ]
        else:
            matrix = [
                [cos(angle), -sin(angle)],
                [sin(angle), cos(angle)]
            ]

        return cls(matrix)

    @classmethod
    def get_3d_rotation_matrix(cls, direction: t.Literal["x", "y", "z"], angle: float) -> "Matrix":
        if direction == "x":
            matrix = [
                [1, 0, 0],
                [0, cos(angle), -sin(angle)],
                [0, sin(angle), cos(angle)],
            ]
        elif direction == "y":
            matrix = [
                [cos(angle), 0, sin(angle)],
                [0, 1, 0],
                [-sin(angle), 0, cos(angle)],
            ]
        elif direction == "z":
            matrix = [
                [cos(angle), -sin(angle), 0],
                [sin(angle), cos(angle), 0],
                [0, 0, 1],
            ]

        return cls(matrix)


if __name__ == "__main__":
    print("This module wasn't designed to run on it's own")
