
# count number of digits with white loop

count = 0;
num = 5438;

while(num > 0):
    num = num // 10;
    count += 1;
    print("Current num:", num, " Current count:", count);

print("Number of digits:", count);
