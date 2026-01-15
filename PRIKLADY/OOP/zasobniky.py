class Stack:
    def __init__(self):
        self.stack = []
        self.n = 0

    def isEmpty(self):
        if self.n == 0:
            return True
        else:
            return False
        
    def push(self, prvek):
        self.n += 1
        self.stack.append(prvek)
    
    def pop(self):
        if not self.isEmpty():
            self.n -= 1
            return self.stack.pop()
        else:
            return print ("POP není možné, zásobník je prázdný")

    def peek(self):
        if not self.isEmpty():
            return self.stack [self.n-1]
        else:
            return print ("zasobnik je prazdny")