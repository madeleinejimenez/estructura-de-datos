# Simulación de pedidos en un restaurante
restaurant_queue = DoublyLinkedQueue()

# Llegan pedidos
restaurant_queue.enqueue("Pedido 1: Hamburguesa")
restaurant_queue.enqueue("Pedido 2: Pizza")
restaurant_queue.enqueue("Pedido 3: Ensalada")

# Mostramos los pedidos
print("Pedidos en espera:")
restaurant_queue.display()

# Se atiende el primer pedido
print("Atendiendo:", restaurant_queue.dequeue())

# Mostramos los pedidos restantes
print("Pedidos restantes:")
restaurant_queue.display()
