import time
import random

class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key

class BST:
    def __init__(self):
        self.root = None

    def insert(self, key):
        if self.root is None:
            self.root = Node(key)
        else:
            self._insert(self.root, key)

    def _insert(self, root, key):
        if key < root.val:
            if root.left is None:
                root.left = Node(key)
            else:
                self._insert(root.left, key)
        else:
            if root.right is None:
                root.right = Node(key)
            else:
                self._insert(root.right, key)

    def search(self, key):
        return self._search(self.root, key)

    def _search(self, root, key):
        if root is None or root.val == key:
            return root is not None
        if key < root.val:
            return self._search(root.left, key)
        return self._search(root.right, key)

class HashTable:
    def __init__(self, size):
        self.size = size
        self.table = [[] for _ in range(size)]

    def _hash(self, key):
        return key % self.size

    def insert(self, key):
        index = self._hash(key)
        if key not in self.table[index]:
            self.table[index].append(key)

    def search(self, key):
        index = self._hash(key)
        return key in self.table[index]

# Pruebas de rendimiento
def measure_time(structure, data, operation):
    start_time = time.time()
    for item in data:
        if operation == "insert":
            structure.insert(item)
        elif operation == "search":
            structure.search(item)
    return time.time() - start_time

# Generar datos de prueba
num_elements = 10000
data = random.sample(range(1, 100000), num_elements)
search_data = random.sample(data, num_elements // 10)

# Instanciar estructuras
bst = BST()
hash_table = HashTable(10000)

# Medir tiempos de inserción
time_bst_insert = measure_time(bst, data, "insert")
time_hash_insert = measure_time(hash_table, data, "insert")

# Medir tiempos de búsqueda
time_bst_search = measure_time(bst, search_data, "search")
time_hash_search = measure_time(hash_table, search_data, "search")

# Mostrar resultados
print(f"Tiempo de inserción BST: {time_bst_insert:.6f} segundos")
print(f"Tiempo de inserción HashTable: {time_hash_insert:.6f} segundos")
print(f"Tiempo de búsqueda BST: {time_bst_search:.6f} segundos")
print(f"Tiempo de búsqueda HashTable: {time_hash_search:.6f} segundos")
