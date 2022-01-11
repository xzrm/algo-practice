
class Test:
    @staticmethod
    def decorate(func):
        def wrapper(*args, **kwargs):
            print("1")
            func(*args, **kwargs)
            print("2")
        return wrapper


@Test.decorate
def f():
    print("aaa")

f()




def decorate(func):
    def wrapper(*args, **kwargs):
        print("1")
        func(*args, **kwargs)
        print("2")
    return wrapper

def a():
    print('b')

a_doc = decorate(a)
def b():
    print('c')
    a_doc()



