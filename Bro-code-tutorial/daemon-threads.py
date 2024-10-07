# daemon thread = a thread that runs in the background, not important for the program to run
#                 the program will not wait for daemon threads to complete before exiting
#                 non-daemon threads cannot normally be killed and stay alive till the task is completed
#
#                 eg. background tasks, garbage collections, waiting for input, long running processes

import threading
import time

def timer(): # eg of a bg process
    print()
    count = 0
    while True:
        time.sleep(1)
        count += 1
        print("logged in for: {} seconds".format(count))

# if we use a non daemon thread, it will continue to exist as long even after the main thread is
# finished
x = threading.Thread(target=timer, args=(), daemon=True) # converting into daemon thread
x.start()
# print(x.isDaemon())

answer = input("Do you want to exit")