from  multiprocessing import Process
import time

def brew_coffee(name):
    for i in range(3):
        print(f"Start: Brewing coffee {name}")
        time.sleep(3)
        print(f"End: Brewing coffee {name}")

if __name__ == "__main__":
    coffee_makers = [
        Process(target=brew_coffee, args=(f"By maker {i+1}", ))
        for i in range(3)
    ]

    for p in coffee_makers:
        p.start()

    for p in coffee_makers:
        p.join()
    print("All coffee done")
