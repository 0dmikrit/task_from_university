def memory(func):
    def inner(args):
        return func(args)
    print(func.__sizeof__)
    return inner


def log(func):
    def inner(args):
        print(f'Method name is {func.__name__}\nDocumentation: {func.__doc__}')
        return func(args)
    return inner