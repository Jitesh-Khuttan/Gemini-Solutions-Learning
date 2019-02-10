import threading
import time

""" We can override 2 methods of class threading.Thread. 
    1. __init__() method
    2. run() method
    Basically run() method is responsible for calling the callable object i.e. the function
    that we pass as a Target to the Thread Class."""

class MyThread(threading.Thread):

    def __init__(self,number,func,args):
        super().__init__()
        self.number = number
        self.func = func
        self.args = args

    def run(self):
        print("{} function has started.".format(self.number))
        self.func(*self.args)    #Calling the target function
        print("{} function has ended".format(self.number))


def calculate_square(number):
    print("Square of the number {} is {}".format(number,number*number))

def main():

    threads_list = []

    for i in range(10):
        t = MyThread(i+1,calculate_square,(i+1,))
        threads_list.append(t)
        t.start()

    for i in range(10):
        threads_list[i].join()

main()
