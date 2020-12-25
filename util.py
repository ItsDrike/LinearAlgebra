from vector import Vector
from math import sqrt


def number_remap(
    value: float,
    old_min: float,
    old_max: float,
    new_min: float,
    new_max: float
) -> float:
    return ((value - old_min) / (old_max - old_min)) * (new_max - new_min) + new_min


def euclidean_distance(vec_1: Vector, vec_2: Vector) -> float:
    x_dist = abs(vec_1.x - vec_2.x)
    y_dist = abs(vec_1.y - vec_2.y)
    z_dist = abs(vec_1.z - vec_2.z)
    return sqrt(x_dist ** 2 + y_dist ** 2 + z_dist ** 2)
