# plaindrome example

num = 1234;

def checkPlaindrome(num):
    temp = num;
    result = 0;

    while temp > 0:
        ld = temp % 10;
        result = result * 10 + ld;
        temp = temp // 10;

    if num == result:
            print("Then number is a plaindrome!", num);
    else: 
        print("The number is not a plaindrome!", num);


checkPlaindrome(num);
checkPlaindrome(121);