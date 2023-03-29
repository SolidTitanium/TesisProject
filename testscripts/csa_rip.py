from typing import *
from collections.abc import Sequence
from annotated_types import Gt

class Temp_Func():

    @classmethod
    def create_n_simplex_from_basis(dimension: Annotated[int, Gt(-1)], basis: Set["Simplex"]) -> "Simplex":
        pass

    @classmethod
    def is_valid_simplex_basis(dimension: Annotated[int, Gt(-1)], basis: Set["Simplex"]) -> bool:
        reduced_basis = {s for ss in basis for s in ss.contains if s.dimension == 0}
        return dimension >= len(reduced_basis) - 1

class Simplex():
    
    def __init__(self: Self, dimension: Annotated[int, Gt(-1)] = 0, basis: Optional[Set["Simplex"]] = None) -> None:
        self.dimension = dimension
        if basis == None:
            self.points = {Simplex() for _ in range(dimension)}
            if dimension == 0:
                self.points.add(self)