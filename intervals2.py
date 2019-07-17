from threading import Thread
from timeit import default_timer as timer
import time
from sys import stderr

class Interval:
    def __init__(self, fun, period, fixed = False):
        self.fun = fun
        self.period = period
        self.fixed = fixed
        self.start_time = None
        self.running = False

    def start(self):
        def thread1_content(host): # Unfixed, safety first.
            if not host.running:
                print("Error: this thread started stopped.", file = stderr)
            while host.running:
                if timer() - host.start_time >= host.period:
                    if host.fixed:
                        host.start_time += host.period
                        thread2 = Thread(target = host.fun)
                        thread2.start()
                    else:
                        host.start_time = timer()
                        host.fun()
        self.running = True
        self.start_time = timer()
        self.thread1 = Thread(target = thread1_content, args = (self,))
        self.thread1.start()

    def cancel(self):
        self.running = False
        self.thread1.join()
        del self.thread1
