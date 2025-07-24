import instaloader
import tkinter as tk
from tkinter import ttk, messagebox

# Insta Setup
ig = instaloader.Instaloader()

# GUI Setup
root = tk.Tk()
root.title("InstaSpy 🔍 — Profile Viewer")
root.geometry("480x520")
root.configure(bg="#0f0f0f")

# Style Setup
style = ttk.Style()
style.theme_use("clam")  # Better base styling
style.configure("TButton", font=("Segoe UI", 11), padding=6, background="#1DB954", foreground="black")
style.configure("TLabel", background="#0f0f0f", foreground="#f0f0f0", font=("Segoe UI", 11))
style.configure("TEntry", padding=5)

# Header
header = ttk.Label(root, text="💡 InstaSpy ", font=("Segoe UI Black", 22), anchor="center")
header.pack(pady=(20, 10))

# Username Entry
username_label = ttk.Label(root, text="Enter Instagram Username:")
username_label.pack()
username_entry = ttk.Entry(root, font=("Segoe UI", 14), width=30, justify="center")
username_entry.pack(pady=10)

# Output Frame
output_frame = tk.Frame(root, bg="#1c1c1c", bd=2, relief="sunken")
output_frame.pack(pady=20, padx=20, fill="both", expand=True)

output_text = tk.Text(output_frame, height=10, bg="#1c1c1c", fg="#00ff99", font=("Courier New", 10), bd=0)
output_text.pack(padx=10, pady=10, fill="both", expand=True)

# Fetch Info Function
def fetch_info():
    username = username_entry.get().strip()
    if not username:
        messagebox.showwarning("Hold Up", "You forgot the username 😐")
        return
    try:
        profile = instaloader.Profile.from_username(ig.context, username)
        output_text.delete("1.0", tk.END)
        output_text.insert(tk.END, f"📛 Username: {profile.username}\n")
        output_text.insert(tk.END, f"📸 Posts: {profile.mediacount}\n")
        output_text.insert(tk.END, f"👥 Followers: {profile.followers}\n")
        output_text.insert(tk.END, f"➡️ Following: {profile.followees}\n")
        output_text.insert(tk.END, f"📝 Bio:\n{profile.biography}")
    except instaloader.exceptions.ProfileNotExistsException:
        messagebox.showerror("Oops", "That profile doesn’t exist 😬")
    except Exception as e:
        messagebox.showerror("Error", f"Something went wrong:\n{str(e)}")

# Download Pic Function
def download_pic():
    username = username_entry.get().strip()
    if not username:
        messagebox.showwarning("Hold Up", "Type a username first 🫠")
        return
    try:
        ig.download_profile(username, profile_pic_only=True)
        messagebox.showinfo("Downloaded 🎉", f"Profile pic of @{username} saved.")
    except Exception as e:
        messagebox.showerror("Download Failed", f"Couldn't download:\n{str(e)}")

# Buttons
btn_frame = tk.Frame(root, bg="#0f0f0f")
btn_frame.pack()

fetch_btn = ttk.Button(btn_frame, text="Fetch Profile Info", command=fetch_info)
fetch_btn.grid(row=0, column=0, padx=10, pady=10)

download_btn = ttk.Button(btn_frame, text="Download DP", command=download_pic)
download_btn.grid(row=0, column=1, padx=10, pady=10)

# Footer
footer = ttk.Label(root, text="Made with ❤️ by Gaurish Metha", font=("Segoe UI", 9))
footer.pack(pady=10)

root.mainloop()
