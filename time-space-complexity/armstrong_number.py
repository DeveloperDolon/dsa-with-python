
# the exercise of armstrong numbers
# the time complexity is O(log10(n))
# the space complexity is O(1)

num = 153;

def checkArmstrong(num):
    temp = num;
    nod = len(str(temp));
    total = 0;

    while temp > 0:
        ld = temp % 10;
        total = total + (ld ** nod);
        temp = temp // 10;

    if total == num:
        print("The number is armstrong number: ", num);
    else: 
        print("Then number is not armstrong number: ", num);


checkArmstrong(num);
checkArmstrong(76);
