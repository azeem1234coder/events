import tkinter as tk

def convert_to_cm():
    try:
        inches = float(entry.get())
        cm = inches * 2.54
        result_label.config(text=f"{inches} inches = {cm:.2f} cm")
    except ValueError:
        result_label.config(text="Please enter a valid number.")

# Create the main window
root = tk.Tk()
root.title("Inches to Centimeters Converter")

# Input field
entry_label = tk.Label(root, text="Enter length in inches:")
entry_label.pack(pady=5)

entry = tk.Entry(root)
entry.pack(pady=5)

# Convert button
convert_button = tk.Button(root, text="Convert", command=convert_to_cm)
convert_button.pack(pady=5)

# Result display
result_label = tk.Label(root, text="")
result_label.pack(pady=10)

# Run the application
root.mainloop()
