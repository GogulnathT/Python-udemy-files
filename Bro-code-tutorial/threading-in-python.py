# thread = a flow of execution like a separate order of instructions
#          however each thread takes a turn running to achieve concurrency
#          GIL -> global interpreter lock -> allows only one thread to hold the control of
#          the python interpreter at any one time

# categories of programs
# cpu bound = a program/task spends most of it's time waiting for internal events(CPU intensive)
#             better to use multiprocessing for cpu bound

# io bound = a program/task spends most of it's time waiting for external events(eg. user input, web scraping)
#            better to use multithreading for io bound

# note = multithreading will have multiple process in concurrency but it is not true multiprocessing

import threading
import time

def eat_breakfast():
    time.sleep(3) # makes the thread sleep for 3 secs
    print("Finished eating")

def drink_coffee():
    time.sleep(4)
    print("Finished drinking")

def study():
    time.sleep(5)
    print("Finished studying")

x = threading.Thread(target=eat_breakfast, args=())
x.start()

y = threading.Thread(target=drink_coffee, args=())
y.start()

z = threading.Thread(target=study, args=())
z.start()
# the main thread is no longer in charge of the functions and they are controlled by the threads
# also main thread wont wait for other threads and will be executed
# these additional threads are created by the main thread

# thread synchronisation
x.join() # the main thread has to wait on till the x thread is finished
y.join()
z.join()

# eat_breakfast()
# drink_coffee()
# study()
# main thread is responsible for running these functions sequentially so 12 secs will be taken

print(threading.active_count())
print(threading.enumerate()) # prints all the threads in the program
print(time.perf_counter())
