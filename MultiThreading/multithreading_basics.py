
import time
import threading

def calcuate_square(arr):

    for element in arr:
        time.sleep(0.2)
        print("Square: ",element*element)

def calculate_cube(arr):

    for element in arr:
        time.sleep(0.2)
        print("Cube: ",element*element*element)

def main():

    arr = [2,3,4,5]

    startTime = time.time()
    #
    # calcuate_square(arr)
    # calculate_cube(arr)
    #
    # print("Total Time Needed: ",time.time() - startTime)

    thread1 = threading.Thread(target=calculate_cube,args=(arr,))
    thread2 = threading.Thread(target=calcuate_square,args=(arr,))

    thread1.start()
    thread2.start()

    thread1.join()
    thread2.join()


    print("Total Time Needed: ",time.time() - startTime)

if __name__ == '__main__':
    main()
