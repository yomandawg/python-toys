import a

from a import add_two as a2

print(dir(a))

def add_nine(num):
    return a2(num) + 7

print(add_nine(10))

a.check_main()

print("current is {}".format(__name__))