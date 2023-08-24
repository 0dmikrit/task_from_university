from col.helper import log
from col.col_error import NullError
import math


class MathQueue:
    def __init__(self, lst):
        self.__lst = lst

    def __sizeof__(self):
        return self.__lst.__sizeof__()

    def __call__(self, *args):
        if args:
            if isinstance(args[0], str):
                self.__lst.append(args[0])
                return
            raise NullError("You can't use other type")
        if len(self.__lst):
            res = self.__lst[0]
            self.__lst.pop(0)
            return eval(res)
        raise NullError('No element for delete')

    def __len__(self):
        return len(self.__lst)

    def __getitem__(self, item):
        if item in range(len(self.__lst)):
            return self.__lst[item]
        raise IndexError

    def __setitem__(self, key, value):
        if key in range(len(self.__lst)):
            self.__lst[key] = value
            return
        raise IndexError

    def __delitem__(self, key):
        if key in range(len(self.__lst)):
            self.__lst.pop(key)
            return
        raise IndexError

    def __iter__(self):
        res = [eval(i) for i in iter(self.__lst)]
        return iter(res)


mq = MathQueue([])