import customtkinter 
import cv2
import main

customtkinter.set_appearance_mode("Dark")  # Modes: "System" (standard), "Dark", "Light"
customtkinter.set_default_color_theme("dark-blue")  # Themes: "blue" (standard), "green", "dark-blue"

root = customtkinter.CTk()
root.title("")
root.geometry("500x200")

def register() :
    def file() :
        file_path = customtkinter.filedialog.askopenfilename(filetypes = [("Image Files", "*.jpg *.jpeg *.png")])
        img.delete(0, customtkinter.END)
        img.insert(0, file_path)
    def sub() :
        cv2.imwrite("known_faces/" + entry.get() + ".jpg", cv2.imread(img.get()))
    reg = customtkinter.CTkToplevel(root)
    reg.title("")
    reg.geometry("500x300")
    label = customtkinter.CTkLabel(reg, text = "Roll Number :", font = ("Courier", 16))
    label.pack()
    entry = customtkinter.CTkEntry(reg, font = ("Courier", 14))
    entry.pack()
    img = customtkinter.CTkEntry(reg , font = ("Courier", 14))
    img.pack(pady = 20)
    img_button = customtkinter.CTkButton(reg, text = "Upload Image", font = ("Courier", 16), command = file)
    img_button.pack()
    submit = customtkinter.CTkButton(reg, text="Submit", font = ("Courier",16), command = sub)
    submit.pack(pady = 20)
    reg.mainloop()

def mark() :
    def file() :
        file_path = customtkinter.filedialog.askopenfilename(filetypes = [("Image Files", "*.jpg *.jpeg *.png")])
        img.delete(0, customtkinter.END)
        img.insert(0, file_path)
    def sub() :
        cv2.imwrite("unknown_faces/" + entry.get() + ".jpg", cv2.imread(img.get()))
        final = customtkinter.CTkToplevel(mar)
        final.title("")
        final.geometry("300x70")
        if main.compare("known_faces/" + entry.get() + ".jpg", "unknown_faces/" + entry.get() + ".jpg") == True :
            out = customtkinter.CTkLabel(final, text = entry.get() + " Logged In", font = ("Courier", 16))
            out.pack(pady = 15)
        else :
            out = customtkinter.CTkLabel(final, text = "Unknown User/Register First", font = ("Courier", 16))
            out.pack(pady = 15)

    mar = customtkinter.CTkToplevel(root)
    mar.title("")
    mar.geometry("500x300")
    label = customtkinter.CTkLabel(mar, text = "Roll Number :", font = ("Courier", 16))
    label.pack()
    entry = customtkinter.CTkEntry(mar, font = ("Courier", 14))
    entry.pack()
    img = customtkinter.CTkEntry(mar , font = ("Courier", 14))
    img.pack(pady = 20)
    img_button = customtkinter.CTkButton(mar, text = "Upload Image", font = ("Courier", 16), command = file)
    img_button.pack()
    submit = customtkinter.CTkButton(mar, text="Submit", font = ("Courier",16), command = sub)
    submit.pack(pady = 20)
    mar.mainloop()

label = customtkinter.CTkLabel(root, text="Holla", font=("Courier", 20))
label.pack(pady=20)

register_button = customtkinter.CTkButton(root, text="Register", font=("Courier", 16), command = register)
register_button.pack(pady=10)

mark_attendance_button = customtkinter.CTkButton(root, text="Mark Attendance", font=("Courier", 16), command = mark)
mark_attendance_button.pack(pady=10)

root.mainloop()