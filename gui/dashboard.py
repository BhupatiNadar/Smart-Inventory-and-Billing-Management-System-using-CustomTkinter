import customtkinter
from PIL import Image

customtkinter.set_appearance_mode("light")
customtkinter.set_default_color_theme("blue")

class SmartInventoryDashboard:
    def __init__(self,root):
        
        self.root=root
        self.root.title("Smart Inventry management System")
        self.root.after(10,lambda: self.root.state("zoomed"))
        self.header_widget()
        self.side_widget()
        
    def header_widget(self):
        
        self.header_frame=customtkinter.CTkLabel(
            self.root,
            bg_color="#000000",
            fg_color="#000000",
            height=70
        )
        self.header_frame.pack(fill="x")
        self.header_frame.pack_propagate(False) 
        
        self.header_text1=customtkinter.CTkLabel(
            self.header_frame,
            text="Smart Inventry management System",
            font=("Segoe UI",38,"bold"),
            text_color="#ffffff"
        )
        self.header_text1.pack(side="left")
        
        python_icon=customtkinter.CTkImage(
            light_image=Image.open("../assets/icons/Python_Icon.png"),
            size=(60,60)
        )
        
        profile_icon=customtkinter.CTkImage(
            light_image=Image.open("../assets/icons/profile_icon.png"),
            size=(70,70)
        )
        
        self.icon_label=customtkinter.CTkLabel(
            self.header_frame,
            text="",
            image=profile_icon,
            compound="left"
        )
        self.icon_label.pack(side="right",padx=10)
        
        self.header_text2=customtkinter.CTkLabel(
            self.header_frame,
            text="Build with Python & CustumTkinter",
            font=("Segoe UI",20,"bold"),
            text_color="#ffffff"
        )
        self.header_text2.pack(side="right")
        
        self.icon_label=customtkinter.CTkLabel(
            self.header_frame,
            text="",
            image=python_icon,
            compound="left"
        )
        self.icon_label.pack(side="right")
        
    def side_widget(self):
        self.side_widget_frame=customtkinter.CTkFrame(
            self.root,
            bg_color="#446dbb",
            fg_color="#446dbb",
            width=250
        )
        self.side_widget_frame.pack(side="left",fill="y")
        
        buttons=["Dashboard","Manage Products","sales & Billing","Stock Levels","Suppliers","Reports","Logout"]
        icons=["dashboard","manage_product","selling_product","stocklevel","supplier_icon","report_icon","logout"]
        count=0
        while(count<len(buttons)):
            icon=customtkinter.CTkImage(
                light_image=Image.open(f"../assets/icons/{icons[count]}.png"),
                size=(30,30)
            )
            
            self.btn=customtkinter.CTkButton(
                self.side_widget_frame,
                text=buttons[count],
                image=icon,
                width=200,
                height=60,
                font=("Segoe UI",15,"bold")
            )
            self.btn.pack(pady=2)
            count+=1
            
    
if __name__=="__main__":
    root=customtkinter.CTk()
    app=SmartInventoryDashboard(root)
    root.mainloop()