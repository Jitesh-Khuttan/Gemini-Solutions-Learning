import time
import multiprocessing

def calculate_square(arr,result,v):

    v.value = 3.45
    for index,element in enumerate(arr):
        print("Square: ",element*element)
        result[index] = element*element
    print("In Process Result: ", result[:])

def main():

    arr = [2,3,4]

    #This is how we share the variables between processes
    result = multiprocessing.Array('i',3)
    v = multiprocessing.Value('d',2.93)
    
    process1 = multiprocessing.Process(target=calculate_square,args=(arr,result,v))

    process1.start()
    process1.join()

    print("Main Fxn Result: ", result[:], " Value: ",v.value)
main()