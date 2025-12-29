import customtkinter
from PIL import Image

class SmartInventoryManageProducts:
    def __init__(self,root):
        self.root=root
        self.ManageProducts()
        
    def ManageProducts(self):
        
        self.complete_frame=customtkinter.CTkFrame(
            self.root,
            bg_color="#daf5ff",
            fg_color="#daf5ff"
        )
        self.complete_frame.pack(fill="both",expand=True)
        
        self.Header_Text_frame=customtkinter.CTkFrame(
            self.complete_frame,
            bg_color="#daf5ff",
            fg_color="#daf5ff"
        )
        self.Header_Text_frame.pack(fill="x")
        
        self.Header_Text=customtkinter.CTkLabel(
            self.Header_Text_frame,
            text="Manage Products",
            font=("Segoe UI",30,"bold"),
            text_color="#446dbb"
        )
        self.Header_Text.pack(side="left",padx=10)
        
        self.SearchBar_frame=customtkinter.CTkFrame(
            self.complete_frame,
            bg_color="#daf5ff",
            fg_color="#daf5ff",
            border_width=2,
            border_color="blue",
            height=60
        )
        self.SearchBar_frame.pack(fill="x",pady=20,padx=(10,10))
        self.SearchBar_frame.pack_propagate(False)
        
        search_icon=customtkinter.CTkImage(
            light_image=Image.open("./assets/icons/Search_icon.png"),
            size=(40,40)
        )
        
        self.SearchBar_icon_Label=customtkinter.CTkLabel(
            self.SearchBar_frame,
            image=search_icon,
            text="",
            fg_color="#ffffff",
            bg_color="#ffffff"
        )
        self.SearchBar_icon_Label.pack(side="left",padx=(30,30))
        
        self.SearchBar_Entry=customtkinter.CTkEntry(
            self.SearchBar_frame,
            font=("Segoe UI",20,"bold"),
            placeholder_text="Search Products...",
            height=40,
            width=800
        )
        self.SearchBar_Entry.pack(side="left",padx=(30,30))
        
        self.Product_add_button=customtkinter.CTkButton(
            self.SearchBar_frame,
            text="+ Add Product",
            font=("Segoe UI",20,"bold"),
            height=40,
            width=100
        )
        self.Product_add_button.pack(side="left" ,padx=(30,30))
        
        self.Product_Table_frame=customtkinter.CTkFrame(
            self.complete_frame,
            bg_color="white",
            fg_color="white",
            height=400
        )
        self.Product_Table_frame.pack(fill="x",padx=(10,10))
        
        product_details=["Product Id","Product Name","Category","Quantity","Price"]
        
        