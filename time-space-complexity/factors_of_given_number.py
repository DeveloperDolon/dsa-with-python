#  print all factors of a given number various algorithm

# 1. Brutforce solution TC -> O(N)/SC -> O(k)
num = 36;

result = [];

def basicFactor(num):
    for i in range(1, num + 1):
        if num % i == 0:
            result.append(i);
    return result;

print("Brutforce solution: ", basicFactor(num));
