##############################################################################
#   a113_TR_simple_window1.py
#   Example soulution: Change its size to 200 by 100 pixels.
##############################################################################
import tkinter as tk

# main window
root = tk.Tk()
root.wm_geometry("500x500")
root.title("Authentication")

# create empty frame
frame_login = tk.Frame(root)
frame_login.grid()


def test_my_button():
    print("clicked")
    frame_auth.tkraise()
    password = ent_password.get()
    lbl_display_pass.config(text = password)


lbl_username = tk.Label(frame_login, text='Username:', font = "Courier")
lbl_username.pack(pady=5, padx=5)

ent_username = tk.Entry(frame_login, bd=3)
ent_username.pack(pady=5)

lbl_password = tk.Label(frame_login, text='Password:', font= "Courier")
lbl_password.pack(pady=5, padx=5)

ent_password= tk.Entry(frame_login, bd=3, show = "*")
ent_password.pack(pady=5)

btn_login = tk.Button(frame_login, text ='Login', font="Courier" ,  command = test_my_button )
btn_login.pack()

lbl_password = tk.Label(frame_login)
lbl_password.config(text='Password:', font='Arial')

frame_auth = tk.Frame(root)
frame_auth.grid(row=0, column=0, sticky="news")

lbl_display_pass = tk.Label(frame_auth, text = "test")
lbl_display_pass.pack()

frame_login.tkraise()

root.mainloop()