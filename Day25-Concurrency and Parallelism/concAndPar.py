'''
In Python, concurrency and parallelism are concepts related to managing multiple tasks or processes to achieve better performance and efficiency. While they share similarities, they serve different purposes:

1. Concurrency:
Concurrency refers to the ability of a program to handle multiple tasks simultaneously, without necessarily running them at the same time. 
It enables efficient task switching and interleaving execution, allowing the program to make progress on different tasks without waiting 
for each task to complete before moving to the next one. Concurrency is particularly useful when dealing with I/O-bound 
operations (e.g., reading/writing files, making network requests) and can help prevent a program from becoming unresponsive.

In Python, concurrency can be achieved using various approaches, such as:
- Threading: The `threading` module allows you to create and manage threads, each executing a specific task. However, due to Python's 
  Global Interpreter Lock (GIL), which prevents multiple threads from executing Python bytecode in parallel, threading may not always result 
  in true parallelism. It can still be beneficial in handling I/O-bound tasks.
- Asynchronous I/O (asyncio): The `asyncio` module allows you to write asynchronous code using coroutines and event loops. Asynchronous programming allows tasks to pause and resume, making it suitable for managing I/O-bound tasks with potential efficiency gains.

2. Parallelism:
Parallelism, on the other hand, involves executing multiple tasks or processes simultaneously by utilizing multiple CPU cores. It is suitable for CPU-bound operations that require significant computational power. In contrast to concurrency, parallelism aims to achieve true simultaneous execution, effectively utilizing multiple cores to perform computations faster.

In Python, achieving true parallelism is often done using the following methods:
- Multiprocessing: The `multiprocessing` module allows you to create and manage multiple processes in Python. Each process operates independently and has its memory space, which bypasses the limitations of the GIL and enables true parallelism across CPU cores.
- Joblib: The `joblib` library is often used for parallelizing tasks that involve heavy computation using the `Parallel` function.

It's important to note that the choice between concurrency and parallelism depends on the nature of the tasks and the resources available.
Concurrency is more suitable for I/O-bound tasks, while parallelism is beneficial for CPU-bound tasks. Additionally, achieving parallelism 
may require extra overhead due to process creation and data communication among processes, so it's essential to benchmark and assess the 
performance gains in your specific use case.
'''

#Types of Concurrencies : 
'''
1. Preemptive concurrency : threading
2. Cooperative concurrency : asyncio
3. Parallelism : multiprocessing
'''

import threading
t = threading.current_thread()
print("Current thread : ",t)
print("Thread name : ",t.name)
print("Thread identifier : ",t.ident)
print("Is thread alive : ",t.is_alive())
t.name = "MyThread"
print("After name change : ",t.name)


def func1():
    print("My name is Rahman")
def func2():
    print("Python is a Language")

print('_'*120)
print('Launching threads using first method\n')
#LAUNCHING THREADS - Method(1)
th1 = threading.Thread(name='My first thread', target = func1)
th2 = threading.Thread(target=func2)
th1.start()
th2.start()

print('_'*120)
print('Launching threads using second method\n')
#LAUNCHING THREADS - Method(2)
class SquareGeneratorThread(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)
    def run(self):
        print("Launching...")
th = SquareGeneratorThread()
th.start()

print('_'*120)
print('Passing parameters to the thread\n')
#PASSING PARAMETERS TO THE THREAD

#Program - Without passing args
import time
def fun1():
    t= threading.current_thread()
    print('Starting',t.name)
    time.sleep(1)
    print('Exiting',t.name)
def fun2():
    t = threading.current_thread()
    print("Starting",t.name)
    time.sleep(1)
    print('Exiting',t.name)
def fun3():
    t= threading.current_thread()
    print('Starting',t.name)
    time.sleep(1)
    print('Exiting',t.name)

t1 = threading.Thread(target=fun1)
t2 = threading.Thread(target=fun2)
t3 = threading.Thread(target=fun3)
t1.start()
t2.start()
t3.start()

print('_'*120)
print('Threads having args\n')
#Program - With passing args
def squares(arr):
    print('Calculating squares : ')
    for n in arr : 
        time.sleep(0.5)
        print('n = ',n,'square=',n*n)
def cubes(arr):
    print('Calculating cubes : ')
    for n in arr : 
        time.sleep(0.5)
        print('n = ',n,'cube=',n*n*n)

arr = [1,2,3,4,5]
startTime = time.time()
squares(arr)
cubes(arr)
endTime = time.time()
print('Time took : ',endTime-startTime,'sec')






