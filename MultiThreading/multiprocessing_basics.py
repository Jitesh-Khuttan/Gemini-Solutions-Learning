import time
import multiprocessing

square_result = []

def calculate_square(arr):

    global square_result
    for element in arr:
        print("Square: ",element*element)
        square_result.append(element*element)
    print("In Process Result: ", square_result)

def main():
    arr = [2,3,4]

    process1 = multiprocessing.Process(target=calculate_square,args=(arr,))

    process1.start()
    process1.join()

    '''In MultiProcessing, the processes do not share variables.So this is why the main fxn
    result gives empty list. To share the variables we need to do IPC (interprocess Comm) '''

    print("Main Fxn Result: ", square_result)
main()