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
