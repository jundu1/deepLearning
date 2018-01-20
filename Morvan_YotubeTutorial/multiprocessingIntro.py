# View more python learning tutorial on my Youtube and Youku channel!!!

# Youtube video tutorial: https://www.youtube.com/channel/UCdyjiB5H8Pu7aDTNVXTTpcg
# Youku video tutorial: http://i.youku.com/pythontutorial

import multiprocessing as mp
import copy
import time

def job(l, q):
    # global lock
    # lock.acquire()
    res = sum(l)
    q.put(res)
    # lock.release()
    
def multicore(l):    
    q = mp.Queue()
    processings = []
    for i in range(4):
        p = mp.Process(target=job, args=(copy.copy(l), q), name='T%i' % i)
        p.start()
        processings.append(p)
    [p.join() for p in processings]
    total = 0
    for _ in range(4):
        total += q.get()
    print(total) 

def normal(l):
    total = sum(l)
    print(total)

if __name__ == '__main__':
    l = list(range(1000000))
    s_t = time.time()
    normal(l*4)
    print('normal: ',time.time()-s_t)
    s_t = time.time()
    multicore(l)
    print('multicore: ', time.time()-s_t)