from queue import PriorityQueue


class Queue:
    def __init__(self) -> None:
        self.__queue_size = 0
        self.__queue = PriorityQueue(maxsize=self.__queue_size)
    
    def enqueue(self, message: str) -> None:
        self.__queue.put(message)
        return
    
    def dequeue(self):
        ...
    
    def size(self) -> int:
        return self.__queue.qsize()

queue = Queue()