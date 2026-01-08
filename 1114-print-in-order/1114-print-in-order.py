from threading import Lock

class Foo:
    def __init__(self):
        self.lock = [Lock(), Lock()]
        self.lock[0].acquire()
        self.lock[1].acquire()
        print(self.lock)


    def first(self, printFirst: 'Callable[[], None]') -> None:
        
        # printFirst() outputs "first". Do not change or remove this line.
        printFirst()
        self.lock[0].release()


    def second(self, printSecond: 'Callable[[], None]') -> None:
        
        # printSecond() outputs "second". Do not change or remove this line.
        self.lock[0].acquire()
        printSecond()
        self.lock[0].release()
        self.lock[1].release()


    def third(self, printThird: 'Callable[[], None]') -> None:
        self.lock[1].acquire()
        # printThird() outputs "third". Do not change or remove this line.
        printThird()
        self.lock[1].release()