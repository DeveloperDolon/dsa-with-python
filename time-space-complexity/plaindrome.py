# plaindrome example

num = 1234;

def checkPlaindrome(num):
    temp = num;
    result = 0;
    # time complexity is O(log10(n)) where n is the number of digits in the number
    # space complexity is O(1) as we are using a constant amount of space to store the result and temp variables
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