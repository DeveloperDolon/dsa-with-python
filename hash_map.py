# has map with python
n = [5, 3, 2, 2, 1, 5, 5, 7, 5, 10];
m = [4, 6, 77, 43, 5, 3, 4, 6, 10];

# very basic method for hash map TC -> O(m*n) / SC -> O(1)
def createHashMap(n, m):
    for i in m:
        count = 0;
        for j in n:
            if j == i:
                count += 1;
        print('Count of', i, ' is ', count);

createHashMap(n, m);

print("---------------------------------");

# optimal method for hash map TC = O(m+n) / SC -> O(1)
def optimalHashMap(n, m):
    hash_list = [0] * 11;

    for num in n:
        hash_list[num] += 1;

    for num in m:
        if num < 1 or num > 10:
            print("Count of ", num, " is ", 0);
        else: 
            print("Count of ", num, " is ", hash_list[num]);

optimalHashMap(n, m);

print("---------------------------------");

# Hash mapping with dictionary TC -> O(N+M) and SC -> O(N)
def hashMapWithDictionary(n, m):
    hash_list = {};

    for num in n:
        hash_list[num] = hash_list.get(num, 0) + 1;
    
    for num in m:
         if num < 1 or num > 10:
             print("Count of ", num, " is ", 0);
         else:
            print('Count of ', num, ' is ', hash_list.get(num, 0));

    print(hash_list);


hashMapWithDictionary(n, m);
