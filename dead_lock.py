
import threading;

lock_one = threading.Lock();
lock_tow = threading.Lock();

def task_one():
    with lock_one:
        print('Lock one is accrued for task_one() method!')
        with lock_tow:
            print('Lock tow is accrued for task_one() method!')


def task_tow():
    with lock_tow:
        print('Lock tow is accrued for task_tow() method!')
        with lock_one:
            print('Lock one is accrued for task_tow() method!')


t1 = threading.Thread(target=task_one);
t2 = threading.Thread(target=task_tow);
t1.start();
t2.start();
t1.join();
t2.join();