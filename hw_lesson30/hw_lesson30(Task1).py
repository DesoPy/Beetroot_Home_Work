import threading


"""
Task 1

A shared counter

Make a class called Counter, and make it a subclass of the Thread class in the Threading module.
Make the class have two global variables, one called counter set to 0, and another called rounds set to 100.000.
Now implement the run() method, let it include a simple for-loop that iterates through rounds (e.i. 100.000 times)
and for each time increments the value of the counter by 1. Create 2 instances of the thread and start them,
then join them and check the result of the counter, it should be 200.000, right?
Run it a couple of times and consider some different reasons why you get the answer that you get.
"""


class Counter(threading.Thread):
    counter = 0
    rounds = 100000

    def run(self):
        for i in range(self.rounds):
            self.counter += 1


counter_1 = Counter()
counter_2 = Counter()
counter_1.start()
counter_2.start()
counter_1.join()
counter_2.join()
print(counter_1.counter)
print(counter_2.counter)
