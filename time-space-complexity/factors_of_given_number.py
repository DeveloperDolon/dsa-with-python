from math import sqrt;

#  print all factors of a given number various algorithm

# 1. Brutforce solution TC -> O(N)/SC -> O(k)
num = 36;
num2 = 20;
num3 = 40;

result = [];

def basicFactor(num):
    for i in range(1, num + 1):
        if num % i == 0:
            result.append(i);
    return result;

print("Brutforce solution: ", basicFactor(num));

# 2. optimal solution TC -> O(N/2) / SC -> O(K)
def optimalSolution(num):
    result = [];
    for i in range(1, int(num / 2) + 1):
        if num % i == 0:
            result.append(i);
    
    result.append(num);
    return result;

print("Optimal solution: ", optimalSolution(num2));

# complex optimal solution TC -> O(sqrt(N)) + O(N Log N) / SC -> O(k)
def complexOptimalSolution(num):
    result = [];
    for i in range(1, int(sqrt(num)) + 1):
        if num % i == 0:
            result.append(i);

            if num // i != i:
                result.append(num // i);

    result.sort()
    return result;

print("Complex optimal solution : ", complexOptimalSolution(num));
