import customtkinter
from PIL import Image

customtkinter.set_appearance_mode("light")
customtkinter.set_default_color_theme("blue")

class SmartInventoryApp:
    def __init__(self,root):
        self.root=root
        
        self.root.title("Smart Inventry management System")
        self.root.after(10,lambda: self.root.state("zoomed"))
        
        self.Header_widget()
        self.Body_widget()
    
    def Header_widget(self):
        
        self.Header_frame=customtkinter.CTkFrame(
            self.root,
            bg_color="#000000",
            fg_color="#000000",
            height=60
        )
        self.Header_frame.pack(fill="x")
        
        self.Header_content1=customtkinter.CTkLabel(
            self.Header_frame,
            text="Smart Inventry management System",
            font=("Segoe UI",38,"bold"),
            text_color="#ffffff"
        )
        self.Header_content1.pack(pady=10)
        
        self.Exit_button=customtkinter.CTkButton(
            self.Header_frame,
            text="Exit",
            fg_color="Green",
            text_color="#ffffff",
            height=40,
            width=150,
            font=("Segoe UI",20,"bold"),
            command=self.root.destroy
        )
        self.Exit_button.place(relx=0.98, rely=0.5, anchor="e")
        
        self.Below_Header_content_frame=customtkinter.CTkFrame(
            self.root,
            bg_color="#446dbb",
            fg_color="#446dbb",
            height=60
        )
        self.Below_Header_content_frame.pack(fill="x")
        
        self.row_frame=customtkinter.CTkFrame(
            self.Below_Header_content_frame,
            fg_color="transparent"
        )
        self.row_frame.pack(pady=10)
        
        python_icon = customtkinter.CTkImage(
        light_image=Image.open("assets/icons/Python_Icon.png"),
        size=(60, 60)
        )
        
        self.icon_label=customtkinter.CTkLabel(
            self.row_frame,
            text="",
            image=python_icon,
            compound="left"
        )
        self.icon_label.pack(side="left",pady=10)
        
        self.Header_content2=customtkinter.CTkLabel(
            self.row_frame,
            text="Build with Python & CustumTkinter",
            font=("Segoe UI",35,"bold"),
            text_color="#ffffff"
        )
        self.Header_content2.pack(side="left",pady=10)
        
    def Body_widget(self):
        self.complete_Remaining_frame = customtkinter.CTkFrame(
            self.root,
            bg_color="#1e3a8a",
            fg_color="#1e3a8a"
        )
        self.complete_Remaining_frame.pack(fill="both", expand=True)
        
        
        self.UserLogin_frame = customtkinter.CTkFrame(
            self.complete_Remaining_frame,
            fg_color="#2c5ab3",
            width=450,
            height=550,
            corner_radius=20
        )
        self.UserLogin_frame.pack(padx=40, pady=40)
        self.UserLogin_frame.pack_propagate(False) 
        
        profile_icon = customtkinter.CTkImage(
            light_image=Image.open("assets/icons/profile_icon.png"),
            size=(100, 100)
        )
        
        self.icon_label = customtkinter.CTkLabel(
            self.UserLogin_frame, 
            text="",
            image=profile_icon
        )
        self.icon_label.pack(pady=(10, 10)) 
        
        self.Login_Text=customtkinter.CTkLabel(
            self.UserLogin_frame,
            text="Login",
            text_color="#ffffff",
            font=("Segoe UI",30,"bold")
        )
        self.Login_Text.pack()
        
        self.username_Frame=customtkinter.CTkFrame(
            self.UserLogin_frame,
            fg_color="transparent"
        )
        self.username_Frame.pack()
        
        user_icon=customtkinter.CTkImage(
            light_image=Image.open("assets/icons/user.png"),
            size=(40,40)
        )
        
        self.username_icon_label=customtkinter.CTkLabel(
            self.username_Frame,
            text="",
            image=user_icon
        )
        self.username_icon_label.pack(side="left")
        
        self.Username_Entry=customtkinter.CTkEntry(
            self.username_Frame,
            placeholder_text="Username",
            height=50,
            width=300,
            font=("Segoe UI",20,"bold")
        )
        self.Username_Entry.pack(pady=10,padx=10)
        
        self.Password_Frame=customtkinter.CTkFrame(
            self.UserLogin_frame,
            fg_color="transparent"
        )
        self.Password_Frame.pack()
        
        passward_icon=customtkinter.CTkImage(
            light_image=Image.open("assets/icons/password.png"),
            size=(40,40)
        )
        
        self.Password_Label=customtkinter.CTkLabel(
            self.Password_Frame,
            text="",
            image=passward_icon
        )
        self.Password_Label.pack(side="left")
        
        self.Password_Entry=customtkinter.CTkEntry(
            self.Password_Frame,
            placeholder_text="Password",
            height=50,
            width=300,
            font=("Segoe UI",20,"bold"),
            show="*"
        )
        
        self.Password_Entry.pack(padx=10,pady=(0,10))
        
        self.Password_Entry_error=customtkinter.CTkLabel(
            self.UserLogin_frame,
            text="",
            text_color="red",
            font=("Segoe UI",15,"bold")
        )
        self.Password_Entry_error.pack()
        
        self.Login_Button=customtkinter.CTkButton(
            self.UserLogin_frame,
            text="Login",
            fg_color="Green",
            height=40,
            width=150,
            font=("Segoe UI",20,"bold"),
            command=lambda:self.CheckUserlogin()
        )
        self.Login_Button.pack(pady=(20,0))
        
        self.or_text_label=customtkinter.CTkLabel(
            self.UserLogin_frame,
            text="or",
            text_color="#ffffff",
            font=("Segoe UI",20,"bold")
        )
        self.or_text_label.pack()
        
        self.Forgot_Button=customtkinter.CTkButton(
            self.UserLogin_frame,
            text="forgot passward?",
            text_color="#ffffff",
            height=40,
            width=150,
            font=("Segoe UI",20,"bold"),
            fg_color="transparent"
        )
        
        self.Forgot_Button.pack()
        
    def CheckUserlogin(self):
        import bcrypt
        import database.db_connection
        
        Username=self.Username_Entry.get().strip()
        password=self.Password_Entry.get().strip()
        
        if not Username or not password:
            self.Password_Entry_error.configure(text="Username and Passward requred")
            return
        
        try:
            conn=database.db_connection.create_connection()
            cursor=conn.cursor()
            query="""Select Username,passward_hash,role from UserLogin where Binary Username=%s"""
            cursor.execute(query,(Username,))
            user = cursor.fetchone()
        except Exception as err:
            self.Password_Entry_error.configure(text="Database error")
            print(err)
        finally:
            if conn:
                cursor.close()
                conn.close()
        print(user)        
        if not user:
            self.Password_Entry_error.configure(text="User not found")
            return
    
        Check_passward=bcrypt.checkpw(password.encode("utf-8"), user[1].encode("utf-8"))
        
        if Check_passward:
            from gui.MainConditionalGUI import SmartInventoryMainConditionalGUI

            for widget in self.root.winfo_children():
                widget.destroy()
            
            SmartInventoryMainConditionalGUI(self.root)
        else:
            self.Password_Entry_error.configure(text="Wrong passward!")


        
if __name__=="__main__":
    root=customtkinter.CTk()
    app=SmartInventoryApp(root)
    root.mainloop()  