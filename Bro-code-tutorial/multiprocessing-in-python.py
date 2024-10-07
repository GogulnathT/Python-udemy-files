# multiprocessing = running tasks on parallel on different cpu cores, bypass the GIL used for
#                   threading
#                   multiprocessing -> better for cpu bound tasks(heavy cpu usage)
#                   multithreading ->  better for io bound tasks(waiting around)

from multiprocessing import Process, cpu_count
import time

def counter(num):
    count = 0
    while count < num:
        count += 1

def main():

    print(cpu_count()) # returns the no. of cpu core

    # a = Process(target=counter, args=(100000,)) # this is also a way to do the same, older method
    # a = Process(target=counter(100000)) # instead of using a single process we can divide it
    a = Process(target=counter(25000))
    b = Process(target=counter(25000))
    c = Process(target=counter(25000))
    d = Process(target=counter(25000))

    a.start()
    b.start()
    c.start()
    d.start()

    a.join() # main process will wait for child process; syncing
    b.join()
    c.join()
    d.join()

    print("finished in : ",time.perf_counter()," secs")

if __name__ == '__main__':
    main()