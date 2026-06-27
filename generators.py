def infinity_chai():
    count = 1;
    while True:
        yield f"Refill #{count}";
        count+=1;

refill = infinity_chai();

# for _ in range(6):
#     print(next(refill));


def chai_stall():
    try:
        while True:
            order = yield "Waiting for chai order";
    except:
        print("Stall closed, No more chai");

stall = chai_stall();

print(next(stall));
stall.close();