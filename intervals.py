#!/usr/bin/python3
import threading
import sys

class Timeout:
	def __init__(self, fn, tm):
		self.fn = fn
		self.tm = tm
	def start(self):
		def timeout(holder):
			holder.timer = threading.Timer(holder.tm, holder.fn)
			holder.timer.start()
		timeout(self)
	def end(self):
		self.timer.cancel()
		del self.timer

class Interval:
	def __init__(self, fn, tm, fixed = False):
		self.fn = fn
		self.tm = tm
		self.fixed = fixed
	def start(self):
		def timeout(holder):
			def wrapper():
				if holder.fixed:
					timeout(holder)
					holder.fn()
				else:
					holder.fn()
					timeout(holder)
			holder.timer = threading.Timer(holder.tm, wrapper)
			holder.timer.start()
		timeout(self)
	def end(self):
		self.timer.cancel()
		del self.timer

def main():
	def f1():
		print("Hello, world.")
	interval = Interval(f1, .2)
	def f2():
		interval.end()
	timeout = Timeout(f2, 1.01)
	interval.start()
	timeout.start()

if __name__ == "__main__":
	main()
