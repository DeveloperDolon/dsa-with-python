import time;

def myDecorator(function): 
    def wrapper(*args, **kwargs):
        func_value = function(*args, **kwargs);
        print('I decorate functions!');
        return func_value;

    return wrapper;

@myDecorator
def gratings(person):
    return f'Good afternoon {person}';

# print(gratings("Dolon Chandra Roy"));


# practical example logging function using decorate function 
def myLogging(function):
    def wrapper(*args, **kwargs):
        value = function(*args, **kwargs);
        with open('log_file.txt', 'a+') as f:
            fname = function.__name__
            print(f'{fname} function returned value : {value}');
            f.write(f'{fname}function returned value : {value}\n');

    return wrapper;

@myLogging
def simpleAddition(number1, number2):
    return number1 + number2;

# simpleAddition(10, 40);


# practical example of timing detection using decorate function 
def logTiming(function):
    def wrapper(*args, **kwargs):
        fname = function.__name__;
        startTime = time.time();
        value = function(*args, **kwargs);
        endTime = time.time();
        with open('log_file.txt', 'a+') as f:
            print(f'{fname} took {endTime - startTime} seconds to execute!');
            f.write(f'{fname} took {endTime - startTime} seconds to execute!\n')
            
        return value;

    return wrapper;


@logTiming
def hugeCounting(arg):
    result = 1;
    for i in range(arg):
        result += i;

    return result;

print(hugeCounting(100000000));