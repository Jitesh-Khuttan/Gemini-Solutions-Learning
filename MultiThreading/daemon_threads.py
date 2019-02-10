

''' Daemon Threads are the threads which gets stopped implicitly when the main thread ends.
    For eg: In the program, we have a checkItem() which only has a task of keeping a check on
    other two functions. Since there is a INFINITE LOOP running inside the fxn, we want that it
    should end, as soon as the main thread ends. So we will make this thread as a Daemon Thread.'''

import threading
import time
value = 4

def addItem1():

    global value
    for i in range(10):
        time.sleep(1)
        value += 1
        print("Value Added")

def addItem2():

    global value
    for i in range(10):
        time.sleep(1)
        value += 2
        print("Value Added")

def checkItem():

    global value
    while True:
        if value > 4:
            value -= 3
            print("Subtracted 3")
        else:
            time.sleep(2)
            print("Waiting")

def main():


    thread1 = threading.Thread(target = addItem1,name = 'thread1')
    thread2 = threading.Thread(target = addItem2,name = 'thread2')
    thread3 = threading.Thread(target = checkItem,name = 'checkerThread',daemon=True)

    thread1.start()
    thread2.start()

    thread1.join()
    thread2.join()

    print("Main Function is Finished")

if __name__ == "__main__":
    main()