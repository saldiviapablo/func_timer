from datetime import datetime

def tiempo_total(func):
    def wrapper():
        initial_time = datetime.now()
        func()
        final_time = datetime.now()
        time_elapsed = final_time - initial_time
        print(f"Pasaron {time_elapsed.total_seconds()} segundos")
    return wrapper

@tiempo_total
def random_func():
    for _ in range(1, 1000000000):
        pass

random_func()