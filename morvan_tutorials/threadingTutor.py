import threading
import time

def thread_job():
    print('T1 start\n')
    for i in range(10):
        time.sleep(0.1)
    print('T1 finish\n')

def T3_job():
    print('T3 start\n')
    for i in range(10):
        time.sleep(0.1)
    print('T3 finish\n')

def T2_job():        
    print('T2 start\n')
    thread3 = threading.Thread(target=T3_job,name = 'T3')
    thread3.start()
    thread3.join()
    print('T2 finish\n')

def main():
    added_thread = threading.Thread(target = thread_job, name='T1')
    thread2 = threading.Thread(target=T2_job,name = 'T2')
    added_thread.start()
    thread2.start()
    added_thread.join()
    # print(threading.active_count())
    # print(threading.enumerate())
    # print(threading.current_thread())
    print('all done')

if __name__ == '__main__':
    main()