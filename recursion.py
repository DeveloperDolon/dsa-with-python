# def greet(): #recursion program
#     print("Hello world");
#     greet();


# greet();


# Head recursion 
headRecursionCount = 0;
tailRecursionCount = 0;

def headRecursion(): # Time complexity -> O(N) / Space complexity -> O(N) //// 1 to N
    global headRecursionCount;
    if headRecursionCount == 4:
        return;

    headRecursionCount += 1;
    print("Hello world from Head Recursion!");
    # headRecursion();

# headRecursion();

def tailRecursion(): # Time complexity -> O(N) / Space complexity -> O(N) /// N to 1
    global tailRecursionCount;
    if tailRecursionCount == 4:
        return 
    
    tailRecursionCount += 1;
    tailRecursion();
    print("Hello world form Tail Recursion!");

# tailRecursion();


# recursion using parameters / Show x element n times 
def headParameterRecursion(x, n):
    if n == 0:
        return;

    print(x);

    headParameterRecursion(x, n - 1);


headParameterRecursion("Hello", 4);

def tailParameterRecursion(x, n):
    if n == 0:
        return;

    tailParameterRecursion(x, n-1);

    print(x);

tailParameterRecursion("World", 4);
