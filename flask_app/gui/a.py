def add_two(num):
    return num + 2

def add_three(num):
    return num + 3

def add_four(num):
    return num + 4

print(1)

print(__name__)

def check_main():
    print("a is {}".format(__name__))

if __name__ == "__main__": # __name__ : execution context가 담겨있는 것
    print(add_two(10))
    print(add_three(10))
    print(add_four(10))