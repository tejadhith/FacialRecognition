import customtkinter 
import PIL.Image, PIL.ImageTk
import cv2

customtkinter.set_appearance_mode("Dark")  # Modes: "System" (standard), "Dark", "Light"
customtkinter.set_default_color_theme("dark-blue")  # Themes: "blue" (standard), "green", "dark-blue"

root = customtkinter.CTk()
root.title("")
root.geometry("500x200")


def register() :
    reg = customtkinter.CTkToplevel(root)
    reg.title("")
    reg.geometry("500x300")
    label = customtkinter.CTkLabel(reg, text = "Roll Number :", font = ("Courier", 16))
    label.pack()
    entry = customtkinter.CTkEntry(reg, font = ("Courier", 14))
    entry.pack()
    frame = customtkinter.CTkButton(reg, text="Submit", font = ("Courier",16), command = show_webcam)
    frame.pack(pady = 20)
    # _, frame = vid.read()
    # img = PIL.Image.fromarray(frame)
    # imgtk = PIL.ImageTk.PhotoImage(image = img)
    # reg.imgtk = imgtk
    # reg.configure(image=imgtk)
    # reg.after(10, show_frame)
    submit = customtkinter.CTkButton(reg, text="Submit", font = ("Courier",16))
    submit.pack(pady = 20)

def mark() :
    mar = customtkinter.CTkToplevel(root)
    mar.title("")
    mar.geometry("500x300")
    label = customtkinter.CTkLabel(mar, text = "Roll Number :", font = ("Courier", 16))
    label.pack()
    entry = customtkinter.CTkEntry(mar, font = ("Courier", 14))
    entry.pack()
    # _, frame = vid.read()
    # img = PIL.Image.fromarray(frame)
    # imgtk = PIL.ImageTk.PhotoImage(image = img)
    # reg.imgtk = imgtk
    # reg.configure(image=imgtk)
    # reg.after(10, show_frame)
    submit = customtkinter.CTkButton(mar, text="Submit", font = ("Courier",16))
    submit.pack(pady = 20)

# vid = cv2.VideoCapture(0)

label = customtkinter.CTkLabel(root, text="Holla", font=("Courier", 20))
label.pack(pady=20)

register_button = customtkinter.CTkButton(root, text="Register", font=("Courier", 16), command = register)
register_button.pack(pady=10)

mark_attendance_button = customtkinter.CTkButton(root, text="Mark Attendance", font=("Courier", 16), command = mark)
mark_attendance_button.pack(pady=10)

root.mainloop()