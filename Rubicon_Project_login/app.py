from flask import Flask, render_template,request
import mysql.connector

app = Flask(__name__)

# MySQL database configuration
db_config={
    'host':'localhost',
    'user':"root",
    'password':"sorry",
    'database':"project"
}

@app.route('/')
def index():
    # cursor = db.cursor()
    # cursor.execute("SELECT * FROM your_table_name")
    # data = cursor.fetchall()
    # cursor.close()
    return render_template('index.html')

@app.route('/login',methods=['post'])
def login():
    if request.method=="post":
        username=request.form['username']
        password=request.form['password']
        store_in_database(username,password)
        return "login successfully"
def store_in_database(username, password):
    conn = mysql.connector.connect(**db_config)
    cursor = conn.cursor()
    insert_query = "INSERT INTO comments (username, password) VALUES (%s, %s)"
    data = (username, password)
    cursor.execute(insert_query, data)
    conn.commit()
    conn.close()
# if __name__ == '__main__':
#     app.run(debug=True)
