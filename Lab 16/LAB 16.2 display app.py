import tkinter as tk

# Initialize main window
root = tk.Tk()
root.title("Text Input App")
root.geometry("300x200")

# Function to display the entered text
def show_text():
    entered_text = entry.get()
    label_result.config(text="You typed: " + entered_text)

# Entry widget for text input
entry = tk.Entry(root, width=30, font=("Arial", 14))
entry.pack(pady=10)

# Button to trigger display of text
button = tk.Button(root, text="Display Text", command=show_text, font=("Arial", 12))
button.pack(pady=5)

# Label to show the result
label_result = tk.Label(root, text="", font=("Arial", 14))
label_result.pack(pady=10)

# Start the GUI event loop
root.mainloop()
