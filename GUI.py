import tkinter as tk
from tkinter import ttk, Listbox, ANCHOR, messagebox
import datetime
from SongCollection import SongCollection

song_collection = SongCollection()

root = tk.Tk()
root.title("Song Collection")
root.geometry("700x400")

tab_parent = ttk.Notebook(root)


tab1 = ttk.Frame(tab_parent)
tab2 = ttk.Frame(tab_parent)
tab3 = ttk.Frame(tab_parent)

background_image = tk.PhotoImage(file='./preview-204862-aYTxozfB5i-high_0000.png')
background_label = tk.Label(tab1, image=background_image)
background_label_1 = tk.Label(tab2, image=background_image)
background_label_2 = tk.Label(tab3, image=background_image)
background_label.place(relwidth=1, relheight=1)
background_label_1.place(relwidth=1, relheight=1)
background_label_2.place(relwidth=1, relheight=1)

tab_parent.add(tab1, text="Songs")
tab_parent.add(tab2, text="Add new song")
tab_parent.add(tab3, text="Search for songs by artist/band")
tab_parent.pack(expand=1, fill='both')


def delete():
    if tab1_listbox.get(ANCHOR) != "":
        msg_box = tk.messagebox.askquestion('Delete song', 'Are you sure you want to delete the song?',
                                            icon='warning')
        if msg_box == 'yes':
            song_string = tab1_listbox.get(ANCHOR)
            song = song_collection.get_song_from_string(song_string)
            song_collection.delete_song(song)
            tab1_listbox.delete(ANCHOR)


def add(title, artist, year, category):
    title = validate_string(title)
    artist = validate_string(artist)
    year = validate_int(year, 0, datetime.datetime.now().year)
    category = validate_string(category)
    if valid_string_check(title) and valid_string_check(artist) \
            and valid_string_check(category) and valid_int_check(year, 0, datetime.datetime.now().year):
        song_collection.add_song(title, artist, year, category)
        update_tab1_song_list()
    clear_tab2_entry()


def search_by_artist(artist):
    tab3_listbox.delete(0, tk.END)
    artist = validate_string(artist)
    songs_by_artist = song_collection.get_song_by_artist(artist)
    if len(songs_by_artist) == 0:
        tab3_listbox.insert(1, "No songs by artist/band present")
    for songs in songs_by_artist:
        tab3_listbox.insert("end", songs)


def validate_string(string):
    if string == "" or len(string.strip()) <= 0 \
            or len(string.strip()) >= 200:
        messagebox.showerror("Invalid input", "Input not valid, please enter valid input.")
    string = string.strip()
    return string


def valid_string_check(string):
    if string == "" or len(string.strip()) <= 0 \
            or len(string.strip()) >= 200:
        return False
    return True


def validate_int(num, lower_limit, upper_limit):
    if not num.isdigit() or int(num) <= int(lower_limit) or int(num) > int(upper_limit):
        messagebox.showerror("Invalid input", "Input not valid, please enter valid input.")
    else:
        return num


def valid_int_check(num, lower_limit, upper_limit):
    clear_tab2_entry()
    if not num.isdigit() or int(num) <= int(lower_limit) or int(num) > int(upper_limit):
        return False
    return True


def update_tab1_song_list():
    tab1_listbox.delete(0, tk.END)
    for songs in song_collection.get_song_list():
        tab1_listbox.insert("end", songs)


def clear_tab2_entry():
    title_entry.delete(0, 'end')
    artist_entry.delete(0, 'end')
    year_entry.delete(0, 'end')
    category_entry.delete(0, 'end')


# tab 1 content
tab1_listbox_frame = tk.Frame(tab1)
tab1_listbox_scrollbar = tk.Scrollbar(tab1_listbox_frame, orient=tk.VERTICAL)
tab1_listbox = Listbox(tab1_listbox_frame, selectmode=tk.SINGLE, yscrollcommand=tab1_listbox_scrollbar.set)
tab1_listbox_scrollbar.config(command=tab1_listbox.yview)
tab1_listbox_scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
tab1_listbox_frame.pack()
tab1_listbox.config(width=0,  font=('Gotham Medium', 12), bg='white')
tab1_listbox.pack()
for songs in song_collection.get_song_list():
    tab1_listbox.insert("end", songs)  # no scroll bar
song = tab1_listbox.get(ANCHOR)
delete_button = tk.Button(tab1, text="Delete", command=delete, font=('Gotham Medium', 12)).pack()

# tab 2 content
title_label = tk.Label(tab2, text="Enter Title:", font=('Gotham Medium', 12)).grid(row=0, column=0, padx=15, pady=15, )
artist_label = tk.Label(tab2, text="Enter artist/band name:", font=('Gotham Medium', 12)).grid(row=1, column=0, padx=15, pady=15)
year_label = tk.Label(tab2, text="Enter year purchased:", font=('Gotham Medium', 12)).grid(row=2, column=0, padx=15, pady=15)
category_label = tk.Label(tab2, text="Enter category:", font=('Gotham Medium', 12)).grid(row=3, column=0, padx=15, pady=15)

title_entry = tk.Entry(tab2, font=('Gotham Medium', 12))
title_entry.grid(row=0, column=1, padx=15, pady=15)
artist_entry = tk.Entry(tab2, font=('Gotham Medium', 12))
artist_entry.grid(row=1, column=1, padx=15, pady=15)
year_entry = tk.Entry(tab2, font=('Gotham Medium', 12))
year_entry.grid(row=2, column=1, padx=15, pady=15)
category_entry = tk.Entry(tab2, font=('Gotham Medium', 12))
category_entry.grid(row=3, column=1, padx=15, pady=15)

add_button = tk.Button(tab2, text="Add song", font=('Gotham Medium', 12),
                       command=lambda: add(title_entry.get(), artist_entry.get(), year_entry.get(),
                                           category_entry.get())) \
    .grid(row=3, column=5, pady=15, padx=15)


# tab3 content
search_by_artist_label = tk.Label(tab3, text="Enter artist/band: ", font=('Gotham Medium', 12)).grid(row=0, column=0, padx=15, pady=15, )
search_by_artist_entry = tk.Entry(tab3, font=('Gotham Medium', 12))
search_by_artist_entry.grid(row=0, column=1, padx=15, pady=15)
search_by_artist_button = tk.Button(tab3, text="Search", font=('Gotham Medium', 12),
                                    command=lambda: search_by_artist(search_by_artist_entry.get())).grid(row=0, column=2, padx=15, pady=15)
tab3_listbox_frame = tk.Frame(tab3)
tab3_listbox_scrollbar = tk.Scrollbar(tab3_listbox_frame, orient=tk.VERTICAL)
tab3_listbox = Listbox(tab3_listbox_frame, selectmode=tk.SINGLE, yscrollcommand=tab3_listbox_scrollbar.set)
tab3_listbox_scrollbar.config(command=tab1_listbox.yview)
tab3_listbox_scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
tab3_listbox_frame.grid(row=3, padx=15, pady=15)
tab3_listbox.config(width=0,  font=('Gotham Medium', 12), bg='white')
tab3_listbox.pack()

root.mainloop()
