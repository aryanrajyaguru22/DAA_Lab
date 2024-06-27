class Queue:
    def _init_(self):
        self.items = []

    def is_empty(self):
        return len(self.items) == 0

    def enqueue(self, item):
        self.items.append(item)

    def dequeue(self):
        if self.is_empty():
            raise IndexError("Dequeue from an empty queue")
        return self.items.pop(0)

    def front(self):
        if self.is_empty():
            raise IndexError("Front from an empty queue")
        return self.items[0]

    def size(self):
        return len(self.items)

    def _str_(self):
        return str(self.items)

def main():
    queue = Queue()
    while True:
        print("\nQueue Operations:")
        print("1. Enqueue")
        print("2. Dequeue")
        print("3. Front")
        print("4. Check if empty")
        print("5. Get size")
        print("6. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            item = input("Enter the item to enqueue: ")
            queue.enqueue(item)
            print(f"Queue after enqueue: {queue}")
        elif choice == '2':
            try:
                dequeued_item = queue.dequeue()
                print(f"Dequeued item: {dequeued_item}")
                print(f"Queue after dequeue: {queue}")
            except IndexError as e:
                print(e)
        elif choice == '3':
            try:
                front_item = queue.front()
                print(f"Front item: {front_item}")
            except IndexError as e:
                print(e)
        elif choice == '4':
            if queue.is_empty():
                print("Queue is empty")
            else:
                print("Queue is not empty")
        elif choice == '5':
            print(f"Queue size: {queue.size()}")
        elif choice == '6':
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please try again.")

if _name_ == "_main_":
    main()