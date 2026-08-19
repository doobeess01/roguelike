class Vector:
    def __init__(self, x: int, y: int):
        self.x = x
        self.y = y

def vector_from_tuple(t: tuple[int,int], ij: bool = False):
    return Vector(t[0], t[1]) if not ij else Vector(t[1], t[0])