# SYNCHRONIZATION
'''
- In a multithreaded application we may be needed to coordinate(synchronize) the activities of the threads running 
  in it.
- The need to coordinate activities of threads will arise in two situations :
    a. When data or orther resources are to be shared amongst others
    b. When we need to carry out communication between threads.

There are three mechanisms for sharing resources : 
    (a). Lock
    (b). RLock
    (c). Semaphore
'''

#Program : Lock
import threading
count = 0
lock = threading.Lock() #lock object has been created

#function to increment count
def increment_count():
    global count
    
    lock.acquire() #acquiring the lock object to use count variable
    
    try:
        count+=1
    finally:
        lock.release() #releasing the lock for other threads to use

#Let's create multiple threads to increment count  
threads = []
for _ in range(5):
    thread = threading.Thread(target = increment_count)
    threads.append(thread)
    thread.start()
#Wait for all the threads to finish
for thread in threads:
    thread.join()
print("Final value of count : {}".format(count))

#RLock
'''
- Sometimes a recursive function may be invoked through multiple threads. Insuch case, if we use Lock to
  Provide sync access to shared variables it would lead to a problem-thread will be blocked when it attempts
  to aquired the same lock second time
'''

rlck = threading.RLock()
rlck.acquire()
rlck.acquire() #this won't block

#Semaphore
'''
- If we wish to permi access to a resource like network connection or a database server to a limited number of 
  threads we can do so using a semaphore object.
- A semaphore obj will a counter, not lock flag.
- Once the counter is set, for every acquire() call the counter decreases and for every .release() the counter
  increases.
- Blocking will occur when more than the set number of threads attempt to aquire the semaphore.
- We have to only initialize the counter to the maximum number while creating the semaphore object, and the 
  semaphore implementation takes the care of the rest
'''

#EVENTS AND CONDITIONS : 
'''
In Python's `threading` module, both `Event` and `Condition` are synchronization primitives that allow 
threads to communicate and coordinate their activities. They are useful when threads need to wait for 
certain conditions to be met before proceeding or when one thread needs to notify other threads about a
particular event.

'''
'''
1. `Event`:
An `Event` is a simple synchronization object that allows one or more threads to wait for a particular 
event to occur. The event can be set (indicating that the event has occurred) or cleared (indicating that 
the event is not yet signaled). Threads can wait for the event to be set using the `wait()` method, and they
can set the event using the `set()` method.
'''
#Program : 

import threading
import time

# Create an Event object
event = threading.Event()

# Function to wait for the event to be set
def wait_for_event():
    print("Waiting for the event to be set...")
    event.wait()
    print("Event has been set!")

# Function to set the event after a delay
def set_event_after_delay(delay):
    time.sleep(delay)
    print("Setting the event after a delay...")
    event.set()

# Create and start the threads
thread1 = threading.Thread(target=wait_for_event)
thread2 = threading.Thread(target=set_event_after_delay, args=(3,))  # Set the event after 3 seconds
thread1.start()
thread2.start()

# Wait for both threads to finish
thread1.join()
thread2.join()

print("All threads have finished.")

'''
In this example, `wait_for_event()` waits for the event to be set using `event.wait()`. Meanwhile, 
`set_event_after_delay()` sets the event after a delay of 3 seconds using `event.set()`.

2. `Condition`:
A `Condition` is a more complex synchronization primitive that allows multiple threads to coordinate 
based on a certain condition. It consists of a lock and a wait-notify mechanism. Threads can wait for
a condition to be true using the `wait()` method, and they can notify other threads about the condition 
change using the `notify()` or `notify_all()` methods.

'''
#Program :
import threading

# Shared resource
shared_variable = 0

# Create a Condition object
condition = threading.Condition()

# Function to increment the shared_variable
def increment_shared_variable():
    global shared_variable

    # Acquire the condition lock
    with condition:
        shared_variable += 1
        print(f"Shared variable incremented to {shared_variable}")

        # Notify other threads waiting for the condition
        condition.notify()

# Function to wait for the condition to be met
def wait_for_condition():
    with condition:
        while shared_variable < 5:
            print("Waiting for the condition to be met...")
            condition.wait()

        print("Condition has been met!")

# Create and start the threads
thread1 = threading.Thread(target=increment_shared_variable)
thread2 = threading.Thread(target=wait_for_condition)
thread1.start()
thread2.start()

# Wait for both threads to finish
thread1.join()
thread2.join()

print("All threads have finished.")
'''
In this example, `wait_for_condition()` waits for the condition `shared_variable >= 5` to be true using 
`condition.wait()`. Meanwhile, `increment_shared_variable()` increments the `shared_variable` and notifies 
other threads waiting for the condition using `condition.notify()`.

Both `Event` and `Condition` are powerful synchronization primitives that can be used to solve complex 
synchronization problems in multithreaded environments. The choice between `Event` and `Condition` depends 
on the specific requirements of the synchronization scenario you are dealing with.
'''
