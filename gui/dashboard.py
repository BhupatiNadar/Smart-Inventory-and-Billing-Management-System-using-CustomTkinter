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
        
        self.Main_widget()
        
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
        self.side_widget_frame.pack_propagate(False)
        
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
            self.btn.pack(pady=8)
            count+=1
            
    def Main_widget(self):
        
        self.Main_widget_complete_frame=customtkinter.CTkFrame(
            self.root,
            bg_color="#daf5ff",
            fg_color="#daf5ff"
        )
        self.Main_widget_complete_frame.pack(fill="both",expand=True)
        
        self.Text_frame=customtkinter.CTkFrame(
            self.Main_widget_complete_frame,
            bg_color="#daf5ff",
            fg_color="#daf5ff"
        )
        self.Text_frame.pack(fill="x")
        
        self.Main_widget_text=customtkinter.CTkLabel(
            self.Text_frame,
            text="Overview",
            font=("Segoe UI",30,"bold"),
            text_color="#446dbb",
        )
        self.Main_widget_text.pack(side="left",padx=10)
        
        self.product_overview_frame=customtkinter.CTkFrame(
            self.Main_widget_complete_frame,
            bg_color="white",
            fg_color="white",
            height=250
        )
        self.product_overview_frame.pack(fill="x",pady=(20,20),padx=(20,20))
        
        frames = ["Total product", "Low Stock items", "Total Sales Today", "Out of Stock"]

        self.product_frames = []   
        
        icons=["TotalProduct_icon","LowStock_icon","TotalSalesIcon","OutOfStock_icon"]
        
        messages=["320","15","58,400","7"]

        for title,icon,message in zip(frames,icons,messages):
            frame = customtkinter.CTkFrame(
                self.product_overview_frame,
                bg_color="#446dbb",
                fg_color="white",
                border_width=2,
                width=250,
                height=180
                )
            frame.pack(side="left", padx=30,pady=10)
            frame.pack_propagate(False)
            
            self.icon=customtkinter.CTkImage(
                light_image=Image.open(f"../assets/icons/{icon}.png"),
                size=(40,40)
            )

            label = customtkinter.CTkLabel(
                frame,
                image=self.icon,
                text=title,
                font=("Segoe UI", 20, "bold"),
                text_color="black",
                compound="left"
                )
            label.pack(pady=20)
            
            label = customtkinter.CTkLabel(
                frame,
                text="---------------",
                font=("Segoe UI", 18, "bold"),
                text_color="black"
                )
            label.pack()
            
            label = customtkinter.CTkLabel(
                frame,
                text=message,
                font=("Segoe UI", 25, "bold"),
                text_color="black"
                )
            label.pack()

        self.product_frames.append(frame)
        
        self.sales_performance_and_stockStatus_frame=customtkinter.CTkFrame(
            self.Main_widget_complete_frame,
            bg_color="#daf5ff",
            fg_color="#daf5ff",
            height=250
        )
        self.sales_performance_and_stockStatus_frame.pack(fill="x",padx=(20,20))
        self.sales_performance_and_stockStatus_frame.pack_propagate(False)
        
        self.sales_performance_and_stockStatus_text=["Sales Performance","Stock Status"]
        

        
    
if __name__=="__main__":
    root=customtkinter.CTk()
    app=SmartInventoryDashboard(root)
    root.mainloop()