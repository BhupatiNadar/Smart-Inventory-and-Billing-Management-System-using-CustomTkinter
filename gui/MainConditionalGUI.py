import customtkinter
from PIL import Image

customtkinter.set_appearance_mode("light")
customtkinter.set_default_color_theme("blue")

class SmartInventoryMainConditionalGUI:
    def __init__(self,root):
        
        self.root=root
        self.root.title("Smart Inventry management System")
        self.root.after(10,lambda: self.root.state("zoomed"))
        self.header_widget()
        self.side_widget()
        self.create_content_frame()
        self.show_dashboard()
        
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
            light_image=Image.open("./assets/icons/Python_Icon.png"),
            size=(60,60)
        )
        
        profile_icon=customtkinter.CTkImage(
            light_image=Image.open("./assets/icons/profile_icon.png"),
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
        
        buttons = [
        ("Dashboard", self.show_dashboard, "dashboard"),
        ("Manage Products", self.show_products, "manage_product"),
        ("Sales & Billing", self.show_sales, "selling_product"),
        ("Stock Levels", self.show_stock, "stocklevel"),
        ("Suppliers", self.show_suppliers, "supplier_icon"),
        ("Reports", self.show_reports, "report_icon"),
        ("Logout", self.logout, "logout"),
            ]
        
        self.side_buttons = [] 
        
        for text,command,icon in buttons:
            icon=customtkinter.CTkImage(
                light_image=Image.open(f"./assets/icons/{icon}.png"),
                size=(30,30)
            )
            
            self.btn=customtkinter.CTkButton(
                self.side_widget_frame,
                text=text,
                image=icon,
                width=200,
                height=60,
                font=("Segoe UI",15,"bold"),
                command=command,
                anchor="w",
                compound="left"
            )
            self.side_buttons.append(self.btn)
            self.btn.pack(pady=8)
            
    def create_content_frame(self):
        self.content_frame = customtkinter.CTkFrame(
        self.root,
        fg_color="#f5f6fa"
        )
        self.content_frame.pack(side="left", fill="both", expand=True)
 
    def clear_content(self):
          for widget in self.content_frame.winfo_children():      
            widget.destroy()
            
    def show_dashboard(self):
        self.clear_content()
        from gui.dashboard import SmartInventoryDashboard
        SmartInventoryDashboard(self.content_frame)
        
    def show_products(self):
        self.clear_content()
        from gui.manage_products import SmartInventoryManageProducts
        SmartInventoryManageProducts(self.content_frame)
    
    def show_sales(self):
        self.clear_content()
        from gui.Sales_And_Billing import SmartInventorySalesAndBilling
        SmartInventorySalesAndBilling(self.content_frame)
    
    def show_stock(self):
        self.clear_content()
        pass
    
    def show_suppliers(self):
        self.clear_content()
        from gui.supplier import SmartInventorySupplier
        SmartInventorySupplier(self.content_frame)

    def show_reports(self):
        self.clear_content()
        pass
    
    def logout(self):
        self.clear_content()
        pass