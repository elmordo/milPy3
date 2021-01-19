from typing import SupportsInt, SupportsIndex, SupportsFloat, SupportsComplex, SupportsAbs, Any
# supports index je podporovan až od pythonu 3.8


class CastableClass(object):

    def __init__(
            self,
            int_val: int,
            index_val: int,
            float_val: float,
            complex_val: complex,
            abs_val: Any
    ):
        self.int_val = int_val
        self.index_val = index_val
        self.float_val = float_val
        self.complex_val = complex_val
        self.abs_val = abs_val

    def __int__(self) -> int:
        print("casting to int")
        return self.int_val

    def __index__(self) -> int:
        print("casting to index")
        return self.index_val

    def __float__(self) -> float:
        print("casting to float")
        return self.float_val

    def __complex__(self) -> complex:
        print("casting to complex")
        return self.complex_val

    def __abs__(self) -> Any:
        print("get absolute value")
        return self.abs_val


instance = CastableClass(10, 5, 3.14, complex(1, 2), 666)
lst = list(range(10))

print(int(instance))
print(lst[instance])
print(float(instance))
print(complex(instance))
print(abs(instance))
