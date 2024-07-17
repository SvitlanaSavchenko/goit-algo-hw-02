import queue
import threading
import time
import random

request_queue = queue.Queue()
exit_flag = False  # Змінна-флаг для контролю виходу з програми

def generate_request():
    try:
        while not exit_flag:
            request_id = random.randint(1, 1000)
            request_queue.put(request_id)
            print(f"Заявка {request_id} додана до черги.")
            time.sleep(random.uniform(0.5, 2.0))
    except Exception as e:
        print(f"Сталася помилка під час генерації заявок: {e}")

def process_request():
    try:
        while not exit_flag or not request_queue.empty():
            if not request_queue.empty():
                request_id = request_queue.get()
                print(f"Заявка {request_id} обробляється...")
                time.sleep(random.uniform(1.0, 3.0))
            else:
                print("Черга заявок порожня.")
                time.sleep(1.0)
    except Exception as e:
        print(f"Сталася помилка під час обробки заявок: {e}")

try:
    gen_thread = threading.Thread(target=generate_request)
    process_thread = threading.Thread(target=process_request)

    gen_thread.start()
    process_thread.start()

    input("Натисніть Enter, щоб завершити виконання...\n")
    exit_flag = True  # Встановлюємо флаг для завершення виконання

    gen_thread.join()
    process_thread.join()

except KeyboardInterrupt:
    print("\nПрограма завершила роботу через введення Ctrl+C")

except Exception as e:
    print(f"Сталася критична помилка: {e}")

finally:
    print("Програма завершила роботу.")

