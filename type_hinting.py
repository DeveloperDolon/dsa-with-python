def myFunc(arg: int) -> str: 
    return f"The number is : {arg}";

def otherFunc(arg: str):
    print(arg);

otherFunc(myFunc(5))