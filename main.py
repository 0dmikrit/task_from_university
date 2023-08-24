from col.queue import queue
from col.stack import stack


def run_queue():
    print(f'{"#"*8}Queue{"#"*8}')
    queue(1)
    queue(2)
    print(list(queue))
    print(queue())
    print(list(queue))
    print(f'{"#" * 21}')


def run_stack():
    print(f'{"#" * 8}Stack{"#" * 8}')
    stack(1)
    stack(2)
    stack(6)
    print(list(stack))
    print(stack())
    print(list(stack))
    print(f'{"#" * 21}')


def run_tree():
    pass


if __name__ == '__main__':
    run_queue()
    run_stack()