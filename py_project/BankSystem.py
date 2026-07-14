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
    