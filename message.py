from datetime import datetime


from datetime import datetime
from tkinter import messagebox

from user import SuperUser


class Message:
    def __init__(self, author, content, keywords=None):
        self.author = author
        self.content = content
        self.keywords = keywords if keywords else []
        self.reads = 0
        self.likes = 0
        self.dislikes = 0
        self.complaints = 0
        self.timestamp = datetime.now()

    def display_message_info(self):
        print(f"Author: {self.author}")
        print(f"Time and Date: {self.timestamp}")
        print(f"Keywords: {', '.join(self.keywords)}")
        print(f"Reads: {self.reads}")
        print(f"Likes: {self.likes}")
        print(f"Dislikes: {self.dislikes}")
        print(f"Complaints: {self.complaints}")
        print(f"Content: {self.content}")

    def promote_to_trendy_post(self):
        # Logic to promote a message to a trendy post
        pass


class MessagingSystem:
    def __init__(self):
        self.users = []
        self.messages = []
        self.super_user = SuperUser("admin", "adminpass")

    def post_message(self, user, content):
        # Check if the message is free or needs billing
        if self.calculate_message_cost(content) > 0:
            # Billing logic
            if user.account_balance < self.calculate_message_cost(content):
                messagebox.showwarning("Insufficient Funds", "You do not have enough funds to post this message.")
                self.redirect_to_payment_page(user)
                return

            # Deduct the cost from the user's account
            user.account_balance -= self.calculate_message_cost(content)

        # Proceed with posting the message
        new_message = Message(author=user.user_id, content=content)
        self.messages.append(new_message)
        messagebox.showinfo("Message Posted", "Your message has been posted successfully.")

        # Update top messages and trendy users after posting a new message
        self.update_top_messages()
        self.update_trendy_users()

    def calculate_message_cost(self, content):
        # Calculate the cost of the message based on its length
        words = len(content.split())
        cost = max(words - 20, 0) * 0.1
        return cost

    def redirect_to_payment_page(self, user):
        # Logic to redirect the user to the payment page
        # You can implement this part based on your GUI design
        messagebox.showinfo("Redirecting to Payment Page", "You will be redirected to the payment page.")
        # Add code to open the payment page or handle the redirection

    def search_messages(self, author=None, keyword=None, with_images=False, with_videos=False, min_likes=None,
                        min_dislikes=None):
        # Logic to search messages based on the provided criteria
        result_messages = []
        for message in self.messages:
            # Implement filtering logic based on the search criteria
            pass
        return result_messages

    def click_on_ad(self, ad_message, cu_user):
        # Logic to handle clicking on an ad by a CU user
        pass

    def apply_to_job(self, job_message, cu_user):
        # Logic to handle applying to a job by a CU user
        pass

    def fine_user_for_ad_or_job(self, user):
        # Logic to fine a TU/OU posting ads or job opportunities
        pass

    def resolve_warnings_for_cu_ou(self, cu_ou_user):
        # Logic to handle warnings and fines for CU/OU users
        pass

    def demote_tu_to_ou(self, tu_user):
        # Logic to demote a TU user to OU
        pass

    def create_special_feature(self):
        # Logic to create a special feature (you can add your own creative feature)
        pass

    def update_top_messages(self):
        # Get the top 3 most liked messages
        top_messages = sorted(self.messages, key=lambda m: m.likes, reverse=True)[:3]

        # Update the top messages label
        top_messages_info = "\n".join([f"{message.author}: {message.likes} Likes" for message in top_messages])
        self.top_messages_label.config(text=f"Top 3 Most Liked Messages:\n{top_messages_info}")

    def update_trendy_users(self):
        # Get the top 3 users with the most likes
        top_users = sorted(self.users, key=lambda u: u.likes, reverse=True)[:3]

        # Update the trendy users label
        trendy_users_info = "\n".join([f"{user.user_id}: {user.likes} Likes" for user in top_users])
        self.trendy_users_label.config(text=f"Top 3 Trendy Users:\n{trendy_users_info}")

