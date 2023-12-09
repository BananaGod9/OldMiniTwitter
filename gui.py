import tkinter as tk
from tkinter import messagebox

import tkinter as tk
from tkinter import messagebox
from datetime import datetime

class Message:
    def __init__(self, author, content, keywords=None):
        self.author = author
        self.content = content
        self.keywords = keywords if keywords else []
        self.reads = 0
        self.likes = 0
        self.dislikes = 0
        self.timestamp = datetime.now()

    def display_message_info(self):
        print(f"Author: {self.author}")
        print(f"Time and Date: {self.timestamp}")
        print(f"Keywords: {', '.join(self.keywords)}")
        print(f"Reads: {self.reads}")
        print(f"Likes: {self.likes}")
        print(f"Dislikes: {self.dislikes}")
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

class SuperUser(User):
    def __init__(self, user_id, password):
        super().__init__(user_id, password)

    def process_user_application(self, user, accepted=True, justification=""):
        if accepted:
            temp_password = self.generate_temp_password()
            user.change_password(temp_password)
            user.deposit_money(100)  # Example deposit amount, adjust as needed
            messagebox.showinfo("Application Accepted", f"User {user.user_id}'s application accepted.\nTemporary password sent.")
        else:
            messagebox.showwarning("Application Denied", f"User {user.user_id}'s application denied.\nJustification: {justification}")

    def generate_temp_password(self):
        # Generate a temporary password for new users
        return "temp_password"

class MessagingSystemGUI:
    def __init__(self, master):
        self.master = master
        self.master.title("Messaging System")

        # Create and pack widgets
        self.label = tk.Label(master, text="Welcome to Messaging System", font=("Helvetica", 16))
        self.label.pack(pady=10)

        self.login_button = tk.Button(master, text="Login", command=self.show_login_dialog)
        self.login_button.pack(pady=10)

        self.apply_button = tk.Button(master, text="Apply for User", command=self.show_application_dialog)
        self.apply_button.pack(pady=10)

        self.messages = []  # Store messages for the current user
        self.users = []  # Store users for the current user
        self.super_user = SuperUser("admin", "adminpass")

    def show_login_dialog(self):
        login_dialog = tk.Toplevel(self.master)
        login_dialog.title("Login")

        # Add login widgets here

        # Example usage of message and user features
        sample_message = Message(author="User1", content="Hello, this is a message.")
        self.messages.append(sample_message)

        sample_user = User(user_id="User1", password="pass1")
        self.users.append(sample_user)

        # Display message information
        tk.Button(login_dialog, text="Show Message Info", command=lambda: sample_message.display_message_info()).pack(pady=5)

        # Display user information
        tk.Button(login_dialog, text="Show User Info", command=lambda: self.show_user_profile(sample_user)).pack(pady=5)

    def show_application_dialog(self):
        application_dialog = tk.Toplevel(self.master)
        application_dialog.title("Apply for User")

        # Add application widgets here

        # Example usage of application features
        user_id_entry = tk.Entry(application_dialog, text="User ID")
        user_id_entry.pack(pady=5)

        password_entry = tk.Entry(application_dialog, text="Password", show="*")
        password_entry.pack(pady=5)

        apply_button = tk.Button(application_dialog, text="Apply", command=lambda: self.process_user_application(user_id_entry.get(), password_entry.get()))
        apply_button.pack(pady=10)

    def process_user_application(self, user_id, password):
        user = User(user_id, password)
        self.super_user.process_user_application(user, accepted=True)

    def show_user_profile(self, user):
        profile_dialog = tk.Toplevel(self.master)
        profile_dialog.title("User Profile")

        tk.Label(profile_dialog, text=f"User Profile - {user.user_id}").pack(pady=10)

        tk.Button(profile_dialog, text="Show Messages", command=lambda: self.show_user_messages(user)).pack(pady=5)

    def show_user_messages(self, user):
        messages_dialog = tk.Toplevel(self.master)
        messages_dialog.title("User Messages")

        tk.Label(messages_dialog, text=f"Messages for {user.user_id}").pack(pady=10)

        for message in self.messages:
            tk.Button(messages_dialog, text=f"Message by {message.author}", command=lambda m=message: m.display_message_info()).pack(pady=5)

    def run(self):
        self.master.mainloop()

if __name__ == "__main__":
    root = tk.Tk()
    gui = MessagingSystemGUI(root)
    gui.run()
