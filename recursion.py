# def greet(): #recursion program
#     print("Hello world");
#     greet();


# greet();


# Head recursion 
headRecursionCount = 0;
tailRecursionCount = 0;

def headRecursion(): # Time complexity -> O(N) / Space complexity -> O(N)
    global headRecursionCount;
    if headRecursionCount == 4:
        return;

    headRecursionCount += 1;
    print("Hello world from Head Recursion!");
    headRecursion();

headRecursion();

def tailRecursion(): # Time complexity -> O(N) / Space complexity -> O(N)
    global tailRecursionCount;
    if tailRecursionCount == 4:
        return 
    
    tailRecursionCount += 1;
    tailRecursion();
    print("Hello world form Tail Recursion!");

tailRecursion();