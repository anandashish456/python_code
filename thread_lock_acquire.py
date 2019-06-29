import threading
import os
import time

def sq(num):
    global a
    print(f"Starting thread {threading.current_thread().name} with pid {os.getpid()}")
    lock.acquire()
    time.sleep(5)
    print(num*num)
    a += 2
    print(a)
    lock.release()


def cube(num):
    global a
    print (f"Starting thread {threading.current_thread().name} with pid {os.getpid()}")
    lock.acquire()
    time.sleep(10)
    print(num*num*num)
    a += 3
    t1.start()
    print(a)
    t1.join()
    lock.release()


if __name__ == '__main__':
    a = 2
    print(f"Starting the main thread {threading.main_thread().name} with pid {os.getpid()}")
    
    lock = threading.Lock()

    t1 = threading.Thread(target=sq, args=(10,), name='Square Thread')
    t2 = threading.Thread(target=cube, args=(10,), name='Cube Thread')

    t2.start()
    #t1.start()

    #t1.join()
    t2.join()

    print("I am done!!")

