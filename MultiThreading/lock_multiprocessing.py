import time
import multiprocessing

def deposit(balance,lock):

    for i in range(100):
        time.sleep(0.1)
        lock.acquire()
        balance = balance + 1;
        lock.release()

def withdraw(balance,lock):

    for i in range(100):
        time.sleep(0.1)
        lock.acquire()
        balance = balance - 1;
        lock.release()

def main():

    shared_v = multiprocessing.Value('i',200)
    lock = multiprocessing.Lock()

    process_deposit = multiprocessing.Process(target=deposit,args=(shared_v,lock))
    process_withdraw = multiprocessing.Process(target=withdraw,args=(shared_v,lock))

    print(shared_v.value)
main()