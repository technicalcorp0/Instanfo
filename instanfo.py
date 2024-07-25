import tkinter as tk
from tkinter import messagebox
import instaloader

class InstagramOSINTApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Instagram OSINT Tool")
        self.root.geometry("400x400")
        self.root.config(bg="#f0f0f0")

        # Create and place widgets
        self.create_widgets()

    def create_widgets(self):
        # Title Label
        self.title_label = tk.Label(self.root, text="Instagram OSINT Tool", font=("Helvetica", 16, "bold"), bg="#f0f0f0", fg="#333")
        self.title_label.pack(pady=10)

        # Username Label and Entry
        self.username_label = tk.Label(self.root, text="Enter Instagram Username:", bg="#f0f0f0", fg="#333")
        self.username_label.pack(pady=5)

        self.username_entry = tk.Entry(self.root, width=40, font=("Helvetica", 12))
        self.username_entry.pack(pady=5)

        # Search Button
        self.search_button = tk.Button(self.root, text="Fetch Data", command=self.fetch_data, bg="#4CAF50", fg="white", font=("Helvetica", 12, "bold"))
        self.search_button.pack(pady=15)

        # Results Text Area
        self.results_text = tk.Text(self.root, height=10, width=50, font=("Helvetica", 12), wrap=tk.WORD, bg="#ffffff", fg="#333")
        self.results_text.pack(pady=10)
        self.results_text.config(state=tk.DISABLED)

    def fetch_data(self):
        username = self.username_entry.get()
        if not username:
            messagebox.showwarning("Input Error", "Please enter a username.")
            return

        L = instaloader.Instaloader()

        try:
            profile = instaloader.Profile.from_username(L.context, username)
            user_data = {
                'Username': profile.username,
                'User ID': profile.userid,
                'Full Name': profile.full_name,
                'Bio': profile.biography,
                'Profile Pic URL': profile.profile_pic_url,
                'Number of Posts': profile.mediacount,
                'Followers': profile.followers,
                'Following': profile.followees,
                'Is Private': profile.is_private,
                'Is Verified': profile.is_verified
            }

            # Display user data
            self.results_text.config(state=tk.NORMAL)
            self.results_text.delete(1.0, tk.END)
            for key, value in user_data.items():
                self.results_text.insert(tk.END, f'{key}: {value}\n')
            self.results_text.config(state=tk.DISABLED)

        except instaloader.exceptions.ProfileNotExistsException:
            messagebox.showerror("Error", f"Profile with username '{username}' does not exist.")
        except Exception as e:
            messagebox.showerror("Error", f"An error occurred: {e}")

if __name__ == "__main__":
    root = tk.Tk()
    app = InstagramOSINTApp(root)
    root.mainloop()
