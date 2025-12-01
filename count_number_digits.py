
# count number of digits with white loop

count = 0;
num = 5438;

while(num > 0):
    num = num // 10;
    count += 1;
    print("Current num:", num, " Current count:", count);

print("Number of digits:", count);


# count number of digits with log function
from math import *;

def countDigits(n):
    if(n == 0):
        return 1;
    return int(log10(n)) + 1;

print("Number of digits (using log):", countDigits(5438));
