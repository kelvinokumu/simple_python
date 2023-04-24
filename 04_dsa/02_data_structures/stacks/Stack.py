class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None


class Stack:
    def __init__(self):
        self.top = None
        self.size = 0

    def push(self, data):
        # create a new node
        node = Node(data)
        if self.top:
            node.next = self.top
            self.top = node
        else:
            self.top = node
            self.size += 1

    def pop(self):
        if self.top:
            data = self.top.data

            self.size -= 1
            if self.top.next:  # check if there is more than one node.
                self.top = self.top.next
            else:
                self.top = None
            return data
        else:
            print("Stack is empty")

    def peek(self):
        if self.top:
            return self.top.data
        else:
            print("Stack is empty")


def check_brackets(expression):
    brackets_stack = Stack()  # The stack class, we defined in previous section.
    last = ' '
    for ch in expression:
        if ch in ('{', '[', '('):
            brackets_stack.push(ch)

        if ch in ('}', ']', ')'):
            last = brackets_stack.pop()
            if last == '{' and ch == '}':
                continue
            elif last == '[' and ch == ']':
                continue
            elif last == '(' and ch == ')':
                continue
            else:
                return False
    if brackets_stack.size > 0:
        return False
    else:
        return True


sl = (
    "{(foo)(bar)}[hello](((this)is)a)test",
    "{(foo)(bar)}[hello](((this)is)atest",
    "{(foo)(bar)}[hello](((this)is)a)test))"
)

for s in sl:
    m = check_brackets(s)
    print("{}: {}".format(s, m))
