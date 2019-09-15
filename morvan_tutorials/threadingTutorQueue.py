import threading
from queue import Queue

def thread_job(l,q):
    print('Thread start\n')
    for i in range(len(l)):
        l[i]=l[i]**2
    q.put(l)    

def main():
    q = Queue()
    threads = []
    data = [[1,2,3],[4,5,6],[4,4,4],[5,5,5]]
    for i in range(4):
        thread = threading.Thread(target = thread_job, args=(data[i],q))        
        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join()

    for _ in range(q.qsize()):
        print(q.get())
        print(q.qsize())

    print('all done')

if __name__ == '__main__':
    main()