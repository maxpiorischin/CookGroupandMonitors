from multiprocessing import Process
import time


def func1(num):
    print(num ** 2)
    time.sleep(1)


def func2(num):
    print(num ** 3)
    time.sleep(1)


if __name__ == '__main__':
    print('hello')  # why does this get printed over and over again?
    counter = 0
    while counter < 10:
        proc1 = Process(target=func1, args=(2,))
        proc2 = Process(target=func2, args=(2,))
        proc1.start()
        proc2.start()
        proc1.join()
        proc2.join()
        counter += 1
