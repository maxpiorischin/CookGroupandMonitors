import multiprocessing

class ez:
    def __init__(self,print):
        self.print = print
        self.queue = multiprocessing.Queue()
    def func(self):
        self.queue.put(self.print)

if __name__ == '__main__':
    mainn = ez('hi')
    print('hi')
    print (multiprocessing.Queue().get())


