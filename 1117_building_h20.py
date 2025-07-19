import threading
class H2O:
    def __init__(self):
        self.barrier=threading.Barrier(3)
        self.sem_o=threading.Semaphore(1)
        self.sem_h=threading.Semaphore(2)



    def hydrogen(self, releaseHydrogen: 'Callable[[], None]') -> None:
        self.sem_h.acquire()
        self.barrier.wait()
        
        # releaseHydrogen() outputs "H". Do not change or remove this line.
        releaseHydrogen()
        self.sem_h.release()


    def oxygen(self, releaseOxygen: 'Callable[[], None]') -> None:
        self.sem_o.acquire()
        self.barrier.wait()
        
        # releaseOxygen() outputs "O". Do not change or remove this line.
        releaseOxygen()
        self.sem_o.release()
