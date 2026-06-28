import threading;
import time;

count = 0;
lock = threading.Lock();

def increment():
    global count;

    for _ in range(0, 200):
        with lock:
            count+=1;
    
threads = [threading.Thread(target=increment) for _ in range(5)];

start = time.time();

[t.start() for t in threads];
[t.join() for t in threads];

end = time.time();

print(f"Threads are executed with {end - start:.2f} seconds...");
print(f'Count is : {count}');