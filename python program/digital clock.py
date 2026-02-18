import tkinter as tk
import time
import itertools

# Colors to cycle through
colors = itertools.cycle(["#00FFFF", "#FF69B4", "#7CFC00", "#FFA500", "#1E90FF", "#FFD700", "#FF4500"])

def update_clock():
    now = time.strftime('%H:%M:%S')
    date = time.strftime('%B %d, %Y')
    day = time.strftime('%A')

    time_label.config(text=now)
    date_label.config(text=date)
    day_label.config(text=day)

    # Toggle blinking and change color
    current_color = next(colors)
    time_label.config(fg=current_color)
    root.after(500, update_clock)  # Blink every 0.5 seconds

# Main window
root = tk.Tk()
root.title("Blinking Rainbow Clock")
root.geometry("700x350")
root.configure(bg="#111111")

# Time label
time_label = tk.Label(root, font=('Courier New', 70, 'bold'), bg="#111111")
time_label.pack(pady=(40, 10))

# Date label
date_label = tk.Label(root, font=('Verdana', 26), fg="#FFB6C1", bg="#111111")
date_label.pack()

# Day label
day_label = tk.Label(root, font=('Verdana', 22), fg="#ADFF2F", bg="#111111")
day_label.pack(pady=(10, 20))

update_clock()
root.mainloop()
