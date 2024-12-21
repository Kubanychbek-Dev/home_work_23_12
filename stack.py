class Node:
    """Конструктор для инициализации узла"""
    def __init__(self, data, next_node=None):
        self.data = data
        self.next_node = next_node


class Stack:
    """Конструктор для инициализации стека"""
    def __init__(self, stack_size=5, top=None):
        self.stack_size = stack_size
        self.top = top  # через топ обращаемся к атрибутам ноды

    def push(self, data):
        """Функция для добавления элемента в стек (на вершину стека)"""
        if self.size_stack() < self.stack_size:
            new_node = Node(data)
            new_node.next_node = self.top  # та вершина которая была
            self.top = new_node  # переназначаем вершину
        else:
            #print("Стэк переполнен")
            return "Стэк переполнен"

    def pop(self):
        """Функция для удаления верхнего элемента из стека"""
        if self.top:
            remove_last = self.top
            self.top = self.top.next_node
            return remove_last.data
        else:
            return "Стэк пуст"

    def is_empty(self):
        """Функция для проверки, есть ли в стеке элементы"""
        if self.top:
            return False
        else:
            return True

    def is_full(self):
        """Проверка на переполнение стека"""
        if self.stack_size == self.size_stack():
            return True
        else:
            return False

    def clear_stack(self):
        """Очистка стека"""
        while self.top:
              self.pop()
        return self.pop()

    def get_data(self, index):
        """Получает элемент из стека по переданному аргументу,
         кроме элемента с вершины стека"""
        counter = 0
        stack_item = self.top
        while stack_item:
            if counter == index:
                return stack_item.data
            stack_item = stack_item.next_node
            counter += 1
        return f"Out of range"

    def size_stack(self):
        """Возвращает размер стека (количество элементов в стеке)"""
        counter = 0
        stack_item = self.top
        while stack_item:
            counter += 1
            stack_item = stack_item.next_node
        return counter

    def counter_int(self):
        """Проверяем, есть ли элементы в стеке, являющимся экземпляроми класса int (numbers)"""
        counter = 0
        stack_item = self.top
        while stack_item:
            if isinstance(stack_item.data, int):
                counter += 1
            stack_item = stack_item.next_node
        return counter


# stack = Stack()
# stack.push(1)
# stack.push("sta")
# stack.push(2)
# stack.push(3)
# stack.push(3.88)

