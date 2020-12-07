import socket
import threading
from threading import Thread
import sys
import time
import random
import math
from queue import Queue


class ThreadPoolManager():
    def __init__(self, thread_num):
        self.work_queue = Queue()
        self.thread_num = thread_num
        self.__init_threading_pool(self.thread_num)

    def __init_threading_pool(self, thread_num):
        for i in range(thread_num):
            thread = ThreadManager(self.work_queue)
            thread.start()

    def add_job(self, func, *args):
        self.work_queue.put((func, args))


class ThreadManager(Thread):
    def __init__(self, work_queue):
        Thread.__init__(self)
        self.work_queue = work_queue
        self.daemon = True

    def run(self):
        while True:
            target, args = self.work_queue.get()
            target(*args)
            self.work_queue.task_done()


thread_pool = ThreadPoolManager(4)


def child_connection(index, sock, connection):
    try:
        print("begin connection %d" % index)
        connection.settimeout(50)
        while True:
            buf = connection.recv(1024)
            if (buf.split(str.encode(' '))[0] == str.encode("ADD")):
                length = int((buf.split(str.encode('\n'))[
                             1]).split(str.encode(' '))[2])
            else:
                length = None
            print(length)
            print(buf)
            if length != None and length != 0:
                num = math.ceil(length / 1024)
                pic = str.encode("")
                print("The file will be", buf, "bytes")
                connection.sendall(str.encode("allowed"))
                for i in range(0, num):
                    picsec = connection.recv(1024)
                    pic += picsec
                ans = open('/home/hatsunehan/图片/test.png', 'wb')
                ans.write(pic)
                connection.sendall(str.encode("finished"))
                print("receive successfully")
            elif buf == str.encode('end'):
                print("close")
                break
            else:
                connection.send(b"please go out!")
                print("send refuse")

    except socket.timeout:
        print("time out")
    print("closing connection %d" % index)
    connection.close()


if __name__ == "__main__":
    print("Server is starting")
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.bind(('127.0.0.1', 8992))
    sock.listen(5)
    print("Server is listening port 8001, with max connection 5")
    index = 0
    while True:

        connection, address = sock.accept()
        index += 1
        thread_pool.add_job(child_connection, *(index, sock, connection))
        if index > 5:
            break

sock.close()
