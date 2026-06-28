
flavors = ['vanilla', 'chocolate', 'strawberry', 'mint']

while (flavor := input("Enter your favorite ice cream flavor (or 'quit' to exit): ")) not in flavors:
    print(f"Sorry, {flavor} is not a valid option.")
else:
    print(f"{flavor} is one of our popular flavors!")