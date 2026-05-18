from flask import Flask, render_template, request, redirect
import mysql.connector

app = Flask(__name__)

# ---------------- DB CONNECTION ----------------
def get_db_connection():
    return mysql.connector.connect(
        host="127.0.0.1",
        user="root",
        password="Pranee@2007",
        database="scholarship_db"
    )

# ---------------- HOME (NOW STUDENTS PAGE) ----------------
@app.route('/', methods=['GET', 'POST'])
def index():
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)

    if request.method == 'POST':
      data = request.form
      print("FORM DATA:", data)   
      try:
            cursor.execute("""
                INSERT INTO Student (Student_ID, Name, Dept_ID, Year, CGPA, Income)
                VALUES (%s, %s, %s, %s, %s, %s)
            """, (
                data['id'], data['name'], data['dept'],
                data['year'], data['cgpa'], data['income']
            ))
            conn.commit()
      except Exception as e:
        print("ERROR:", e)

    cursor.execute("SELECT * FROM Student")
    students = cursor.fetchall()

    conn.close()
    return render_template('students.html', students=students)

# ---------------- STUDENTS (OPTIONAL REDIRECT) ----------------
@app.route('/students')
def students():
    return redirect('/')

# ---------------- SCHOLARSHIPS ----------------
@app.route('/scholarships', methods=['GET', 'POST'])
def scholarships():
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)

    if request.method == 'POST':
        data = request.form
        try:
            cursor.execute("""
                INSERT INTO Scholarship (Scholarship_ID, Name, Criteria, Amount, Deadline)
                VALUES (%s, %s, %s, %s, %s)
            """, (
                data['id'], data['name'], data['criteria'],
                data['amount'], data['deadline']
            ))
            conn.commit()
        except Exception as e:
            print("ERROR:", e)

    cursor.execute("SELECT * FROM Scholarship")
    scholarships = cursor.fetchall()

    conn.close()
    return render_template('scholarships.html', scholarships=scholarships)

# ---------------- APPLICATIONS ----------------
@app.route('/applications', methods=['GET', 'POST'])
def applications():
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)

    if request.method == 'POST':
        data = request.form
        try:
            cursor.execute("""
                INSERT INTO Application (Application_ID, Student_ID, Scholarship_ID, Status, Date)
                VALUES (%s, %s, %s, %s, %s)
            """, (
                data['id'], data['student_id'],
                data['scholarship_id'], "Pending", data['date']
            ))
            conn.commit()
        except Exception as e:
            print("ERROR:", e)

    cursor.execute("SELECT * FROM Application")
    apps = cursor.fetchall()

    conn.close()
    return render_template('applications.html', apps=apps)

# ---------------- APPROVE / REJECT ----------------
@app.route('/update_status/<int:id>/<status>')
def update_status(id, status):
    conn = get_db_connection()
    cursor = conn.cursor()

    cursor.execute(
        "UPDATE Application SET Status=%s WHERE Application_ID=%s",
        (status, id)
    )

    conn.commit()
    conn.close()
    return redirect('/applications')

# ---------------- DISBURSEMENT ----------------
@app.route('/disburse', methods=['POST'])
def disburse():
    data = request.form
    conn = get_db_connection()
    cursor = conn.cursor()

    try:
        cursor.execute("""
            INSERT INTO Disbursement (Disbursement_ID, Application_ID, Amount, Status)
            VALUES (%s, %s, %s, %s)
        """, (
            data['id'], data['app_id'], data['amount'], "Paid"
        ))
        conn.commit()
    except Exception as e:
        print("ERROR:", e)

    conn.close()
    return redirect('/applications')

# ---------------- RUN ----------------
if __name__ == '__main__':
    app.run(debug=True)