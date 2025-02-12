import greetings
import importlib
import time


greetings.say_hello()

time.sleep(10)


importlib.reload(greetings)

greetings.say_hello()
