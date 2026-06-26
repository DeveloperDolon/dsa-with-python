def makeToken(num):
    token = "";
    for i in range(num):
        token = token + str(i);

    return token;

# print(f"The token is : {makeToken(120)}")



orders = ["Dolon", "Dujoy", "Sarna", "Rakhi"];
bills = [1, 2, 3, 4, 5];

def printList(listOfOrder):
    for order in listOfOrder:
        print(f"Order is prepared for {order}");

def printEnumerate(orderList):
    for idx, name in enumerate(orderList, start=1):
        print(f'The index of {idx} is for : {name}');

# printEnumerate(orders)

def printOrderBillWithZip(orders, amounts): 
    for name, amount in zip(orders, amounts):
        print(f'{name} paid {amount} taka!');

# printOrderBillWithZip(orders, bills);

def printWithWhileLoop(loopRange):
    temp = 40;
    while temp < loopRange:
        print(f"The temperature is : {temp}");
        temp += 15;

    print('Chai is completed!');

# printWithWhileLoop(140)



def workWithForElse(docs):
    for name, age in docs:
        if age >= 80:
            print(f"{name} is eligible is to manage to staff!");
            break;
    else:
        print(f"No one is eligible to manage the staff");

staff = [("Dolon", 25), ("Durjoy", 22), ("Sarna", 23), ("Rakhi", 10), ("Sukharanjan roy", 80)];
workWithForElse(staff)