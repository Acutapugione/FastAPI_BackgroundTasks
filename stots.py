from sys import getsizeof


def get_real_size(obj, seen=None):
    """
    Recursively calculates the real size of an object, including nested objects.
    """
    if seen is None:
        seen = set()
    obj_id = id(obj)
    if obj_id in seen:
        return 0  # Avoid infinite recursion for self-referential objects
    seen.add(obj_id)

    size = getsizeof(obj)
    if hasattr(obj, "__dict__"):
        size += get_real_size(obj.__dict__, seen)
    elif hasattr(obj, "__iter__") and not isinstance(obj, (str, bytes, bytearray)):
        size += sum([get_real_size(i, seen) for i in obj])

    return size


class A:  # 8 bytes type, 8 bytes pointer (int64)
    __slots__ = "x", "y", "z"

    def __init__(self):
        self.x = 0
        self.y = 0
        self.z = 0


class B:
    def __init__(self):
        self.x = 0
        self.y = 0
        self.z = 0


print(f"{get_real_size(A())=}")
print(f"{get_real_size(B())=}")

# print(f"{getsizeof(A())  + getsizeof(A().__slots__) +  getsizeof(A().__dict__)=}")
