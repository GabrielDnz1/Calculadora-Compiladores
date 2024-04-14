from enum import Enum

class Exp(Enum):
    BINARY_OP = 0
    UNARY_OP = 1
    CONSTANT = 2
    FRACTION = 3
    VARIABLE = 4