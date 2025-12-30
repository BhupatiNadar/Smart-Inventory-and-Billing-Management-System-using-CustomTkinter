# 🧾 Smart Inventory Management System

A **desktop-based Smart Inventory Management System** built using **Python, CustomTkinter, and MySQL**, designed to manage products, categories, suppliers, sales, stock levels, and reports through a modern graphical user interface.

---

## 📌 Features

- 🔐 **User Authentication**
  - Secure login system with role-based access (Admin, Manager, Employee)
  - Password hashing using `bcrypt`

- 📦 **Product Management**
  - Add, update, delete, and view products
  - Category-based product organization
  - Reorder level & stock availability tracking

- 🗂 **Category & Supplier Management**
  - Manage product categories
  - Maintain supplier details linked to categories

- 💰 **Sales & Billing**
  - Create invoices
  - Track daily sales
  - Sales status handling (Pending, Paid, Prepaid, Shipped)

- 📊 **Reports & Analytics**
  - Sales performance visualization using Matplotlib
  - Pie charts and graphical reports
  - Export charts as PNG images

- 🖥 **Modern GUI**
  - Built using **CustomTkinter**
  - Clean layout with icons and responsive design

---

## 🛠 Tech Stack

| Technology | Usage |
|----------|------|
| Python | Core programming language |
| CustomTkinter | Modern GUI framework |
| MySQL | Database |
| Matplotlib | Charts & reports |
| Pillow (PIL) | Image handling |
| bcrypt | Password hashing |

---

## 📂 Project Structure

"""
Smart_inventory_management_system_using_Ctk
├── README.md
├── requirements.txt
├── gui
    ├── .virtual_documents
    │   └── Report
    │   │   └── SalesReportToday.ipynb
    ├── Report
    │   ├── .ipynb_checkpoints
    │   │   └── SalesReportToday-checkpoint.ipynb
    │   ├── sales_report1.png
    │   ├── sales_report2.png
    │   └── SalesReportToday.ipynb
    ├── .ipynb_checkpoints
    │   └── dashboard-checkpoint.py
    ├── dashboard.py
    ├── MainConditionalGUI.py
    ├── Sales_And_Billing.py
    ├── supplier.py
    └── manage_products.py
├── assets
    └── icons
    │   ├── user.png
    │   ├── logout.png
    │   ├── Edit_icon.png
    │   ├── dashboard.png
    │   ├── password.png
    │   ├── stocklevel.png
    │   ├── Python_Icon.png
    │   ├── Search_icon.png
    │   ├── profile_icon.png
    │   ├── report_icon.png
    │   ├── LowStock_icon.png
    │   ├── OutOfStock_icon.png
    │   ├── TotalSalesIcon.png
    │   ├── manage_product.png
    │   ├── selling_product.png
    │   ├── supplier_icon.png
    │   ├── TotalProduct_icon.png
    │   └── Delete_product_icon.png
├── database
    ├── ErDiagram.mwb
    ├── db_connection.py
    ├── .ipynb_checkpoints
    │   └── db_connection-checkpoint.py
    └── Smart_invertry_management_system_using_Ctk.sql
├── .gitignore
├── .virtual_documents
    └── gui
    │   └── Report
    │       └── SalesReportToday.ipynb
└── main.py


"""


---

## ⚙️ Installation & Setup

### 1️⃣ Clone the Repository
```bash
git clone https://github.com/BhupatiNadar/Smart-Inventory-and-Billing-Management-System-using-CustomTkinter.git
cd Smart-Inventory-and-Billing-Management-System-using-CustomTkinter