"""
Task 1
A Person class

Make a class called Person. Make the __init__() method take firstname, lastname, and age as parameters
and add them as attributes. Make another method called talk() which makes prints a greeting from the person containing,
for example like this: “Hello, my name is Carl Johnson, and I’m 26 years old”.
"""


class Person():

    def __init__(self, firstname, lastname, age):
        self.firstname = firstname
        self.lastname = lastname
        self.age = age

    def talk(self):
        print(f'Hello, my name is {self.firstname} {self.lastname} and I’m {self.age} years old')


"""
Task 2
Doggy age

Create a class Dog with class attribute `age_factor` equals to 7.
Make __init__() which takes values for a dog’s age.
Then create a method `human_age` which returns the dog’s age in human equivalent.
"""


class Dog():

    age_factor = 7

    def __init__(self, dog_age):
        self.dog_age = dog_age

    def human_age(self):
        return Dog.age_factor * self.dog_age


"""
Task 3
TV controller

Create a simple prototype of a TV controller in Python. It’ll use the following commands:

first_channel() - turns on the first channel from the list.
last_channel() - turns on the last channel from the list.
turn_channel(N) - turns on the N channel. Pay attention that the channel numbers start from 1, not from 0.
next_channel() - turns on the next channel. If the current channel is the last one, turns on the first channel.
previous_channel() - turns on the previous channel. If the current channel is the first one, turns on the last channel.
current_channel() - returns the name of the current channel.
is_exist(N/'name') - gets 1 argument - the number N or the string 'name' and returns "Yes",
if the channel N or 'name' exists in the list, or "No" - in the other case.
 
The default channel turned on before all commands is №1.

Your task is to create the TVController class and methods described above.
"""


class TVController():

    now_current_channel = ''

    def __init__(self, channels: list):
        self.channels = channels
        TVController.now_current_channel = self.channels[0]

    def first_channel(self):
        TVController.now_current_channel = self.channels[0]
        print(self.channels[0])

    def last_channel(self):
        TVController.now_current_channel = self.channels[-1]
        print(self.channels[-1])

    def turn_channel(self, i):
        TVController.now_current_channel = self.channels[i-1]
        print(self.channels[i-1])

    def next_channel(self):
        if TVController.now_current_channel == self.channels[-1]:
            TVController.now_current_channel = self.channels[0]
            print(self.channels[0])
        else:
            cur_ind = self.channels.index(TVController.now_current_channel)
            next_ind = cur_ind + 1
            TVController.now_current_channel = self.channels[next_ind]
            print(self.channels[next_ind])

    def previous_channel(self):
        if TVController.now_current_channel == self.channels[0]:
            TVController.now_current_channel = self.channels[-1]
            print(self.channels[-1])
        else:
            cur_ind = self.channels.index(TVController.now_current_channel)
            next_ind = cur_ind - 1
            TVController.now_current_channel = self.channels[next_ind]
            print(self.channels[next_ind])

    def current_channel(self):
        print(TVController.now_current_channel)

    def is_exist(self, input_value):
        if isinstance(input_value, int):
            if input_value <= len(self.channels) + 1:
                print('Yes')
            else:
                print('No')
        elif isinstance(input_value, str):
            if input_value in self.channels:
                print('Yes')
            else:
                print('No')
        else:
            print('Unsupported input')

CHANNELS = ["BBC", "Discovery", "TV1000"]

controller = TVController(CHANNELS)

controller.first_channel()
controller.last_channel()
controller.turn_channel(1)
print(controller.current_channel)
controller.next_channel()
controller.previous_channel()
controller.current_channel()
controller.is_exist(4)
