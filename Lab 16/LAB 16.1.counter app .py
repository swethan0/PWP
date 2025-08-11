import tkinter as tk

# Initialize main window
root = tk.Tk()
root.title("Counter App")
root.geometry("250x150")

# Initialize counter variable
counter = tk.IntVar(value=0)

# Function to increment the counter
def increment():
    counter.set(counter.get() + 1)

# Label to display the counter
label = tk.Label(root, textvariable=counter, font=("Helvetica", 32))
label.pack(pady=20)

# Button to increase counter
button = tk.Button(root, text="Click Me", command=increment, font=("Helvetica", 14))
button.pack()

# Start the Tkinter loop
root.mainloop()
