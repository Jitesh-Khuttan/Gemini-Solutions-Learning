import time
import multiprocessing


def calculate_square(arr,q):
    for element in arr:
        q.put(element*element)


def main():
    arr = [2, 3, 4]

    #q is a data structure(Queue) which acts as a shared memory between processes

    q = multiprocessing.Queue()

    process1 = multiprocessing.Process(target=calculate_square, args=(arr,q))

    process1.start()
    process1.join()

    while q.empty() is False:
        print(q.get())

main()