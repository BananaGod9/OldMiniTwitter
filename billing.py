from user import User


class Billing:
    @staticmethod
    def bill_user(user, amount):
        # Implementation for billing a user
        if user.account_balance >= amount:
            user.account_balance -= amount
            print(f"{user.user_id} billed ${amount:.2f}. Remaining balance: ${user.account_balance:.2f}")
        else:
            print(f"{user.user_id} does not have enough funds to cover the billing. Warning issued.")
            user.apply_warning()

    @staticmethod
    def fine_user(user, amount):
        # Implementation for fining a user
        if user.account_balance >= amount:
            user.account_balance -= amount
            print(f"{user.user_id} fined ${amount:.2f}. Remaining balance: ${user.account_balance:.2f}")
        else:
            print(f"{user.user_id} does not have enough funds to cover the fine. Warning issued.")
            user.apply_warning()


# Creating a Billing instance
billing_system = Billing()

# Creating a user for testing
user1 = User("user1", "password1", account_balance=50)

# Billing the user
billing_system.bill_user(user1, amount=30)

# Fining the user
billing_system.fine_user(user1, amount=15)
