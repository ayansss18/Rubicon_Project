from flask import Flask, render_template, request
import mysql.connector

app = Flask(__name__)

# MySQL configuration
db_config = {
    'host': 'localhost',
    'user': 'root',
    'password': 'datawizard123',
    'database': 'data_wizard'
}

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/submit', methods=['POST'])
def submit():
    if request.method == 'POST':
        Name = request.form['Name']
        College_Name = request.form['College_Name']
        English_Marks = request.form['English_Marks']
        Maths_Marks = request.form['Maths_Marks']
        Science_Marks = request.form['Science_Marks']

        # Store the data in the database
        store_in_database(Name,College_Name,English_Marks,Maths_Marks,Science_Marks)

        return "Data submitted successfully!"


def store_in_database(Name,College_Name,English_Marks,Maths_Marks,Science_Marks):
    conn = mysql.connector.connect(**db_config)
    cursor = conn.cursor()
    insert_query = "INSERT INTO marks (Name,College_Name,English_Marks,Maths_Marks,Science_Marks) VALUES (%s, %s,%s,%s,%s)"
    data = (Name,College_Name, English_Marks,Maths_Marks,Science_Marks)
    cursor.execute(insert_query, data)
    conn.commit()
    conn.close()