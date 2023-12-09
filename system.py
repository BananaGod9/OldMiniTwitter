from user import User


class MessagingSystem:
    def __init__(self):
        self.users = []
        self.messages = []

    def process_user_application(self, user_id, password):
        user = User(user_id, password)
        self.super_user.process_user_application(user, accepted=True)
        user.apply_deposit(100)  # Example deposit amount, adjust as needed

        # Update top messages, trendy users, and suggest accounts
        self.update_top_messages()
        self.update_trendy_users()
        self.suggest_accounts(user)
    def process_user_application(self, user, accepted=True, justification=""):
        # Implementation for processing user applications
        if accepted:
            temp_password = self.generate_temp_password()
            user.change_password(temp_password)
            user.deposit_money(100)  # Example deposit amount, adjust as needed
            print(f"User {user.user_id}'s application accepted. Temporary password sent.")

        else:
            print(f"User {user.user_id}'s application denied. Justification: {justification}")

    def suggest_accounts_to_follow(self, user):
        # Implementation for suggesting accounts to follow based on user history
        suggested_accounts = [u.user_id for u in self.users if u.user_id != user.user_id]
        print(f"Suggested accounts for {user.user_id} to follow: {suggested_accounts}")

    def handle_user_dispute(self, user, dispute_winner):
        # Implementation for handling user disputes
        if dispute_winner == user:
            user.clear_warnings()
            print(f"Dispute won! Warnings cleared for {user.user_id}.")
        else:
            if user.warnings > 0:
                user.apply_warning()
                print(f"{user.user_id} warned due to a dispute.")
            else:
                print(f"{user.user_id} has no warnings to apply.")

    def feature_top_messages_and_users(self):
        # Implementation for featuring top messages and users on the top page
        top_messages = sorted(self.messages, key=lambda m: m.likes, reverse=True)[:3]
        top_users = sorted(self.users, key=lambda u: u.likes, reverse=True)[:3]

        print("Top Messages:")
        for message in top_messages:
            print(f"{message.author}: {message.content} - Likes: {message.likes}")

        print("\nTop Users:")
        for user in top_users:
            print(f"{user.user_id} - Likes: {user.likes}")

    def generate_temp_password(self):
        # Generate a temporary password for new users
        return "temp_password"


# Example Usage:

# Creating a MessagingSystem
messaging_system = MessagingSystem()

# Creating users for testing
user1 = User("user1", "password1")
user2 = User("user2", "password2")
user3 = User("user3", "password3")

# Processing user applications
messaging_system.process_user_application(user1)
messaging_system.process_user_application(user2, accepted=False, justification="Incomplete profile")

# Suggesting accounts to follow
messaging_system.suggest_accounts_to_follow(user3)

# Handling user dispute
messaging_system.handle_user_dispute(user1, dispute_winner=user1)
messaging_system.handle_user_dispute(user2, dispute_winner=user1)

# Featuring top messages and users
messaging_system.feature_top_messages_and_users()
