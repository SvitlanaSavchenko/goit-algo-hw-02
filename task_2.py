from collections import deque

def is_palindrome(s):
    # Перевіряємо, чи вхідний параметр є рядком
    if not isinstance(s, str):
        raise TypeError("Input should be a string")
    
    # Перетворюємо рядок у нижній регістр і видаляємо пробіли
    s = s.lower().replace(" ", "")
    
    # Ініціалізуємо двосторонню чергу (deque)
    d = deque()
    
    # Додаємо символи рядка до черги
    for char in s:
        d.append(char)
    
    # Порівнюємо символи з обох кінців черги
    while len(d) > 1:
        if d.popleft() != d.pop():
            return False
    
    # Якщо черга порожня або містить лише один символ (для непарної довжини)
    return True

# Тести для функції is_palindrome
try:
    input_string = "A man a plan a canal Panama"
    if is_palindrome(input_string):
        print(f"{input_string} є паліндромом.")
    else:
        print(f"{input_string} не є паліндромом.")
    
    # Приклад з неправильним вхідним типом (це викличе помилку TypeError)
    print(is_palindrome(12345))
    
except TypeError as e:
    print(f"Error: {e}")
