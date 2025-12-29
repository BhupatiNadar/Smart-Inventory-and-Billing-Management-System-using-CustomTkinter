import customtkinter as ctk
from PIL import Image


class SmartInventoryManageProducts:
    def __init__(self, root):
        self.root = root

        self.page_size = 5
        self.current_page = 1

        self.build_ui()
        self.load_products(1)


    def build_ui(self):

        
        self.complete_frame = ctk.CTkFrame(self.root, fg_color="#daf5ff")
        self.complete_frame.pack(fill="both", expand=True)

        
        header_frame = ctk.CTkFrame(self.complete_frame, fg_color="#daf5ff")
        header_frame.pack(fill="x", padx=15, pady=10)

        ctk.CTkLabel(
            header_frame,
            text="Manage Products",
            font=("Segoe UI", 30, "bold"),
            text_color="#446dbb"
        ).pack(side="left")

        
        search_frame = ctk.CTkFrame(
            self.complete_frame,
            fg_color="white",
            border_width=2,
            border_color="#446dbb",
            height=70
        )
        search_frame.pack(fill="x", padx=15, pady=15)
        search_frame.pack_propagate(False)

        search_icon = ctk.CTkImage(
            Image.open("./assets/icons/Search_icon.png"),
            size=(30, 30)
        )

        ctk.CTkLabel(search_frame, image=search_icon, text="").pack(
            side="left", padx=20
        )

        self.search_entry = ctk.CTkEntry(
            search_frame,
            placeholder_text="Search Products...",
            font=("Segoe UI", 18),
            width=700,
            height=40
        )
        self.search_entry.pack(side="left", padx=20)

        ctk.CTkButton(
            search_frame,
            text="+ Add Product",
            font=("Segoe UI", 18, "bold"),
            width=180,
            height=40
        ).pack(side="right", padx=20)

        
        table_frame = ctk.CTkFrame(
            self.complete_frame,
            fg_color="white",
            height=300
        )
        table_frame.pack(fill="x", padx=15)
        table_frame.pack_propagate(False)

        
        headers = ["Product ID", "Product Name", "Category", "Quantity", "Price"]

        header_row = ctk.CTkFrame(table_frame, fg_color="#446dbb", height=45)
        header_row.pack(fill="x")
        header_row.pack_propagate(False)

        for title in headers:
            ctk.CTkLabel(
                header_row,
                text=title,
                font=("Segoe UI", 16, "bold"),
                text_color="white",
                width=200,
                anchor="w"
            ).pack(side="left", padx=5)

        self.scroll_frame = ctk.CTkFrame(
            table_frame,
            fg_color="white"
        )
        self.scroll_frame.pack(fill="both", expand=True)

        self.pagination_frame = ctk.CTkFrame(
            self.complete_frame,
            fg_color="#daf5ff",
            height=50
        )
        self.pagination_frame.pack(fill="x", pady=10)

        ctk.CTkButton(
            self.pagination_frame,
            text="⟨ Previous",
            width=120,
            command=self.prev_page
        ).pack(side="left", padx=10)

        for page in range(1, 4):
            ctk.CTkButton(
                self.pagination_frame,
                text=str(page),
                width=40,
                command=lambda p=page: self.load_products(p)
            ).pack(side="left", padx=5)

        ctk.CTkButton(
            self.pagination_frame,
            text="Next ⟩",
            width=120,
            command=self.next_page
        ).pack(side="left", padx=10)
        
        self.Tail_frame=ctk.CTkFrame(
            self.complete_frame,
            bg_color="#ffffff",
            fg_color="#ffffff"
        )
        self.Tail_frame.pack(fill="x",padx=(10,10))
        
        Edit_icon=ctk.CTkImage(
            light_image=Image.open("./assets/icons/Edit_icon.png"),
            size=(30,30)
        )
        
        ctk.CTkButton(
            self.Tail_frame,
            image=Edit_icon,
            text="Edit Product",
            text_color="#000000",
            bg_color="#daf5ff",
            fg_color="#daf5ff",
        ).pack(side="left",padx=10,pady=10)
        
        Delete_product_icon=ctk.CTkImage(
            light_image=Image.open("./assets/icons/Delete_product_icon.png"),
            size=(30,30)
        )
        
        ctk.CTkButton(
            self.Tail_frame,
            image=Delete_product_icon,
            text="Delete Product",
            text_color="#000000",
            bg_color="#daf5ff",
            fg_color="#daf5ff",
        ).pack(side="left",padx=10,pady=10)

    def load_products(self, page):
        self.current_page = page

        
        for widget in self.scroll_frame.winfo_children():
            widget.destroy()

        offset = (page - 1) * self.page_size

        try:
            from database.db_connection import create_connection
            conn = create_connection()
            cursor = conn.cursor()

            query = """
                SELECT p.product_id,
                    p.product_name,
                    c.category_name AS category_name,
                    p.product_quantity,
                    p.price
                FROM product p
                JOIN category c
                ON c.category_id = p.category_id
                ORDER BY p.product_id ASC
                LIMIT %s OFFSET %s
            """
            cursor.execute(query, (self.page_size, offset))
            products = cursor.fetchall()

        except Exception as err:
            print("Database Error:", err)
            return

        finally:
            cursor.close()
            conn.close()

        for product in products:
            self.create_row(product)

    def create_row(self, data):

        row = ctk.CTkFrame(
            self.scroll_frame,
            fg_color="#f8fbff",
            height=40
        )
        row.pack(fill="x", pady=2)
        row.pack_propagate(False)

        for value in data:
            ctk.CTkLabel(
                row,
                text=value,
                font=("Segoe UI", 15),
                width=200,
                anchor="w"
            ).pack(side="left", padx=5)

    def next_page(self):
        self.load_products(self.current_page + 1)

    def prev_page(self):
        if self.current_page > 1:
            self.load_products(self.current_page - 1)
