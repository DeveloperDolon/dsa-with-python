from multiprocessing import Process;
import time;

def coding():
    for i in range(1, 5):
        print(f"Coding for file number #{i}");
        time.sleep(1);

def deploying():
    for i in range(1, 5):
        print(f"Deploying project #{i}");
        time.sleep(2);

if __name__ == "__main__":
    codingProcess = Process(target=coding)
    deployingProcess = Process(target=deploying)

    codingProcess.start()
    deployingProcess.start()

    codingProcess.join()
    deployingProcess.join()

    print("All processes completed!")