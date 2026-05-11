import threading
import time

def take_order():
    for i in range(5):
        print(f"Taking order {i}")
        time.sleep(2)

def prepare_order():
    for i in range(5):
        print(f"Preparing coffee {i}")
        time.sleep(5)


order = threading.Thread(target=take_order)
prepare = threading.Thread(target=prepare_order)

order.start()
prepare.start()
order.join()
prepare.join()
print(f"Finished all tasks")
# wait for both to finish