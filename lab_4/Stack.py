class StackQueue:
    def push(self, element):
        pass

    def pop(self):
        pass

    def element(self):
        pass

    def is_empty(self):
        pass

class ArrayStack(StackQueue):
    def __init__(self, size):
        self.size = size
        self.stack = []

    def push(self, element):
        if len(self.stack) < self.size:
            self.stack.append(element)
        else:
            raise Exception("Stack is full")

    def pop(self):
        if not self.is_empty():
            return self.stack.pop()
        else:
            raise Exception("Stack is empty")

    def element(self):
        if not self.is_empty():
            return self.stack[-1]
        else:
            raise Exception("Stack is empty")

    def is_empty(self):
        return len(self.stack) == 0

    def is_full(self):
        return len(self.stack) == self.size

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedStack(StackQueue):
    def __init__(self):
        self.top = None

    def push(self, element):
        new_node = Node(element)
        new_node.next = self.top
        self.top = new_node

    def pop(self):
        if not self.is_empty():
            top_data = self.top.data
            self.top = self.top.next
            return top_data
        else:
            raise Exception("Stack is empty")

    def element(self):
        if not self.is_empty():
            return self.top.data
        else:
            raise Exception("Stack is empty")

    def is_empty(self):
        return self.top is None

class ListStack(StackQueue):
    def __init__(self):
        self.stack = []

    def push(self, element):
        self.stack.append(element)

    def pop(self):
        if not self.is_empty():
            return self.stack.pop()
        else:
            raise Exception("Stack is empty")

    def element(self):
        if not self.is_empty():
            return self.stack[-1]
        else:
            raise Exception("Stack is empty")

    def is_empty(self):
        return len(self.stack) == 0

# Create an instance of ArrayUpStack with a size of 5
array_stack = ArrayStack(5)

# Push elements onto the stack
array_stack.push(1)
array_stack.push(2)
array_stack.push(3)

# Check if the stack is empty
print("Is the ArrayUpStack empty?", array_stack.is_empty())

# Check the top element
print("Top element of ArrayUpStack:", array_stack.element())

# Pop elements from the stack
print("Popped element from ArrayUpStack:", array_stack.pop())
print("Popped element from ArrayUpStack:", array_stack.pop())
print("Popped element from ArrayUpStack:", array_stack.pop())

# Check if the stack is empty again
print("Is the ArrayUpStack empty?", array_stack.is_empty())

# Create an instance of LinkedStack
linked_stack = LinkedStack()

# Push elements onto the stack
linked_stack.push("B# Create an instance of ArrayStack with a maximum size of 5")
array_stack = ArrayStack(5)

# Push some fruits onto the stack
array_stack.push("Apple")
array_stack.push("Banana")
array_stack.push("Cherry")

# Check if the basket is empty
print("Is the fruit basket empty?", array_stack.is_empty())

# Peek at the top fruit
print("The top fruit in the basket is:", array_stack.element())

# Take out fruits from the basket
print("Took out a", array_stack.pop())
print("Took out a", array_stack.pop())
print("Took out a", array_stack.pop())

# Check if the basket is empty again
print("Is the fruit basket empty?", array_stack.is_empty())

# Create an instance of LinkedStack
linked_stack = LinkedStack()

# Add some books to the stack
linked_stack.push("Harry Potter")
linked_stack.push("Lord of the Rings")
linked_stack.push("The Hobbit")

# Check if the bookshelf is empty
print("Is the bookshelf empty?", linked_stack.is_empty())

# Peek at the top book
print("The top book on the bookshelf is:", linked_stack.element())

# Take books off the bookshelf
print("Took down the book:", linked_stack.pop())
print("Took down the book:", linked_stack.pop())
print("Took down the book:", linked_stack.pop())

# Check if the bookshelf is empty again
print("Is the bookshelf empty?", linked_stack.is_empty())

# Create an instance of ListStack
list_stack = ListStack()

# Stack up some dishes
list_stack.push("Plate")
list_stack.push("Bowl")
list_stack.push("Cup")

# Check if the stack is empty
print("Is the stack of dishes empty?", list_stack.is_empty())

# See the dish on top
print("The dish on top of the stack is:", list_stack.element())

# Remove dishes from the stack
print("Removed a", list_stack.pop())
print("Removed a", list_stack.pop())
print("Removed a", list_stack.pop())

# Check if the stack of dishes is empty again
print("Is the stack of dishes empty?", list_stack.is_empty())
