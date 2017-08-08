""""
Puzzle: Rewrite the barrier solution so that after all
the threads have passed through, the turnstile is locked again.

The point of this exercise is that no threads can get more than
one turnstile away from the rest of the threads.
This is visible through the print lines.
The groups are consistently waiting at the same turnstiles.
"""
from random import randint
from threading import Semaphore, Thread

turnstile_1 = Semaphore(0)
turnstile_2 = Semaphore(1)
mutex = Semaphore(1)
count = 0
threads = 10


def code_loop(name):
	global turnstile_1
	global turnstile_2
	global mutex
	global count
	global threads

	mutex.acquire()
	count += 1
	if count == threads: 
		turnstile_2.acquire()
		turnstile_1.release()
	mutex.release()

	turnstile_1.acquire()
	print '{} is waiting at turnstile_1'.format(name)
	turnstile_1.release()

	# critical code

	mutex.acquire()
	count -= 1
	if count == 0:
		turnstile_1.acquire()
		turnstile_2.release()
	mutex.release()

	turnstile_2.acquire()
	print '{} is waiting at turnstile_2'.format(name)
	turnstile_2.release()


def run_code_loop(name, loops):
	print '{} is running {} times'.format(name, loops)
	for _ in xrange(loops):
		code_loop(name)


def execute(loops):
	"""
	Demonstrates the two-phase barrier solution with print lines.

	Args:
		loops (int): How many times to run the code block.

	Returns:
		None

		Prints lines.
	"""
	for x in xrange(threads):
		t = Thread(group=None, target=run_code_loop, name=str(x), args=str(x), kwargs={'loops':loops})
		t.start()



