#!/usr/bin/python3
import threading
import timeit
import time
import intervals2

# Try out timeit.default_timer()
start = timeit.default_timer()
pass
end = timeit.default_timer()
print(end - start)

# Speed test for timeit.default_timer()
timeit.timeit(\
'''
start = timeit.default_timer()
pass
end = timeit.default_timer()
'''\
, 'import timeit', number=1000000)

# # Test multi-threading and joining threads using threading
# def sth(a,b,t):
#     time.sleep(t)
#     print(a+b)
#
# t1 = threading.Thread(target=sth,args=(1,2,5)) # 3rd
# t2 = threading.Thread(target=sth,args=(3,5,3)) # 2nd
# t1.start()
# t2.start()
# sth(4,9,1) # 1st
# t1.join()
# t2.join()

# Test intervals2.py Interval
def sth_else():
    print("Hello, world.")
    time.sleep(1)
    print("Bye, world.")
interval1 = intervals2.Interval(sth_else, .5, True)
def stopI1():
    interval1.cancel()
interval1.start()
threading.Timer(5, stopI1).start()
