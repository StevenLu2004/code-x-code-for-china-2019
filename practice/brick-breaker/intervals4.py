from threading import Thread
from timeit import default_timer as timer
import time
from sys import stderr

class Interval:
    def __defaultXsafeFunction():
        pass # Deliberately do nothing

    def __init__(self, fun, period, fixed = False, xsafe = True, xsafeFun = __defaultXsafeFunction):
        self.fun = fun
        self.period = period
        self.fixed = fixed
        self.xsafe = xsafe
        self.xsafeFun = xsafeFun
        self.start_time = None
        self.running = False
        self.thread1 = Thread()
        self.level_2_threads = []

    def checkLvl2(self):
        res = True
        delList = []
        for i in range(len(self.level_2_threads)):
            if not self.level_2_threads[i][1].is_alive():
                delList.append(i)
            elif not self.level_2_threads[i][0]:
                res = False
        for i in range(-len(delList) + 1, 1):
            del self.level_2_threads[delList[-i]]
        return res

    def start(self):
        def thread1_content(host):
            if not host.running:
                print("Error: this thread started stopped.", file = stderr)
            while host.running:
                if timer() - host.start_time >= host.period:
                    if host.fixed:
                        host.start_time += host.period
                        if (not host.xsafe) or host.checkLvl2():
                            thread2 = Thread(target = host.fun)
                            fxsafe = False
                        else:
                            thread2 = Thread(target = host.xsafeFun)
                            fxsafe = True
                        thread2.start()
                        self.level_2_threads.append((fxsafe, thread2))
                    else:
                        host.start_time = timer()
                        host.fun()
        self.running = True
        self.start_time = timer()
        self.thread1 = Thread(target = thread1_content, args = (self,))
        self.thread1.start()

    def cancel(self):
        self.running = False
        print("The property 'running' of this Interval object now has value {}.".format(self.running), file = stderr)
        for is_safe, level_2_thread in self.level_2_threads:
            if level_2_thread.is_alive():
                level_2_thread.join()
        self.thread1.join()
        print("Thread 1 has just ended.", file = stderr)
        self.level_2_threads = []
