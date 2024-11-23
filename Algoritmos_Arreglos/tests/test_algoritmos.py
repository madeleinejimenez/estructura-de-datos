import unittest
from main import buscar_mayor, buscar_menor, bubble_sort, selection_sort

class TestAlgoritmos(unittest.TestCase):
    def test_buscar_mayor(self):
        self.assertEqual(buscar_mayor([3, 1, 4, 1, 5, 9]), 9)
        self.assertEqual(buscar_mayor([-1, -5, -3]), -1)

    def test_buscar_menor(self):
        self.assertEqual(buscar_menor([3, 1, 4, 1, 5, 9]), 1)
        self.assertEqual(buscar_menor([-1, -5, -3]), -5)

    def test_bubble_sort(self):
        arr = [64, 34, 25, 12, 22, 11, 90]
        bubble_sort(arr)
        self.assertEqual(arr, [11, 12, 22, 25, 34, 64, 90])

    def test_selection_sort(self):
        arr = [64, 34, 25, 12, 22, 11, 90]
        selection_sort(arr)
        self.assertEqual(arr, [11, 12, 22, 25, 34, 64, 90])

if __name__ == "__main__":
    unittest.main()
