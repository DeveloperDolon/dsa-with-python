class User:
    def __init__(self, name, age, address):
        self.__name = name
        self.__age = age
        self.__address = address

    @property
    def name(self):
        return self.__name

    @property
    def age(self):
        return self.__age

    @property
    def address(self):
        return self.__address

    @property
    def user_info(self):
        return {
            "name": self.__name,
            "age": self.__age,
            "address": self.__address
        }

class Bank:
    users = []

    def __init__(self, name, total_balance, user_limit, interest):
        self.__name = name
        self.__total_balance = total_balance
        self.__user_limit = user_limit
        self.__interest = interest

    def _add_user(self, user):
        self.users.append(user)

    @property
    def bank_name(self):
        return self.__name

    def _add_balance(self, balance):
        self.__total_balance += balance

    def _add_user_limit(self, user_limit):
        self.__user_limit += user_limit

    def _add_interest(self, interest):
        self.__interest += interest

    def _set_balance(self, balance):
        self.__total_balance = balance

    def _set_user_limit(self, user_limit):
        self.__user_limit = user_limit

    def _set_interest(self, interest):
        self.__interest += interest

    def _bank_info(self):
        return {
            "name": self.__name,
            "total_balance": self.__total_balance,
            "user_limit": self.__user_limit,
            "interest": self.__interest
        }
    
    def public_bank_info(self):
        remaining_user_count = self.__user_limit - len(self.users)

        return {
            "name": self.__name,
            "interest": self.__interest,
            "remaining_user": remaining_user_count
        }

class RunSystem:
    banks = []

    def run(self):
        sonali_bank = Bank("Sonali Bank Ltd.", 5000000, 500, 10)
        brack_bank = Bank("Brack Bank Ltd.", 2000000, 300, 7)
        self.__add_bank(sonali_bank)
        self.__add_bank(brack_bank)

        while True:
            print("Welcome to Bank system🎉")

            print("""
            Options (input number to chose option): 
                1. Add bank
                2. Add user
                3. See banks information
                4. exit
            """)

            chose = input("Input option number: ")

            match chose:
                case "1":
                    self.__add_bank_info()
                case "2":
                    self.__add_user()
                case "3":
                    self.__bank_details_showing()
                case "4":
                    print("Exited")
                    break
                case _:
                    print("No option selected!")

    def __add_bank_info(self):
        print("Input information to add bank. \n")

        bank_name = input("Bank name: ")
        bank_total_balance = input("Bank total balance: ")
        bank_user_limit = input("Bank user limit: ")
        bank_interest = input("Bank interest: ")

        new_bank = Bank(
            bank_name, 
            int(bank_total_balance), 
            int(bank_user_limit), 
            int(bank_interest)
        )

        self.__add_bank(new_bank)
        print("The bank has been successfully added✅")

    def __bank_details_showing(self):
        print("Chose bank to show details: \n")
        
        for index, bank in enumerate(self.banks, 1):
            print(f"{index}. {bank.bank_name}")

        user_input = input("Enter option number: ")
        chose_bank = self.banks[int(user_input) - 1].public_bank_info()
        
        print(f"""
            Bank Name: {chose_bank['name']}
            Interest Rate: {chose_bank['interest']}%
            Remaining User: {chose_bank['remaining_user']}
        """)

    def __add_bank(self, bank):
        self.banks.append(bank)

    def __add_user(self):
        print("Which bank you want to add user: \n")
        
        for index, bank in enumerate(self.banks, 1):
            print(f"{index}. {bank.bank_name}")

        user_input = input("Enter option number: ")
        chose_bank = self.banks[int(user_input) - 1]

        print("Input user information: \n")

        user_name = input("Input username: ")
        user_age = input("Input age: ")
        address = input("Input address: ")

        new_user = User(user_name, user_age, address)

        chose_bank._add_user(new_user)

        print(f"User added to the {chose_bank.bank_name}✅")

        
bankSystem = RunSystem()
bankSystem.run()
