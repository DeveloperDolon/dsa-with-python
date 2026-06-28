from multiprocessing import Process, Value
# count = 0;
# def work():
#     global count;
#     for i in range(5):
#         count+= 1;
#         print(count)

# if __name__ == "__main__":
#     p1 = Process(target=work)
#     p2 = Process(target=work)

#     p1.start()
#     p2.start()

#     p1.join()
#     p2.join()

# print("Final value of the multiprocessing: ", count);

def work(count):
    for _ in range(5):
        with count.get_lock():  # synchronize access
            count.value += 1

if __name__ == "__main__":
    count = Value('i', 0)

    p1 = Process(target=work, args=(count,))
    p2 = Process(target=work, args=(count,))

    p1.start()
    p2.start()

    p1.join()
    p2.join()

    print("Final value:", count.value)  # 10