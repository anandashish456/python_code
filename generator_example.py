import time

l = []


def normal_list():
    for i in range(1000000):
        l.append(i)
    return l


def generator_list():
    for i in range(1000000):
        l.append(i)
    yield l


t1 = time.clock()
#lists = normal_list()
lists = generator_list()
t2 = time.clock()

print((str(t2-t1)))
