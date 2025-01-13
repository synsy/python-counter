import tkinter as tk

label_bg = "#252422"

root = tk.Tk()
root.title("Death Counter")
root.geometry("350x250")
root.configure(bg="#25000e")

def open_popup():
    # Create a new Toplevel window (popup)
    popup = tk.Toplevel(root)
    popup.title("Add Player")
    popup.geometry("200x100")

    # Label and Entry for player name
    label = tk.Label(popup, text="Enter Player Name:")
    label.pack(pady=5)

    entry = tk.Entry(popup)
    entry.pack(pady=5)
    entry.focus_set()  # Set focus to the entry field immediately

    # Function to remove a player
    def remove_player(frame):
        frame.destroy()

    # Function to add a death (increment/decrement the death counter)
    def update_death(deaths_label, amount):
        current_deaths = int(deaths_label["text"])  # Get current death count
        if amount < 0 < current_deaths:
            deaths_label.config(text=str(current_deaths + amount))  # Increment by 1 and update label
        else:
            if amount > 0:
                deaths_label.config(text=str(current_deaths + amount)) # Decrement by 1 and update label

    # Function to handle the input
    def add_player():
        player_name = entry.get()
        if player_name:
            # Create a frame to hold both the player and deaths labels, with a border around the frame
            player_frame = tk.Frame(root, highlightbackground="black", highlightthickness=1, background=label_bg)
            player_frame.pack(pady=5, padx=5, fill="x")

            # Configure the grid to allow stretching
            player_frame.grid_columnconfigure(1, weight=1)

            # Player label on the left
            player_label = tk.Label(player_frame, text=player_name, font=("Arial", 15), bg=label_bg, fg="white")
            player_label.grid(row=0, column=0, padx=5, sticky="w")

            # Deaths label in the middle
            deaths_label = tk.Label(player_frame, text="0", font=("Arial", 15), bg=label_bg, fg="white")
            deaths_label.grid(row=0, column=1, padx=20, sticky="e")

            # Add death button
            add_death_button = tk.Button(player_frame, text="+", command=lambda: update_death(deaths_label, 1), bg="green", fg="white", width=2, height=1, font=("Arial", 8, "bold"))
            add_death_button.grid(row=0, column=2, padx=3, sticky="e")

            # Subtract death button
            subtract_death_button = tk.Button(player_frame, text="-", command=lambda: update_death(deaths_label, -1), bg="pink", fg="white", width=2, height=1, font=("Arial", 8, "bold"))
            subtract_death_button.grid(row=0, column=3, padx=3, sticky="e")

            # Remove player button
            remove_player_button = tk.Button(player_frame, text="X", command=lambda: remove_player(player_frame), bg="red", fg="white", width=2, height=1, font=("Arial", 8, "bold"))
            remove_player_button.grid(row=0, column=4, padx=3, sticky="e")

        popup.destroy()  # Close the popup after getting input

    # Button to submit the player name
    submit_button = tk.Button(popup, text="Submit", command=add_player)
    submit_button.pack(pady=10)

    # Bind the Enter key to the add_player function
    popup.bind('<Return>', lambda event: add_player())


# Button on the main window to open the popup
button = tk.Button(root, text="Add Player", command=open_popup)
button.pack(pady=10)
button.focus_set()
button.bind('<Return>', lambda event: open_popup())

root.mainloop()
