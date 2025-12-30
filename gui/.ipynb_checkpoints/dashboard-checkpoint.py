import customtkinter
from PIL import Image

customtkinter.set_appearance_mode("light")
customtkinter.set_default_color_theme("blue")

class SmartInventoryDashboard:
    def __init__(self,root):
        self.root=root
        self.dashboard()
                
    def dashboard(self):
        
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
                light_image=Image.open(f"./assets/icons/{icon}.png"),
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
            bg_color="#ffffff",
            fg_color="#ffffff",
            height=300
        )
        self.sales_performance_and_stockStatus_frame.pack(fill="x",padx=(20,20))
        self.sales_performance_and_stockStatus_frame.pack_propagate(False)
        
        self.sales_performance_and_stockStatus_text=["Sales Performance","Stock Status"]
        

        
    