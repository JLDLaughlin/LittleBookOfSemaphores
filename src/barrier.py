'''
Puzzle: Generalize the rendezvous problem to more than two threads.
Every thread should run the following code:

	rendezvous
	critical point
'''
from threading import Semaphore, Thread

n = 6
count = 0
mutex = Semaphore(1)
barrier = Semaphore(0)

def print_outs(name):
	global n
	global mutex
	global count
	global barrier

	print 'calculating {}'.format(name)

	mutex.acquire()
	count += 1
	mutex.release()

	if count == n:
		barrier.release()

	barrier.acquire()
	barrier.release()

	print '{} is at critical code'.format(name)


def quick_threads():
	for x in xrange(n):
		t = Thread(group=None, target=print_outs, name=str(x), args=str(x), kwargs=None)
		t.start()

	print 'done'




