class HashTable:
    def __init__(self):
        self.__data = (0, )
        self.__keys = [ ]

    def __call__(self, value):
        if value:
            self.__key = int(str(hash(value))[17::])
            self.__keys.append(self.__key)
            self.__data = tuple(map((lambda x: x if x in self.__keys else 0), [i for i in range(1000)]))
            return self.__key

    def __getitem__(self, item):
        if item in range(len(self.__data)):
            return self.__data[item]

    def __sizeof__(self):
        return self.__data.__sizeof__()


ht = HashTable()
print(ht('f'))
print(ht.__sizeof__())