import threading
import time
import queue

count = 0

def calculate_square(q,name):
    global count
    print("Thread {} Started ".format(name))
    while not q.empty():
        elem = q.get()
        print("Thread {} calculated: {}".format(name,elem*elem))
        count += 1

def main():


    result_threads = []
    start = time.time()
    q = queue.Queue()

    for element in range(100):
        q.put(element)

    for i in range(2):
        t = threading.Thread(target=calculate_square,args=(q,i+1))
        result_threads.append(t)
        t.start()

    for thread in result_threads:
        thread.join()

    end = time.time()

    global count
    print ("So time taken for execution: {}".format(end-start))
    print ("Count = {}".format(count))

main()