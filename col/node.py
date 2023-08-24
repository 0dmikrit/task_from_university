class Node:
    def __init__(self, value):
        self.value = value
        self.children = []

    def add_child(self, child):
        self.children.append(child)

    def view(self):
        return self.value


class Tree:
    def __init__(self, root):
        self.nodes = [] #Список узлов
        self.root = Node(root)

    def __call__(self, *args, **kwargs):
        """При вызове класса с аргументом, мы добавляем аргумент в список узлов
иначе вызываем метод view"""
        if args:
            self.nodes.append(Node(args[0]))
            return
        return self.view(self.root)

    def create(self):
        """Метод, который пробегает по списку объектов и создает дерево"""
        for node in self.nodes:
            self.root.add_child(node)
            ...

    def view(self, node):
        """Метод показывающий дерево"""
        res = [node.view()]
        if node.children():
            for child in node.children():
                res.append(self.view(child))
        return res






