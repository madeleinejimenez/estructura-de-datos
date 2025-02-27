class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = None

class DoublyLinkedQueue:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def enqueue(self, value):
        """ Agrega un elemento al final de la cola """
        new_node = Node(value)
        if self.tail is None:  # Si la cola está vacía
            self.head = self.tail = new_node
        else:
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node
        self.size += 1

    def dequeue(self):
        """ Elimina y devuelve el elemento al frente de la cola """
        if self.head is None:
            raise IndexError("La cola está vacía")
        
        value = self.head.value
        self.head = self.head.next
        if self.head is None:  # Si la cola queda vacía
            self.tail = None
        else:
            self.head.prev = None
        self.size -= 1
        return value

    def peek(self):
        """ Devuelve el primer elemento sin eliminarlo """
        if self.head is None:
            return None
        return self.head.value

    def is_empty(self):
        """ Retorna True si la cola está vacía """
        return self.size == 0

    def __len__(self):
        return self.size

    def display(self):
        """ Muestra los elementos de la cola """
        current = self.head
        elements = []
        while current:
            elements.append(str(current.value))
            current = current.next
        print(" <- ".join(elements))

# Ejemplo de uso
queue = DoublyLinkedQueue()
queue.enqueue(10)
queue.enqueue(20)
queue.enqueue(30)
queue.display()  # Salida: 10 <- 20 <- 30
print("Dequeued:", queue.dequeue())  # Salida: Dequeued: 10
queue.display()  # Salida: 20 <- 30
