
import tkinter as tk

root = tk.Tk()
root.title("Password Strength Checker")
root.geometry("500x300")

label = tk.Label(root, text="Enter Password:", font=("Arial", 12))
label.pack(pady=10)

password_entry = tk.Entry(root, show="*", width=30)
password_entry.pack()

def check_strength():
    password = password_entry.get()

    has_upper = any(c.isupper() for c in password)
    has_lower = any(c.islower() for c in password)
    has_digit = any(c.isdigit() for c in password)
    has_special = any(c in "@#$%&!" for c in password)
    is_long = len(password) >= 8

    score = sum([has_upper, has_lower, has_digit, has_special, is_long])

    if score <= 2:
        strength = "Weak"
        color = "red"
    elif score <= 4:
        strength = "Medium"
        color = "orange"
    else:
        strength = "Strong"
        color = "green"

    result_label.config(text=f"Strength: {strength}", fg=color)

    suggestions = ""
    if not is_long:
        suggestions += "• Use at least 8 characters\n"
    if not has_upper:
        suggestions += "• Add uppercase letters\n"
    if not has_lower:
        suggestions += "• Add lowercase letters\n"
    if not has_digit:
        suggestions += "• Add numbers\n"
    if not has_special:
        suggestions += "• Add special characters (@#$%&!)\n"

    suggestion_label.config(text=suggestions)


check_button = tk.Button(root, text="Check Strength", command=check_strength)
check_button.pack(pady=10)

result_label = tk.Label(root, text="", font=("Arial", 12, "bold"))
result_label.pack()

suggestion_label = tk.Label(root, text="", font=("Arial", 10), justify="left")
suggestion_label.pack()

root.mainloop()

