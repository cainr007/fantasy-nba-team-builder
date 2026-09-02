from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from BLL import LogIn_BLL
from BLL import Fantasy_Team_BLL
from BLL import Players_BLL
from PIL import ImageTk, Image

starter_window = Tk()

starter_window.title("Starter Window")
screen_width = starter_window.winfo_screenwidth()
screen_height = starter_window.winfo_screenheight()
starter_window.geometry(f"{screen_width}x{screen_height}")
starter_window.config(background="#949494")

def logIn():
    global username, password, host, port
    username = user_username.get()
    password = user_password.get()
    host = user_host.get()
    port = user_port.get()
    "Username: ",username
    "Password: ",password
    if username == "" or password == "" or host == "" or port == "":
        messagebox.showerror("Error","Please enter username, password, host, and port.")
        return
    try:
        port = int(port)
    except ValueError:
        messagebox.showerror("Error", "Port must be a number.")
        return
    logging_in = LogIn_BLL(username, password, host, port)
    if logging_in.logIn():
        messagebox.showinfo("Success","Login successful!")
        start_main()
    else:
        messagebox.showerror("Error","Invalid username, password, host, or port.")

def create_fantasy_team():
    create_fantasy_team_window = Toplevel(starter_window)
    create_fantasy_team_window.title("Create Fantasy Team")
    screen_width = create_fantasy_team_window.winfo_screenwidth()
    screen_height = create_fantasy_team_window.winfo_screenheight()
    create_fantasy_team_window.geometry(f"{screen_width}x{screen_height}")
    create_fantasy_team_window.config(background="#949494")

    back_button = Button(create_fantasy_team_window, text="Back",font=("Monospace", 25), bg= "#949494", command=create_fantasy_team_window.destroy)
    back_button.pack(anchor="ne", padx=20, pady=20)   



    create_fantasy_team_Label = Label(create_fantasy_team_window, text="Create Fantasy Team", font=("Monospace", 70), bd=5, relief="groove", bg="#000000", width=200, height=1)
    create_fantasy_team_Label.pack(pady=20)

    fantasy_team_label = Label(create_fantasy_team_window, text="Enter Fantasy Team Name:", font=("Monospace", 40), bg="#949494")
    fantasy_team_label.pack(pady=20)

    fantasy_team_entry = Entry(create_fantasy_team_window, font=("Monospace", 40))
    fantasy_team_entry.pack(pady=20)

    def create_team():
        global fantasyID
        fantasy_team_name = fantasy_team_entry.get()
        fantasy_team_bll = Fantasy_Team_BLL(username, password, host, port)
        fantasyID = fantasy_team_bll.create_fantasy_team(fantasy_team_name)
        messagebox.showinfo("Result", f"Fantasy Team Created!\nFantasyID: {fantasyID}")
        create_fantasy_team_window.destroy()

    create_team_button = Button(create_fantasy_team_window, text="Create Team", font=("Monospace", 40), bg="#630635", command=create_team)
    create_team_button.pack(pady=20)
    

def add_to_fantasy_team(playerID):
    global fantasyID
    global update_playerID
    if "fantasyID" not in globals():
        messagebox.showerror("Error", "Please make sure you create a fantasy team first.")
        return
    fantasy_team_bll = Fantasy_Team_BLL(username, password, host, port)
    if "update_playerID" in globals():
        confirm = messagebox.askyesno("Update Player", "Are you sure you'd like to make a replacement?")
        if not confirm:
            return
        result = fantasy_team_bll.update_fantasy_team(fantasyID, update_playerID, playerID)
        if result is not None:
            messagebox.showinfo("Result", result)
        else:
            messagebox.showinfo("Success!", "This player has been added to your team!")
        del update_playerID
        return
    result = fantasy_team_bll.add_to_fantasy_team(fantasyID, playerID)
    if result is not None:
        messagebox.showinfo("Result", result)
    else:
        messagebox.showinfo("Success!", "This player has been added to your team!")

def view_players():
    players_bll = Players_BLL(username, password, host, port)
    players = players_bll.get_player_list()

    view_players_window = Toplevel(starter_window)
    view_players_window.title("View Players")
    screen_width = view_players_window.winfo_screenwidth()
    screen_height = view_players_window.winfo_screenheight()
    view_players_window.geometry(f"{screen_width}x{screen_height}")
    view_players_window.config(background="#949494")

    view_players_window_Label = Label(view_players_window, text="View Players", font=("Monospace", 70), bd=5, relief="groove", bg="#000000", width=200, height=1)
    view_players_window_Label.pack(pady=20)

    back_button = Button(view_players_window, text="Back",font=("Monospace", 25), bg= "#949494", command=view_players_window.destroy)
    back_button.pack(anchor="ne", padx=20, pady=20)      

    player_canvas = Canvas(view_players_window, bg="#949494")
    player_canvas.pack(side="left", fill="both", expand=True)
    player_scrollbar = Scrollbar(view_players_window, orient="vertical", command=player_canvas.yview)
    player_scrollbar.pack(side="right", fill="y")
    player_canvas.configure(yscrollcommand=player_scrollbar.set)

    player_scrollable_frame = Frame(player_canvas, bg="#949494")
    player_canvas.create_window((0, 0), window=player_scrollable_frame, anchor="nw", width=screen_width)

    for index, p in enumerate(players):
        player_image = Image.open(f"Images/{p[0]}.png")
        player_image = player_image.resize((300, 200))
        player_image = ImageTk.PhotoImage(player_image)

        player_card = Frame(player_scrollable_frame, bg="#630635", bd=5, relief='groove')
        
        row = index // 4
        column = index % 4
        player_card.grid(row=row, column=column, padx=20, pady=20)

        player_image_label = Label(player_card, image=player_image, bg="#949494")
        player_image_label.image = player_image
        player_image_label.pack(pady=20)

        player_name_label = Label(player_card, text=p[1], font=("Monospace", 20, "bold"), bg="#630635")
        player_name_label.pack(pady=10)

        player_info_label = Label(player_card, text=f"Team: {p[4]} | Position: {p[2]}\n", font=("Monospace", 16), bg="#630635")
        player_info_label.pack(pady=10)

        player_stats_label = Label(player_card, text=f"Points: {p[5]}\n\nRebounds: {p[6]}\n\nAssists: {p[7]}\n", font=("Monospace", 16), bg="#630635")
        player_stats_label.pack(pady=10)

        add_player_button = Button(player_card, text="Add Player", font=("Monospace", 16), bg="#949494", command=lambda playerID=p[0]: add_to_fantasy_team(playerID))
        add_player_button.pack(pady=10)
    
    player_scrollable_frame.update_idletasks()
    player_canvas.config(scrollregion=player_canvas.bbox("all"))

def remove_from_fantasy_team(playerID, fantasy_team_window):
    global fantasyID
    if "fantasyID" not in globals ():
        messagebox.showerror("Error", "Please create a fantasy team first.")
        return
    confirm = messagebox.askyesno("Remove Player", "Are you sure you'd like to remove this player?")
    if not confirm:
        return
    fantasy_team_bll = Fantasy_Team_BLL(username, password, host, port)
    result = fantasy_team_bll.remove_from_fantasy_team(fantasyID, playerID)
    if result is not None:
        messagebox.showinfo("Result", result)
    else:
        messagebox.showinfo("Success.", "You have removed this player.")
        fantasy_team_window.destroy()
        my_fantasy_team()

def update_from_fantasy_team(playerID, fantasy_team_window):
    global update_playerID
    update_playerID = playerID
    fantasy_team_window.destroy()
    view_players()

def my_fantasy_team():
    global fantasyID
    if "fantasyID" not in globals():
        messagebox.showerror("Error", "Please make sure you create a fantasy team first.")
        return
    fantasy_team_bll = Fantasy_Team_BLL(username, password, host, port)
    players = fantasy_team_bll.get_fantasy_team_players(fantasyID)
    if not players:
        messagebox.showinfo("Fantasy Team", "Your fantasy team is empty.")
        return
        
    my_fantasy_team_window = Toplevel(starter_window)
    my_fantasy_team_window.title("My Fantasy Team")
    screen_width = my_fantasy_team_window.winfo_screenwidth()
    screen_height = my_fantasy_team_window.winfo_screenheight()
    my_fantasy_team_window.geometry(f"{screen_width}x{screen_height}")
    my_fantasy_team_window.config(background="#949494")

    back_button = Button(my_fantasy_team_window, text="Back",font=("Monospace", 25), bg= "#949494", command=my_fantasy_team_window.destroy)
    back_button.pack(anchor="ne", padx=20, pady=20)    

    my_fantasy_team_Label = Label(my_fantasy_team_window, text="My Fantasy Team", font=("Monospace", 70), bd=5, relief="groove", bg="#000000", width=200, height=1)
    my_fantasy_team_Label.pack(pady=20)

    player_canvas = Canvas(my_fantasy_team_window, bg="#949494")
    player_canvas.pack(side="left", fill="both", expand=True)
    player_scrollbar = Scrollbar(my_fantasy_team_window, orient="vertical", command=player_canvas.yview)
    player_scrollbar.pack(side="right", fill="y")
    player_canvas.configure(yscrollcommand=player_scrollbar.set)

    player_scrollable_frame = Frame(player_canvas, bg="#949494")
    player_canvas.create_window((0, 0), window=player_scrollable_frame, anchor="nw", width=screen_width)


    for index, p in enumerate(players):
        player_card = Frame(player_scrollable_frame, bg="#630635", bd=5, relief='groove')
        row = index // 3
        column = index % 3
        player_card.grid(row=row, column=column, padx=20, pady=20)

        player_image = Image.open(f"Images/{p[0]}.png")
        player_image = player_image.resize((300, 200))
        player_image = ImageTk.PhotoImage(player_image)

        player_image_label = Label(player_card, image=player_image, bg="#949494")
        player_image_label.image = player_image
        player_image_label.pack(pady=20)     

        player_name_label = Label(player_card, text=p[1], font=("Monospace", 20, "bold"), bg="#630635")
        player_name_label.pack(pady=10)

        player_info_label = Label(player_card, text=f"Team: {p[3]} | Position: {p[2]}\n", font=("Monospace", 16), bg="#630635")
        player_info_label.pack(pady=10)

        player_stats_label = Label(player_card, text=f"Points: {p[4]}\n\nRebounds: {p[5]}\n\nAssists: {p[6]}\n", font=("Monospace", 16), bg="#630635")
        player_stats_label.pack(pady=10)

        remove_player_button = Button(player_card, text="Remove Player", font=("Monospace", 16), bg= "#949494", command=lambda playerID=p[0] : remove_from_fantasy_team(playerID, my_fantasy_team_window))
        remove_player_button.pack(pady=10)

        update_player_button = Button(player_card, text="Update Player", font=("Monospace", 16), bg= "#949494", command=lambda playerID=p[0] : update_from_fantasy_team(playerID, my_fantasy_team_window))
        update_player_button.pack(pady=10)

    player_scrollable_frame.update_idletasks()
    player_canvas.config(scrollregion=player_canvas.bbox("all"))

    summary = fantasy_team_bll.get_fantasy_team_summary(fantasyID)
    if summary:
        avg_ppg = summary[0][0]
        avg_rpg = summary[0][1]
        avg_apg = summary[0][2]

        summary_label = Label(my_fantasy_team_window, text=f"Team Averages\n\n"f"Points: {avg_ppg:.2f}\n"f"Rebounds: {avg_rpg:.2f}\n"f"Assists: {avg_apg:.2f}\n",
                              font=("Monospace", 30), bd=5, relief="groove", bg="#630635")
        summary_label.pack(padx= 60, pady=30)

Log_In_Label = Label(starter_window, text="WELCOME", font=("Monospace", 70), bd=5, relief="groove", bg="#000000", width=200, height=1)
Log_In_Label.pack(pady=30)

Username_Label = Label(starter_window, text="USERNAME", font=("Monospace", 40), bg="#949494")
Username_Label.pack()

user_username = Entry(
    starter_window,
    font=("Monospace",40)
)
user_username.pack()

Password_Label = Label(starter_window, text="PASSWORD", font=("Monospace", 40), bg="#949494")
Password_Label.pack()

user_password = Entry(
    starter_window,
    font=("Monospace",40),
    show="*"
)
user_password.pack()

Host_Label = Label(starter_window, text="HOST", font=("Monospace", 40), bg="#949494")
Host_Label.pack()

user_host = Entry(
    starter_window,
    font=("Monospace",40)
)
user_host.insert(0, "localhost")
user_host.pack()

Port_Label = Label(starter_window, text="PORT", font=("Monospace", 40), bg="#949494")
Port_Label.pack()

user_port = Entry(
    starter_window,
    font=("Monospace",40)
)
user_port.insert(0, "3306")
user_port.pack()

logInButton_Image = Image.open("Images/Log In Button.png").resize((100, 50))
logInButton = ImageTk.PhotoImage(logInButton_Image)

Log_In_Button = Button(
    starter_window, image=logInButton,
    command=logIn,
    bg="#949494",pady=25)
Log_In_Button.pack(pady=100)

def start_main():
    second_window = Toplevel(starter_window)
    second_window.title("Main Window")
    screen_width = second_window.winfo_screenwidth()
    screen_height = second_window.winfo_screenheight()
    second_window.geometry(f"{screen_width}x{screen_height}")
    second_window.config(background="#949494")

    nbaLogo = Image.open("Images/NBA logo.png").resize((300, 200))
    nbaLogo = ImageTk.PhotoImage(nbaLogo)
    nbaLogoLabel = Label(second_window, image=nbaLogo, bg="#000000", bd=5, relief="groove", width=3000, height=200)
    nbaLogoLabel.image = nbaLogo
    nbaLogoLabel.pack(pady=20)

    nba_Label = Label(second_window, text="NBA FANTASY LEAGUE", font=("Monospace", 50), bd=5, relief="groove", bg="#000000", width=200, height=1)
    nba_Label.pack(pady=50)

    create_fantasy_team_button = Button(second_window, text="Create Fantasy Team", font=("Monospace", 40), bg="#949494", command=create_fantasy_team)
    create_fantasy_team_button.pack(pady=30)

    view_players_button = Button(second_window, text="View Players", font=("Monospace", 40), bg="#949494", command=view_players)
    view_players_button.pack(pady=30)

    my_fantasy_team_button = Button(second_window, text="My Fantasy Team", font=("Monospace", 40), bg="#949494", command=my_fantasy_team)
    my_fantasy_team_button.pack(pady=30)

starter_window.mainloop()