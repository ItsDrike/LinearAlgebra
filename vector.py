import typing as t
from exceptions import DimensionError
from math import floor

from matrix import Matrix


class Vector:
    def __init__(self, *points: tuple):
        if len(points) == 1 and isinstance(points[0], list):
            self.points = points[0]
        else:
            self.points = list(points)
        self._compute()

    def _compute(self) -> None:
        """Compute all attributes from `self.points`."""
        for index, point in enumerate(self.points):
            if not isinstance(point, (int, float)):
                raise TypeError(f"All points must be integers or floats, but point{index} is {type(point)}")

        if self.dimensions <= 4:
            for attr_name, value in zip(list("xyzw"), self.points):
                setattr(self, attr_name, value)

    def project(self, dimensions: int = 2) -> "Vector":
        cls = self.__class__
        matrix = Matrix.from_vector(self)
        projection_matrix = Matrix.get_projection_matrix(self.dimensions, dimensions)
        projected_matrix = projection_matrix * matrix
        return cls.from_matrix(projected_matrix)

    def __add__(self, other: "Vector") -> "Vector":
        cls = self.__class__

        if not isinstance(other, cls):
            raise TypeError(f"Vector can only be added with another Vector, not with {type(other)}")

        if self.dimensions != other.dimensions:
            raise DimensionError(f"Vector can only be added with another Vector of the same size ({self.dimensions})!={other.dimensions}")

        added_vector = []
        for index in range(other.dimensions):
            added_vector[index] = self[index] + other[index]

        return cls(*added_vector)

    def __sub__(self, other: "Vector") -> "Vector":
        cls = self.__class__

        if not isinstance(other, cls):
            raise TypeError(f"Vector can only be subtracted by another Vector, not by {type(other)}")

        if self.dimensions != other.dimensions:
            raise DimensionError(f"Vector can only be subtracted by another Vector of the same size ({self.dimensions})!={other.dimensions}")

        added_vector = []
        for index in range(other.dimensions):
            added_vector[index] = self[index] - other[index]

        return cls(*added_vector)

    def __mul__(self, other: t.Union[int, float]) -> "Vector":
        cls = self.__class__

        if not isinstance(other, (int, float)):
            raise TypeError(f"Vector can only be multiplied with an integer or float, not with {type(other)}")

        extended_vector = []
        for point in self:
            extended_vector.append(point * other)

        return cls(*extended_vector)

    def __truediv__(self, other: t.Union[int, float]) -> "Vector":
        cls = self.__class__

        if not isinstance(other, (int, float)):
            raise TypeError(f"Vector can only be divided by an integer or float, not by {type(other)}")

        extended_vector = []
        for point in self:
            extended_vector.append(point / other)

        return cls(*extended_vector)

    def __floordiv__(self, other: t.Union[int, float]) -> "Vector":
        cls = self.__class__

        if not isinstance(other, (int, float)):
            raise TypeError(f"Vector can only be divided by an integer or float, not by {type(other)}")

        extended_vector = []
        for point in self:
            extended_vector.append(floor(point / other))

        return cls(*extended_vector)

    def __eq__(self, other: "Vector") -> bool:
        if not isinstance(other, Vector):
            raise TypeError(f"Equality comparison with Vector can only be performed with another Vector, got {type(other)}")

        return self.points == other.points

    def __getitem__(self, index: int) -> t.Union[int, float]:
        return self.points[index]

    def __setitem__(self, index: int, value: t.Union[int, float]) -> None:
        self.points[index] = value
        self._compute()

    def __delitem__(self, index: int) -> None:
        del self.points[index]
        self._compute()

    def __round__(self, n_digits: t.Optional[int] = None) -> "Vector":
        cls = self.__class__

        points = [round(point, n_digits) for point in self.points]
        return cls(*points)

    def __abs__(self) -> "Vector":
        cls = self.__class__

        points = [abs(point) for point in self.points]
        return cls(*points)

    def __len__(self) -> int:
        return len(self.points)

    @property
    def dimensions(self) -> int:
        return self.__len__()

    @classmethod
    def from_matrix(cls, matrix: "Matrix") -> "Vector":
        points = []
        if matrix.cols != 1:
            raise DimensionError("Matrix must only have 1 row.")

        for col in matrix:
            points.append(col[0])

        return cls(*points)


if __name__ == "__main__":
    print("This module wasn't designed to run on it's own")
