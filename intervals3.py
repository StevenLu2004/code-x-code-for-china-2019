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
        self.thread1 = Thread()
        self.level_2_threads = []

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
                        self.level_2_threads.append(thread2)
                    else:
                        host.start_time = timer()
                        host.fun()
        self.running = True
        self.start_time = timer()
        self.thread1 = Thread(target = thread1_content, args = (self,))
        self.thread1.start()

    def cancel(self):
        self.running = False
        for level_2_thread in self.level_2_threads:
            if level_2_thread.is_alive():
                level_2_thread.join()
        self.thread1.join()
        self.level_2_threads = []
