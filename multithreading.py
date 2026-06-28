import threading;
import time;

def coding():
    for i in range(1, 5):
        print(f"Coding for file number #{i}");
        time.sleep(1);

def deploying():
    for i in range(1, 5):
        print(f"Deploying project #{i}");
        time.sleep(2);

codingThread = threading.Thread(target=coding);
deployingThread = threading.Thread(target=deploying);

codingThread.start();
deployingThread.start();

codingThread.join();
deployingThread.join();