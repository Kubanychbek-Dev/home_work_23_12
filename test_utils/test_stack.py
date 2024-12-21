import unittest
from stack import Stack


class TestStack(unittest.TestCase):
    st = Stack()

#Testing push
    def test_push(self):
        self.st.push(1)
        self.st.push(2)
        self.st.push(3)
        self.st.push(4)
        self.st.push(5)
        self.assertEqual(self.st.push(4), "Стэк переполнен")

#Testing pop
    def test_pop_if(self):
        self.st.clear_stack()
        self.st.push(1)
        self.st.push(44)
        self.assertEqual(self.st.pop(), 44)

    def test_pop_else(self):
        self.st.clear_stack()
        self.assertEqual(self.st.pop(), "Стэк пуст")

# #Testing is_empty
    def test_is_empty_if(self):
        self.st.push(44)
        self.assertEqual(self.st.is_empty(), False)

    def test_is_empty_else(self):
        self.st.clear_stack()
        self.assertEqual(self.st.is_empty(), True)

# #Testing is_full
    def test_is_full_if(self):
        self.st.clear_stack()
        self.st.push(1)
        self.st.push(2)
        self.st.push(3)
        self.st.push(4)
        self.st.push(5)
        self.assertEqual(self.st.is_full(), True)

    def test_is_full_else(self):
        self.st.clear_stack()
        self.assertEqual(self.st.is_full(), False)

#Testing clear_stack
    def test_clear_stack(self):
        self.st.push(1)
        self.st.push(2)
        self.st.push(3)
        self.st.push(4)
        self.assertEqual(self.st.clear_stack(), "Стэк пуст")

#Testing get_data
    def test_get_data(self):
        self.st.clear_stack()
        self.st.push(1)
        self.st.push(2)
        self.st.push(3)
        self.st.push(4)
        self.assertEqual(self.st.get_data(2), 2)

    def test_get_data_else(self):
        self.st.clear_stack()
        self.st.push(1)
        self.st.push(2)
        self.assertEqual(self.st.get_data(2), "Out of range")

#Testing size_stack
    def test_size_stack(self):
        self.st.clear_stack()
        self.st.push(1)
        self.st.push(2)
        self.assertEqual(self.st.size_stack(), 2)

#Testing counter_int
    def test_counter_int(self):
        self.st.clear_stack()
        self.st.push(1)
        self.st.push(2)
        self.st.push(3)
        self.st.push(4)
        self.st.push("Hello")
        self.assertEqual(self.st.counter_int(), 4)