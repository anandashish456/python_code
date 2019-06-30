from multiprocessing import Process, Lock
import time, os

def sq():
    global a
    print("Starting thread 1 with PID: {}".format(os.getpid()))
    lock.acquire()
    a += 2
    print(10*10)
    time.sleep(10)
    print(a)
    lock.release()


def cubes():
    global a
    print("Starting thread 2 with PID: {}".format(os.getpid()))
    lock.acquire()
    a += 3
    print(10*10*10)
    print(a)
    lock.release()


if __name__ == '__main__':
    a = 2

    print ("Starting main thread with PID: {}".format(os.getpid()))

    lock = Lock()

    p1 = Process(target=sq)
    p2 = Process(target=cubes)

    p1.start()
    p2.start()

    p1.join()
    p2.join()

    print("Main thread is over")    
