🎓 Scholarship Management System

A web-based Scholarship Management System built using Flask, MySQL, HTML, and Bootstrap to manage students, scholarships, applications, approvals, and fund disbursements efficiently.

🚀 Features
👨‍🎓 Add and manage students
🏆 Create and manage scholarships
📄 Apply for scholarships
✅ Approve or reject applications
💰 Scholarship disbursement system
📊 View all applications and payments
🔐 MySQL database integration
🛠️ Tech Stack
Frontend: HTML, CSS, Bootstrap
Backend: Flask (Python)
Database: MySQL
Server: Gunicorn
📂 Project Structure
Scholarship-Management-System/
│── app.py
│── requirements.txt
│── Procfile
│── templates/
│   ├── students.html
│   ├── scholarships.html
│   ├── applications.html
│   └── disbursements.html
│── static/
│── database/
⚙️ Installation
1️⃣ Clone the Repository
git clone https://github.com/your-username/scholarship-management-system.git

cd scholarship-management-system
2️⃣ Create Virtual Environment
python -m venv venv
3️⃣ Activate Virtual Environment
Windows
venv\Scripts\activate
Mac/Linux
source venv/bin/activate
4️⃣ Install Dependencies
pip install -r requirements.txt
5️⃣ Configure MySQL Database

Create a MySQL database named:

scholarship_db

Update your MySQL credentials in app.py.

6️⃣ Run the Application
python app.py

The app will run on:

http://127.0.0.1:5001
📌 Main Functionalities
👨‍🎓 Student Management

Add student details including:

Student ID
Name
Department
Year
CGPA
Family Income
🏆 Scholarship Management

Manage scholarship details:

Scholarship ID
Name
Eligibility Criteria
Maximum Amount
Deadline
📄 Application Management

Students can apply for scholarships and admins can:

Approve applications
Reject applications
💰 Disbursement System

Approved applications can receive scholarship payments.

📜 License

This project is for educational purposes.

👩‍💻 Author

Ruthika Reddy
