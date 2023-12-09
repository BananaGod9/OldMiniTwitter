from gui import Message

from datetime import datetime


class Message:
    def __init__(self, author, content, keywords=None):
        self.author = author
        self.content = content
        self.keywords = keywords if keywords else []
        self.reads = 0
        self.likes = 0
        self.dislikes = 0
        self.complaints = 0  # New attribute to track complaints
        self.timestamp = datetime.now()

    def display_message_info(self):
        print(f"Author: {self.author}")
        print(f"Time and Date: {self.timestamp}")
        print(f"Keywords: {', '.join(self.keywords)}")
        print(f"Reads: {self.reads}")
        print(f"Likes: {self.likes}")
        print(f"Dislikes: {self.dislikes}")
        print(f"Complaints: {self.complaints}")  # Display complaints along with other info
        print(f"Content: {self.content}")


class User:
    def __init__(self, user_id, password, account_balance=0, warnings=0, likes=0, dislikes=0):
        self.user_id = user_id
        self.password = password
        self.account_balance = account_balance
        self.warnings = warnings
        self.likes = likes
        self.dislikes = dislikes

    def change_password(self, new_password):
        self.password = new_password

    def deposit_money(self, amount):
        self.account_balance += amount

    def apply_warning(self):
        self.warnings += 1

    def clear_warnings(self):
        self.warnings = 0

    def like_message(self, message):
        message.likes += 1
        self.likes += 1

    def dislike_message(self, message):
        message.dislikes += 1
        self.dislikes += 1

    def initiate_dispute(self, other_user):
        # Logic to initiate a dispute with another user
        return Dispute(self, other_user)


class SuperUser(User):
    def __init__(self, user_id, password):
        super().__init__(user_id, password)

    def resolve_dispute(self, dispute, winner):
        # Logic to resolve a dispute and apply consequences
        if winner == dispute.initiator:
            dispute.initiator.clear_warnings()
            print(f"Dispute won! Warnings cleared for {dispute.initiator.user_id}.")
        else:
            if dispute.initiator in dispute.complainant.followers:  # Check if the complainant is a follower
                dispute.complainant.apply_warning()
                print(f"Warning applied to {dispute.complainant.user_id} for initiating a dispute.")
            else:
                dispute.complainant.like_message(dispute.message)  # Reward complained user with 3 likes
                print(f"{dispute.complainant.user_id} rewarded with 3 likes for receiving a dispute from a surfer.")


class Dispute:
    def __init__(self, initiator, complainant, message):
        self.initiator = initiator
        self.complainant = complainant
        self.message = message


class MessagingSystem:
    def __init__(self):
        self.users = []
        self.messages = []
        self.super_user = SuperUser("admin", "adminpass")

    def process_user_application(self, user, accepted=True, justification=""):
        if accepted:
            temp_password = self.super_user.generate_temp_password()
            user.change_password(temp_password)
            user.deposit_money(100)  # Example deposit amount, adjust as needed
            self.users.append(user)
            print(f"User {user.user_id}'s application accepted. Temporary password sent.")
        else:
            print(f"User {user.user_id}'s application denied. Justification: {justification}")

    def suggest_accounts_to_follow(self, user):
        suggested_accounts = [u.user_id for u in self.users if u.user_id != user.user_id]
        print(f"Suggested accounts for {user.user_id} to follow: {suggested_accounts}")

    def handle_user_dispute(self, user, dispute_winner):
        if dispute_winner == user:
            user.clear_warnings()
            print(f"Dispute won! Warnings cleared for {user.user_id}.")

    def generate_temp_password(self):
        # Generate a temporary password for new users
        return "temp_password"
