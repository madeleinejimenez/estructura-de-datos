class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.left = None
        self.right = None

class BST:
    def __init__(self):
        self.root = None

    def insert(self, key, value):
        if self.root is None:
            self.root = Node(key, value)
        else:
            self._insert(self.root, key, value)

    def _insert(self, root, key, value):
        if key < root.key:
            if root.left is None:
                root.left = Node(key, value)
            else:
                self._insert(root.left, key, value)
        else:
            if root.right is None:
                root.right = Node(key, value)
            else:
                self._insert(root.right, key, value)

    def search(self, key):
        return self._search(self.root, key)

    def _search(self, root, key):
        if root is None:
            return None
        if root.key == key:
            return root.value
        if key < root.key:
            return self._search(root.left, key)
        return self._search(root.right, key)

    def delete(self, key):
        self.root = self._delete(self.root, key)

    def _delete(self, root, key):
        if root is None:
            return root
        if key < root.key:
            root.left = self._delete(root.left, key)
        elif key > root.key:
            root.right = self._delete(root.right, key)
        else:
            if root.left is None:
                return root.right
            elif root.right is None:
                return root.left
            temp = self._min_value_node(root.right)
            root.key = temp.key
            root.value = temp.value
            root.right = self._delete(root.right, temp.key)
        return root

    def _min_value_node(self, node):
        current = node
        while current.left is not None:
            current = current.left
        return current

# Aplicación de agenda de contactos usando BST
class ContactManager:
    def __init__(self):
        self.bst = BST()

    def add_contact(self, name, number):
        self.bst.insert(name, number)

    def find_contact(self, name):
        return self.bst.search(name)

    def delete_contact(self, name):
        self.bst.delete(name)

    def display_contacts(self):
        contacts = []
        self._inorder(self.bst.root, contacts)
        return contacts

    def _inorder(self, root, contacts):
        if root is not None:
            self._inorder(root.left, contacts)
            contacts.append((root.key, root.value))
            self._inorder(root.right, contacts)

# Pruebas de la aplicación
if __name__ == "__main__":
    cm = ContactManager()
    cm.add_contact("Alice", "123456789")
    cm.add_contact("Bob", "987654321")
    cm.add_contact("Charlie", "456789123")
    
    print("Lista de contactos:", cm.display_contacts())
    print("Buscar contacto Bob:", cm.find_contact("Bob"))
    cm.delete_contact("Bob")
    print("Lista de contactos tras eliminar Bob:", cm.display_contacts())
