from col.col_error import NullError


class Stack:
    """Класс Stack имеет возможность итерации,
обращение по индексу
"""
    def __init__(self, arr):
        self.__arr = arr

    def __sizeof__(self):
        return self.__arr.__sizeof__()

    def __iter__(self):
        return iter(self.__arr[::-1])

    def __len__(self):
        return len(self.__arr)

    def __getitem__(self, item):
        if item in range(len(self.__arr)):
            return self.__arr[::-1][item]
        raise IndexError

    def __setitem__(self, key, value):
        if key in range(len(self.__arr)):
            self.__arr = self.__arr[::-1]
            self.__arr[key] = value
            self.__arr = self.__arr[::-1]
            return
        raise IndexError

    def __call__(self, *args):
        if args:
            if self.__checking(args[0]):
                self.__arr.append(args[0])
                return
            raise NullError
        if self.__arr:
            res = self.__arr[-1]
            self.__arr.pop(-1)
            return res
        raise NullError

    def __is_len(self):
        if len(self.__arr) < 100:
            return True
        return False

    def __check_size(self, other):
        if other.__sizeof__() <= 28:
            return True
        return False

    def __checking(self, other):
        if isinstance(other, int)  and self.__is_len() and self.__check_size(other):
            return True
        return False

    def clear_stack(self):
        self.__arr.clear()

    def docs(self):
        return self.__doc__



stack = Stack([])