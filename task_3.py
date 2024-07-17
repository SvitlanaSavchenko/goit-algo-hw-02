def check_symmetry(s):
    stack = []
    matching_brackets = {'(': ')', '{': '}', '[': ']'}
    open_brackets = set(matching_brackets.keys())
    close_brackets = set(matching_brackets.values())
    
    for char in s:
        if char in open_brackets:
            stack.append(char)
        elif char in close_brackets:
            if not stack:
                return "Несиметрично"
            top = stack.pop()
            if matching_brackets[top] != char:
                return "Несиметрично"
    
    if stack:
        return "Несиметрично"
    else:
        return "Симетрично"

# Приклади використання:
strings = [
    "( ){[ 1 ]( 1 + 3 )( ){ }}",
    "( 23 ( 2 - 3);",
    "( 11 }"
]

for s in strings:
    result = check_symmetry(s)
    print(f"{s}: {result}")
