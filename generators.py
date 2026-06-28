def infinity_sequence():
    result = 1;

    while True:
        yield result;
        result *= 5;

values = 1;

def generatorFunc(numRange):
    gen = infinity_sequence();
    result = None;

    for i in range (numRange):
        result = next(gen);

    return result;

print(generatorFunc(4500));