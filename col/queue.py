from col.col_error import NullError


class Queue:
    def __init__(self, lst):
        self.__lst = lst

    def __sizeof__(self):
        return self.__lst.__sizeof__()

    def __call__(self, *args):
        if args:
            if isinstance(args[0], int):
                self.__lst.append(args[0])
                return
            raise NullError("You can't use other type")
        if len(self.__lst):
            res = self.__lst[0]
            self.__lst.pop(0)
            return res
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
        return iter(self.__lst)

    def filtration(self):
        """Filter our queue if element in queue is eval"""
        self.__lst = list(filter((lambda x: x if x % 2 == 0 else 0), self.__lst))


queue = Queue([])